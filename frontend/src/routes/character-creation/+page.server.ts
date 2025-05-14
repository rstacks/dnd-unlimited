import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, isLoggedIn } from "$lib/util/user";
import { error, redirect } from "@sveltejs/kit";
import { getClasses } from "$lib/util/class";
import type { ClassData } from "$lib/util/class";
import type { AbilityScores } from "$lib/util/character";
import { BACKEND_URL, API_KEY } from "$env/static/private";
import { getSpells } from "$lib/util/spell";
import { isBackendRunning } from "$lib/util/ping";

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
  abilityScores: AbilityScores;
  notes?: string;
  meleeWep?: string;
  rangedWep?: string;
}

export const load = (async ({ cookies }) => {
  if (!(await isBackendRunning())) {
    error(503, { message: "Service Unavailable" });
  }

  if (!(await isLoggedIn(cookies))) {
    redirect(303, "/");
  }

  const classes = await getClasses();
  const classSelectedList = initializeClassSelectedList(classes);
  const spells = await getSpells();
  return { classes: classes, classSelectedList: classSelectedList, spells: spells };
}) satisfies PageServerLoad;

export const actions = {
  default: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const sessionId = cookies.get("sessionId")!;
    const userId = await getUserIdBySession(sessionId);
    const characterFormInputs = await getFormData(request);

    await createCharacterInDb(userId, characterFormInputs);
    redirect(303, "/dashboard");
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
  const str = Number(data.get("str")?.toString());
  const dex = Number(data.get("dex")?.toString());
  const con = Number(data.get("con")?.toString());
  const intl = Number(data.get("intl")?.toString());
  const wis = Number(data.get("wis")?.toString());
  const cha = Number(data.get("cha")?.toString());
  const notes = data.get("bkg-notes")?.toString();
  const meleeWep = data.get("melee-wep")?.toString();
  const rangedWep = data.get("ranged-wep")?.toString();
  return {
    classId: classId,
    charName: name,
    abilityScores: {
      str: str,
      dex: dex,
      con: con,
      intl: intl,
      wis: wis,
      cha: cha
    },
    notes: notes,
    meleeWep: meleeWep,
    rangedWep: rangedWep
  };
}

async function createCharacterInDb(userId: number, charInfo: CharacterInfo): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/create-character", {
    method: "POST",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      userId: userId,
      classId: charInfo.classId,
      charName: charInfo.charName,
      abilityScores: charInfo.abilityScores,
      notes: charInfo.notes,
      meleeWep: charInfo.meleeWep,
      rangedWep: charInfo.rangedWep
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}
