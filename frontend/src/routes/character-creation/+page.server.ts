import type { PageServerLoad } from "./$types";
import { getUserIdBySession } from "$lib/util/user";
import { redirect } from "@sveltejs/kit";
import { getClasses } from "$lib/util/class";

export const load = (async ({ cookies }) => {
  const sessionId = cookies.get("sessionId");
  if (!sessionId) {
    redirect(303, "/");
  }
  const userId = await getUserIdBySession(sessionId);
  if (userId === -1) {
    redirect(303, "/");
  }

  const classes = await getClasses();
  return { classes: classes };
}) satisfies PageServerLoad;
