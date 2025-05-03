import type { PageServerLoad, Actions } from "./$types";
import { v4 as uuidv4 } from "uuid";
import { BACKEND_URL } from "$env/static/private";
import bcrypt from "bcrypt";
import { error, type Cookies } from "@sveltejs/kit";

const SALT_ROUNDS = 10;

interface FormResponses {
  phone?: string;
  name?: string;
}

interface UserInfo {
  id: number;
  phone_hash: string;
}

interface UsersJSON {
  users: UserInfo[];
}

/**
 * TODO: 
 * check for sessionId. If it exists in the db, redirect eventually.
 * For now do something to indicate this
 */
export const load = (async ({ cookies }) => {
  const badPhone = cookies.get("badPhone");
  const badName = cookies.get("badName");
  const onRegisterForm = cookies.get("onRegisterForm");
  const accountNotFound = cookies.get("accountNotFound");
  const accountAlreadyExists = cookies.get("accountAlreadyExists");
  return {
    badPhone: badPhone,
    badName: badName,
    onRegisterForm: onRegisterForm,
    accountNotFound: accountNotFound,
    accountAlreadyExists: accountAlreadyExists
  };
}) satisfies PageServerLoad;

export const actions = {
  login: async ({ cookies, request }) => {
    initializeCookies(cookies, "login");

    const formResponses = await getPhoneAndName(request);
    const phonePlaintext = formResponses.phone;

    if (!phonePlaintext || !isValidPhone(phonePlaintext)) {
      cookies.set("badPhone", "true", { path: "/" });
      return;
    }

    const userId = await getUserId(phonePlaintext);
    if (userId === -1) {
      cookies.set("accountNotFound", "true", { path: "/" });
      return;
    }

    // const resp = await fetch(BACKEND_URL + "/ping");
    // if (resp.ok) {
    //   const msg = await resp.text();
    //   console.log("API response: " + msg);
    // }


    
    
    // const sessionId = uuidv4();
    // cookies.set("sessionId", sessionId, { path: "/" });

    // console.log(phoneHash);

    // Steps:
    // 2. Hash it
    //    a. Check the database for a match. If match, make note of the user_id
    //       Else, update form with error message
    // 3. Generate session id
    // 4. Set the session id cookie, then send the session id to the db
  },
  register: async ({ cookies, request }) => {
    initializeCookies(cookies, "register");

    const formResponses = await getPhoneAndName(request);
    const phonePlaintext = formResponses.phone;
    const username = formResponses.name;

    if (!phonePlaintext || !isValidPhone(phonePlaintext)) {
      cookies.set("badPhone", "true", { path: "/" });
      return;
    }
    if (!username || !isValidName(username)) {
      cookies.set("badName", "true", { path: "/" });
      return;
    }

    const userId = await getUserId(phonePlaintext);
    if (userId !== -1) {
      cookies.set("accountAlreadyExists", "true", { path: "/" });
      return;
    }

    const phoneHash = await bcrypt.hash(phonePlaintext.toString(), SALT_ROUNDS);
    const sessionId = uuidv4();
    cookies.set("sessionId", sessionId, { path: "/" });

    // Redirect to a registration page. Steps will be similar to login.
    // This probably doesn't need to be a form action. Make the registration
    // button an anchor tag outside of the form element, and send 'em to 
    // a new page
  }
} satisfies Actions;

function initializeCookies(cookies: Cookies, formtype: "login" | "register"): void {
  if (formtype === "login") {
    cookies.set("onRegisterForm", "false", { path: "/" });
  } else {
    cookies.set("onRegisterForm", "true", { path: "/" });
  }
  cookies.set("accountNotFound", "false", { path: "/" });
  cookies.set("accountAlreadyExists", "false", { path: "/" });
  cookies.set("badPhone", "false", { path: "/" });
  cookies.set("badName", "false", { path: "/" });
}

async function getPhoneAndName(request: Request): Promise<FormResponses> {
  const data = await request.formData();
  const phone = data.get("phone")?.toString();
  const name = data.get("user-name")?.toString();
  return {
    phone: phone,
    name: name
  };
}

function isValidPhone(phone: string): boolean {
  if (!phone || phone.trim().length <= 0) {
    return false;
  }
  if (phone.match(/[0-9]{10}/)?.at(0) !== phone.trim()) {
    return false;
  }
  return true;
}

function isValidName(name: string): boolean {
  if (name && name.trim().length > 0) {
    return true;
  }
  return false;
}

async function getUserId(phonePlaintext: string): Promise<number> {
  const resp = await fetch(BACKEND_URL + "/users");
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
  const usersJson: UsersJSON = await resp.json();
  const allUsers = usersJson.users;

  for (const user of allUsers) {
    const nextPhoneHash = user.phone_hash;
    const userExists = await bcrypt.compare(phonePlaintext, nextPhoneHash);
    if (userExists) {
      return user.id;
    }
  }
  return -1;
}
