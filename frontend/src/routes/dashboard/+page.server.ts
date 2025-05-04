import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, getUserById } from "$lib/util/user";
import { BACKEND_URL, API_KEY } from "$env/static/private"; 
import { redirect, error } from "@sveltejs/kit";

export const load = (async ({ cookies }) => {
  const sessionId = cookies.get("sessionId");
  if (!sessionId) {
    redirect(303, "/");
  }
  const userId = await getUserIdBySession(sessionId);
  if (userId === -1) {
    redirect(303, "/");
  }
  
  const userData = await getUserById(userId);
  return { name: userData.user_name };
}) satisfies PageServerLoad;

export const actions = {
  logout: async ({ cookies }) => {
    const sessionId = cookies.get("sessionId");
    if (!sessionId) {
      return;
    }
    const userId = await getUserIdBySession(sessionId);

    await logoutInDb(userId);
    cookies.delete("sessionId", { path: "/" });
  },
  updateName: async ({ cookies, request }) => {
    const name = await getName(request);
    if (!name || !isValidName(name)) {
      return;
    }

    const sessionId = cookies.get("sessionId");
    if (!sessionId) {
      return;
    }
    const userId = await getUserIdBySession(sessionId);

    await setNameInDb(userId, name);
  }
} satisfies Actions;

async function getName(request: Request): Promise<string | undefined> {
  const data = await request.formData();
  const name = data.get("user-name")?.toString();
  return name;
}

function isValidName(name: string): boolean {
  if (name && name.trim().length > 0) {
    return true;
  }
  return false;
}

async function setNameInDb(userId: number, name: string): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/users/" + userId, {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      userName: name
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}

async function logoutInDb(userId: number): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/logout", {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      "userId": userId
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}
