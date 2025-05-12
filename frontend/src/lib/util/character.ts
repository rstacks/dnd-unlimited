import { BACKEND_URL, API_KEY } from "$env/static/private";
import { error } from "@sveltejs/kit";
import type { Spell } from "./spell";

export interface AbilityScores {
  str: number;
  dex: number;
  con: number;
  intl: number;
  wis: number;
  cha: number;
}

export interface Weapon {
  weapon_name: string;
  weapon_type: string;
  weapon_desc: string;
  damage_die: string;
}

export interface Item {
  item_name: string;
  item_desc: string;
  amount: number;
}

export interface Character {
  id: number;
  class_id: number;
  class_name: string;
  hit_dice: string;
  feat_name: string;
  feat_desc: string;
  character_name: string;
  lvl: number;
  xp: number;
  str: number;
  dex: number;
  con: number;
  intl: number;
  wis: number;
  cha: number;
  armor_class: number;
  hp: number;
  max_hp: number;
  notes: string;
  status_effects: string;
  lvl_1_spell_slots: number;
  lvl_2_spell_slots: number;
  lvl_3_spell_slots: number;
  lvl_4_spell_slots: number;
  proficiency_bonus: number;
  speed: number;
  rages: number;
  rage_damage: number;
  second_wind: number;
  martial_arts: string;
  sneak_attack: string;
  saves: string[];
  skills: string[];
  spells: Spell[];
  weapons: Weapon[];
  items: Item[]
}

interface CharactersJSON {
  characters: Character[];
}

export interface Skill {
  skill_name: string;
  ability_name: string;
}

interface SkillsJSON {
  skills: Skill[];
}

// export interface ClassStats {
//   proficiency_bonus: number;
//   rages: number;
//   rage_damage: number;
//   lvl_1_spell_slots: number;
//   lvl_2_spell_slots: number;
//   lvl_3_spell_slots: number;
//   lvl_4_spell_slots: number;
//   second_wind: number;
//   martial_arts: string;
//   sneak_attack: string;
// }

export async function getUserCharacters(userId: number): Promise<Character[]> {
  const resp = await fetch(BACKEND_URL + "/characters/" + userId, {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }

  const respJson: CharactersJSON = await resp.json();
  const allCharacters: Character[] = respJson.characters;
  return allCharacters;
}

export async function getSkills(): Promise<Skill[]> {
  const resp = await fetch(BACKEND_URL + "/skills", {
    headers: { "Authorization": "Bearer " + API_KEY }
  });
  if (!resp.ok) {
    error(503, { message: "Server offline" });
  }

  const respJson: SkillsJSON = await resp.json();
  let allSkills: Skill[] = respJson.skills;
  const sortedSkills = allSkills.sort((lhs, rhs) => {
    return lhs.skill_name.localeCompare(rhs.skill_name);
  });

  return sortedSkills;
}

// export async function getClassStatsByLevel(classId: number, lvl: number): Promise<ClassStats> {
//   const resp = await fetch(BACKEND_URL + "/levels/" + lvl + "/" + classId, {
//     headers: { "Authorization": "Bearer " + API_KEY }
//   });
//   if (!resp.ok) {
//     error(503, { message: "Server offline" });
//   }

//   const statsJson: ClassStats = await resp.json();
//   return statsJson;
// }

// export async function levelUp() {
//   // increase max hp by average hit die roll result (ceil) + CON
//   // Remember that when CON mod increases by 1, max HP increase by 1 per current level

// }
