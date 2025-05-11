import type { PageServerLoad, Actions } from "./$types";
import { getUserIdBySession, getUserById, isLoggedIn } from "$lib/util/user";
import { BACKEND_URL, API_KEY } from "$env/static/private"; 
import { redirect, error } from "@sveltejs/kit";
import { getSkills, getUserCharacters } from "$lib/util/character";

interface CharacterSheetFields {
  id: number;
  xp: number;
  notes?: string;
  hp: number;
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
    console.log(charSheetFields);
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
  const id = data.get("char-id");
  const xp = data.get("xp");
  const notes = data.get("notes");
  const hp = data.get("hp");

  return {
    id: Number(id?.toString()),
    xp: Number(xp?.toString()),
    notes: notes?.toString(),
    hp: Number(hp?.toString())
  };
}
