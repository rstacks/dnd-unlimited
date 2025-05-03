import type { PageServerLoad } from "./$types";
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