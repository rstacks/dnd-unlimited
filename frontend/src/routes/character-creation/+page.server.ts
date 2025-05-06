import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, isLoggedIn } from "$lib/util/user";
import { redirect } from "@sveltejs/kit";
import { getClasses } from "$lib/util/class";
import type { ClassData } from "$lib/util/class";
import type { AbilityScores } from "$lib/util/character";

/**
 * Tracks whether a given class has been selected by the user
 * for their character.
 */
export interface ClassSelected {
  classId: number;
  selected: boolean;
}

interface CharacterInfo {
  classId?: number;
  charName?: string;
  abilityScores?: AbilityScores;
  notes?: string;
  meleeWep?: string;
  rangedWep?: string;
}

export const load = (async ({ cookies }) => {
  if (!(await isLoggedIn(cookies))) {
    redirect(303, "/");
  }

  const classes = await getClasses();
  const classSelectedList = initializeClassSelectedList(classes);
  return { classes: classes, classSelectedList: classSelectedList };
}) satisfies PageServerLoad;

export const actions = {
  default: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const sessionId = cookies.get("sessionId")!;
    const userId = await getUserIdBySession(sessionId);

    const formResults = await getFormData(request);
    console.log(formResults);
    console.log(JSON.stringify(formResults.abilityScores));

    //redirect(303, "/dashboard");
  }
} satisfies Actions;

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

async function getFormData(request: Request): Promise<CharacterInfo> {
  const data = await request.formData();
  const classId = Number(data.get("class-id")?.toString());
  const name = data.get("char-name")?.toString();
  const abilityScores = data.get("ability-scores")?.valueOf() as AbilityScores | undefined;
  const notes = data.get("bkg-notes")?.toString();
  const meleeWep = data.get("melee-wep")?.toString();
  const rangedWep = data.get("ranged-wep")?.toString();
  return {
    classId: classId,
    charName: name,
    abilityScores: abilityScores,
    notes: notes,
    meleeWep: meleeWep,
    rangedWep: rangedWep
  };
}
