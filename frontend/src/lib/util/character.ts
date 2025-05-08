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
  saves: string[],
  skills: string[],
  spells: Spell[],
  weapons: Weapon[],
  items: Item[]
}

interface CharactersJSON {
  characters: Character[];
}

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
