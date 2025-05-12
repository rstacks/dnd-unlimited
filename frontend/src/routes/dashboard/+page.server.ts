import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, getUserById, isLoggedIn } from "$lib/util/user";
import { BACKEND_URL, API_KEY } from "$env/static/private"; 
import { redirect, error } from "@sveltejs/kit";
import { getSkills, getUserCharacters } from "$lib/util/character";

interface CharacterSheetFields {
  id: number;
  xp: number;
  notes: string;
  hp: number;
}

interface LevelUpFormFields {
  charId: number;
  nextLvl: number;
  classId: number;
  abilitiesToUpgrade: string;     // Space-separated list of strings
  numAbilitiesToUpgrade: number;
  hitDie: string;
  con: number;
}

export const load = (async ({ cookies }) => {
  if (!(await isLoggedIn(cookies))) {
    redirect(303, "/");
  }

  const sessionId = cookies.get("sessionId")!;
  const userId = await getUserIdBySession(sessionId);
  const userData = await getUserById(userId);
  const characters = await getUserCharacters(userId);
  const skills = await getSkills();
  let showCharacterSheetStates: boolean[] = [];
  for (const character of characters) {
    showCharacterSheetStates.push(false);
  }

  return {
    name: userData.user_name,
    characters: characters,
    charSheetStates: showCharacterSheetStates,
    skills: skills
  };
}) satisfies PageServerLoad;

export const actions = {
  logout: async ({ cookies }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const sessionId = cookies.get("sessionId")!;
    const userId = await getUserIdBySession(sessionId);

    await logoutInDb(userId);
    cookies.delete("sessionId", { path: "/" });
  },
  updateName: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const name = await getName(request);
    if (!name || !isValidName(name)) {
      return;
    }

    const sessionId = cookies.get("sessionId")!;
    const userId = await getUserIdBySession(sessionId);

    await setNameInDb(userId, name);
  },
  updateCharacter: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const charSheetFields = await getCharacterSheetFields(request);
    await updateCharInDb(charSheetFields);
  },
  levelUp: async ({ cookies, request }) => {
    if (!(await isLoggedIn(cookies))) {
      redirect(303, "/");
    }

    const levelUpFormFields = await getLevelUpFormFields(request);
    await levelUpInDb(levelUpFormFields);
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
      userName: name.trim()
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

async function getCharacterSheetFields(request: Request): Promise<CharacterSheetFields> {
  const data = await request.formData();
  const idInput = data.get("char-id");
  const xpInput = data.get("xp");
  const notesInput = data.get("notes");
  const hpInput = data.get("hp");

  let notesVal = "";
  if (notesInput) {
    notesVal = notesInput.toString();
  }

  return {
    id: Number(idInput?.toString()),
    xp: Number(xpInput?.toString()),
    notes: notesVal,
    hp: Number(hpInput?.toString())
  };
}

async function updateCharInDb(charSheetFields: CharacterSheetFields): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/characters", {
    method: "PATCH",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      id: charSheetFields.id,
      xp: charSheetFields.xp,
      notes: charSheetFields.notes,
      hp: charSheetFields.hp
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}

async function getLevelUpFormFields(request: Request): Promise<LevelUpFormFields> {
  const data = await request.formData();
  const charId = data.get("char-id");
  const nextLvl = data.get("next-lvl");
  const classId = data.get("class-id");
  const abilitiesToUpgradeInput = data.get("ability-scores");
  const numAbilitiesToUpgrade = data.get("num-ability-scores");
  const hitDieInput = data.get("hit-die");
  const con = data.get("con");

  let abilitiesToUpgrade = "";
  if (abilitiesToUpgradeInput) {
    abilitiesToUpgrade = abilitiesToUpgradeInput.toString();
  }
  let hitDie = "";
  if (hitDieInput) {
    hitDie = hitDieInput.toString();
  }

  return {
    charId: Number(charId?.toString()),
    nextLvl: Number(nextLvl?.toString()),
    classId: Number(classId?.toString()),
    abilitiesToUpgrade: abilitiesToUpgrade,
    numAbilitiesToUpgrade: Number(numAbilitiesToUpgrade?.toString()),
    hitDie: hitDie,
    con: Number(con?.toString())
  };
}

async function levelUpInDb(formFields: LevelUpFormFields): Promise<void> {
  const resp = await fetch(BACKEND_URL + "/characters", {
    method: "PUT",
    headers: {
      "Authorization": "Bearer " + API_KEY,
      "content-type": "application/json"
    },
    body: JSON.stringify({
      charId: formFields.charId,
      nextLvl: formFields.nextLvl,
      classId: formFields.classId,
      abilitiesToUpgrade: formFields.abilitiesToUpgrade,
      numAbilitiesToUpgrade: formFields.numAbilitiesToUpgrade,
      hitDie: formFields.hitDie,
      con: formFields.con
    })
  });

  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }
}
