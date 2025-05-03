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

interface FormCookies {
  badPhone?: string;
  badName?: string;
  onRegisterForm?: string;
  accountNotFound?: string;
  accountAlreadyExists?: string;
}

/**
 * TODO: 
 * check for sessionId. If it exists in the db, redirect eventually.
 * For now do something to indicate this
 */
export const load = (async ({ cookies }) => {
  const formCookies = getFormCookies(cookies);
  resetFormCookies(cookies);
  return formCookies;
}) satisfies PageServerLoad;

export const actions = {
  login: async ({ cookies, request }) => {
    cookies.set("onRegisterForm", "false", { path: "/" });

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

    const sessionId = uuidv4();
    cookies.set("sessionId", sessionId, { path: "/" });

    // 4. Set the session id cookie, then send the session id and hash to the db
  },
  register: async ({ cookies, request }) => {
    cookies.set("onRegisterForm", "true", { path: "/" });

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

    
  }
} satisfies Actions;

function resetFormCookies(cookies: Cookies): void {
  cookies.set("accountNotFound", "false", { path: "/" });
  cookies.set("accountAlreadyExists", "false", { path: "/" });
  cookies.set("badPhone", "false", { path: "/" });
  cookies.set("badName", "false", { path: "/" });
}

function getFormCookies(cookies: Cookies): FormCookies {
  return {
    badPhone: cookies.get("badPhone"),
    badName: cookies.get("badName"),
    onRegisterForm: cookies.get("onRegisterForm"),
    accountNotFound: cookies.get("accountNotFound"),
    accountAlreadyExists: cookies.get("accountAlreadyExists")
  };
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
