import type { PageServerLoad } from "./$types";
import { getUserIdBySession } from "$lib/util/user";
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
  const sessionId = cookies.get("sessionId");
  if (!sessionId) {
    redirect(303, "/");
  }
  const userId = await getUserIdBySession(sessionId);
  if (userId === -1) {
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
