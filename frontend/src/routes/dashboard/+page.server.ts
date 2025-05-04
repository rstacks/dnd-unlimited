import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, getUserById } from "$lib/util/user";
import { redirect } from "@sveltejs/kit";

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
  logout: async ({ cookies, request }) => {

  },
  updateName: async ({ request }) => {
    const name = await getName(request);
    if (!name || !isValidName(name)) {
      return;
    }

    
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
