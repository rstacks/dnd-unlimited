import { BACKEND_URL, API_KEY } from "$env/static/private";
import { error } from "@sveltejs/kit";

export interface Spell {
  spell_type: string;
  spell_name: string;
  spell_desc: string;
  class_id: number;
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

export async function getSpells(): Promise<Spell[]> {
  const resp = await fetch(BACKEND_URL + "/spells", {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" })
  }

  const respJson: SpellJSON = await resp.json();
  const classSpells = respJson.spells;
  return classSpells;
}
