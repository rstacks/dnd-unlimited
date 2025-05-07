import { BACKEND_URL, API_KEY } from "$env/static/private";
import { error } from "@sveltejs/kit";

export interface Spell {
  type: string;
  name: string;
  desc: string;
}

interface SpellJSON {
  spells: Spell[];
}

export async function getSpellsByClass(classId: number): Promise<Spell[]> {
  const resp = await fetch(BACKEND_URL + "/spells/" + classId, {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" })
  }

  const respJson: SpellJSON = await resp.json();
  const classSpells = respJson.spells;
  return classSpells;
}
