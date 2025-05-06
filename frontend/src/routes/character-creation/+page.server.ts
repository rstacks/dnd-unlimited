import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, isLoggedIn } from "$lib/util/user";
import { redirect } from "@sveltejs/kit";
import { getClasses } from "$lib/util/class";
import { type ClassData } from "$lib/util/class";

/**
 * Tracks whether a given class has been selected by the user
 * for their character.
 */
export interface ClassSelected {
  classId: number;
  selected: boolean;
}

export const load = (async ({ cookies }) => {
  if (!(await isLoggedIn(cookies))) {
    redirect(303, "/");
  }

  const classes = await getClasses();
  const classSelectedList = initializeClassSelectedList(classes);
  return { classes: classes, classSelectedList: classSelectedList };
}) satisfies PageServerLoad;

function initializeClassSelectedList(classes: ClassData[]): ClassSelected[] {
  let classSelectedList: ClassSelected[] = [];
  for (const classData of classes) {
    classSelectedList.push({
      classId: classData.id,
      selected: false
    });
  }
  return classSelectedList;
}

export const actions = {
  default: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const sessionId = cookies.get("sessionId")!;
    const userId = await getUserIdBySession(sessionId);

  }
} satisfies Actions;
