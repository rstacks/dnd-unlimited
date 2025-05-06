import type { PageServerLoad, Actions } from "./$types";
import { v4 as uuidv4 } from "uuid";
import { BACKEND_URL, API_KEY } from "$env/static/private";
import bcrypt from "bcrypt";
import { error, redirect, type Cookies } from "@sveltejs/kit";
import { getUserIdByPhone, isLoggedIn } from "$lib/util/user";

const SALT_ROUNDS = 10;

interface FormResponses {
  phone?: string;
  name?: string;
}

interface FormCookies {
  badPhone?: string;
  badName?: string;
  onRegisterForm?: string;
  accountNotFound?: string;
  accountAlreadyExists?: string;
}

export const load = (async ({ cookies }) => {
  if (await isLoggedIn(cookies)) {
    redirect(303, "/dashboard");
  }

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

    const userId = await getUserIdByPhone(phonePlaintext);
    if (userId === -1) {
      cookies.set("accountNotFound", "true", { path: "/" });
      return;
    }

    const sessionIdPlaintext = uuidv4();
    const sessionIdHash = await bcrypt.hash(sessionIdPlaintext, SALT_ROUNDS);
    
    await loginInDb(userId, sessionIdHash);
    cookies.set("sessionId", sessionIdPlaintext, { path: "/" });
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

    const userId = await getUserIdByPhone(phonePlaintext);
    if (userId !== -1) {
      cookies.set("accountAlreadyExists", "true", { path: "/" });
      return;
    }

    const phoneHash = await bcrypt.hash(phonePlaintext.toString(), SALT_ROUNDS);
    const sessionIdPlaintext = uuidv4();
    const sessionIdHash = await bcrypt.hash(sessionIdPlaintext, SALT_ROUNDS);
    
    await registerInDb(phoneHash, username, sessionIdHash);
    cookies.set("sessionId", sessionIdPlaintext, { path: "/" });
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

async function loginInDb(userId: number, sessionId: string): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/login", {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      userId: userId,
      sessionId: sessionId
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}

async function registerInDb(phoneHash: string, username: string, sessionId: string): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/register", {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      phoneHash: phoneHash,
      userName: username.trim(),
      sessionId: sessionId
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}
