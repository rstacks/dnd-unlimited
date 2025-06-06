# Functions for interacting with the database are defined here.

import sqlite3
from math import floor

DB_CONNECTION_STR = "./db/dnd-db.db"
SAVE_SHORT_TO_LONG = {
  "str": "Strength",
  "dex": "Dexterity",
  "con": "Constitution",
  "intl": "Intelligence",
  "wis": "Wisdom",
  "cha": "Charisma"
}

def _get_db_connection() -> sqlite3.Connection:
  con = sqlite3.connect(DB_CONNECTION_STR)
  return con

def _assign_class_saves(cur: sqlite3.Cursor, class_id: int, class_data: dict) -> None:
  saves_query = "SELECT st.st_name FROM class_saving_throw_proficiencies AS cstp INNER JOIN saving_throws AS st ON cstp.saving_throw_id = st.id WHERE cstp.class_id = ?"
  cur.execute(saves_query, (class_id,))
  class_saves: list[list] = cur.fetchall()
  for class_save in class_saves:
    class_data["saves"].append(SAVE_SHORT_TO_LONG[class_save[0]])

def _assign_class_skills(cur: sqlite3.Cursor, class_id: int, class_data: dict) -> None:
  skills_query = "SELECT s.skill_name FROM class_skill_proficiencies AS csp INNER JOIN skills AS s ON csp.skill_id = s.id WHERE csp.class_id = ?"
  cur.execute(skills_query, (class_id,))
  class_skills: list[list] = cur.fetchall()
  for class_skill in class_skills:
    class_data["skills"].append(class_skill[0])

def _get_ability_modifier(ability_score: int) -> int:
  return floor((ability_score - 10) / 2)

def _get_avg_die_roll(hit_die: str) -> int:
  max_roll = int(hit_die[1:])
  return (max_roll / 2) + 1

def get_users():
  con = _get_db_connection()
  cur = con.cursor()
  cur.execute("SELECT id, phone_hash, session_uuid FROM users")
  raw_result: list[list] = cur.fetchall()
  con.close()
  
  formatted_records = []
  for user_data in raw_result:
    user_dict = {"id": user_data[0], "phone_hash": user_data[1], "session_uuid": user_data[2]}
    formatted_records.append(user_dict)

  return { "users": formatted_records }

def get_user_by_id(id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT phone_hash, user_type, user_name, session_uuid FROM users WHERE id = ?", (id,))
  user_data: list[str] = cur.fetchone()

  con.close()

  if not user_data:
    raise ValueError("User not found")

  return {
    "phone_hash": user_data[0],
    "user_type": user_data[1],
    "user_name": user_data[2],
    "session_uuid": user_data[3]
  }

def set_user_name(user_id: int, name: str):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET user_name = ? WHERE id = ?", (name, user_id))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def register_user(phone_hash: str, user_name: str, session_id: str):
  values = (phone_hash, user_name, session_id)

  con = _get_db_connection()
  
  cur = con.cursor()
  cur.execute("INSERT INTO users (user_type, phone_hash, user_name, session_uuid) VALUES ('player', ?, ?, ?)", values)
  con.commit()

  cur.execute("SELECT id FROM users WHERE session_uuid = ?", (session_id,))
  new_user_id: list[int] = cur.fetchone()
  
  con.close()

  return { "new_user_id": new_user_id[0] }

def login_user(user_id: int, session_id: str):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET session_uuid = ? WHERE id = ?", (session_id, user_id))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def logout_user(user_id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET session_uuid = '' WHERE id = ?", (user_id,))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def get_classes():
  class_and_feat_query = "SELECT c.id, c.class_name, c.class_desc, c.hit_dice, f.feat_name, f.feat_desc FROM classes AS c INNER JOIN feats AS f ON c.feat_id = f.id"

  con = _get_db_connection()
  cur = con.cursor()
  cur.execute(class_and_feat_query)
  class_and_feat_records: list[list] = cur.fetchall()

  formatted_records = []
  for class_and_feat_record in class_and_feat_records:    
    record_dict = {
      "id": class_and_feat_record[0],
      "class_name": class_and_feat_record[1],
      "class_desc": class_and_feat_record[2],
      "hit_dice": class_and_feat_record[3],
      "feat_name": class_and_feat_record[4],
      "feat_desc": class_and_feat_record[5],
      "saves": [],
      "skills": []
    }

    _assign_class_saves(cur, class_and_feat_record[0], record_dict)
    _assign_class_skills(cur, class_and_feat_record[0], record_dict)

    formatted_records.append(record_dict)

  con.close()

  return { "classes": formatted_records }

def get_spells_by_class(class_id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT spell_type, spell_name, spell_desc FROM spells WHERE class_id = ?", (class_id,))
  spell_records: list[list] = cur.fetchall()

  con.close()

  formatted_records = []
  for spell_record in spell_records:
    formatted_records.append({
      "spell_type": spell_record[0],
      "spell_name": spell_record[1],
      "spell_desc": spell_record[2],
      "class_id": class_id
    })

  return { "spells": formatted_records }

def get_spells():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT spell_type, spell_name, spell_desc, class_id FROM spells")
  spell_records: list[list] = cur.fetchall()

  con.close()

  formatted_records = []
  for spell_record in spell_records:
    formatted_records.append({
      "spell_type": spell_record[0],
      "spell_name": spell_record[1],
      "spell_desc": spell_record[2],
      "class_id": spell_record[3]
    })

  return { "spells": formatted_records }  

def create_weapon(name: str, type: str) -> int | None:
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("INSERT INTO weapons (weapon_name, weapon_type) VALUES (?, ?)", (name, type))
  con.commit()
  weapon_id = cur.lastrowid

  con.close()

  return weapon_id

def get_character_weapons(char_id: int):
  char_weapons_query = "SELECT w.weapon_name, w.weapon_type, w.weapon_desc, cw.damage_die FROM character_weapons AS cw INNER JOIN weapons AS w ON cw.weapon_id = w.id WHERE cw.character_id = ?"

  con = _get_db_connection()

  cur = con.cursor()
  cur.execute(char_weapons_query, (char_id,))
  raw_weapons_records: list[list] = cur.fetchall()

  con.close()
  
  formatted_records = []
  for weapon_record in raw_weapons_records:
    formatted_records.append({
      "weapon_name": weapon_record[0],
      "weapon_type": weapon_record[1],
      "weapon_desc": weapon_record[2],
      "damage_die": weapon_record[3]
    })

  return { "weapons": formatted_records }

def get_character_items(char_id: int):
  char_items_query = "SELECT i.item_name, i.item_desc, ci.amount FROM character_items AS ci INNER JOIN items AS i ON ci.item_id = i.id WHERE ci.character_id = ?"

  con = _get_db_connection()

  cur = con.cursor()
  cur.execute(char_items_query, (char_id,))
  raw_items_records: list[list] = cur.fetchall()

  con.close()
  
  formatted_records = []
  for item_record in raw_items_records:
    formatted_records.append({
      "item_name": item_record[0],
      "item_desc": item_record[1],
      "amount": item_record[2]
    })

  return { "items": formatted_records }

def create_class_character(class_id: int) -> int | None:
  class_info_query = "SELECT c.hit_dice, f.feat_name FROM classes AS c INNER JOIN feats AS f ON c.feat_id = f.id WHERE c.id = ?"
  general_insertion_stmt = "INSERT INTO characters (class_id, lvl, xp, proficiency_bonus, speed, hp, max_hp) VALUES (?, ?, ?, ?, ?, ?, ?)"
  feat_update_stmt = "UPDATE characters SET ? = ? WHERE id = ?"

  con = _get_db_connection()
  cur = con.cursor()
  
  cur.execute(class_info_query, (class_id,))
  class_record = cur.fetchone()
  hit_die: str = class_record[0]
  feat: str = class_record[1]
  max_hit_die_roll = int(hit_die[1:])

  cur.execute(general_insertion_stmt, (class_id, 1, 0, 2, 30, max_hit_die_roll, max_hit_die_roll))
  con.commit()
  character_id = cur.lastrowid

  if feat == "Spellcasting":
    # Warlocks (class_id == 11) get less slots than all other spellcasters
    spell_slots = 1 if class_id == 11 else 2
    cur.execute(feat_update_stmt.replace("?", "lvl_1_spell_slots", 1), (spell_slots, character_id))
  if feat == "Rage":
    cur.execute(feat_update_stmt.replace("?", "rages", 1), (2, character_id))
    cur.execute(feat_update_stmt.replace("?", "rage_damage", 1), (2, character_id))
  if feat == "Second Wind":
    cur.execute(feat_update_stmt.replace("?", "second_wind", 1), (2, character_id))
  if feat == "Martial Arts":
    cur.execute(feat_update_stmt.replace("?", "martial_arts", 1), ("1d6", character_id))
  if feat == "Sneak Attack":
    cur.execute(feat_update_stmt.replace("?", "sneak_attack", 1), ("1d6", character_id))

  con.commit()
  con.close()

  return character_id

def create_character(user_id: int, class_id: int, name: str, ability_scores: dict, notes: str, weapon_ids: list[int]):
  update_char_stmt = "UPDATE characters SET user_id = ?, character_name = ?, str = ?, dex = ?, con = ?, intl = ?, wis = ?, cha = ?, armor_class = ?, hp = hp + ?, max_hp = max_hp + ?, notes = ? WHERE id = ?"
  insert_char_weps_stmt = "INSERT INTO character_weapons VALUES (?, ?, ?)"

  char_id = create_class_character(class_id)
  character_weapons_records = [(char_id, wep_id, "1d6") for wep_id in weapon_ids]

  con = _get_db_connection()
  
  cur = con.cursor()
  cur.execute(update_char_stmt, (
    user_id,
    name,
    ability_scores["str"],
    ability_scores["dex"],
    ability_scores["con"],
    ability_scores["intl"],
    ability_scores["wis"],
    ability_scores["cha"],
    10 + _get_ability_modifier(ability_scores["dex"]),
    _get_ability_modifier(ability_scores["con"]),
    _get_ability_modifier(ability_scores["con"]),
    notes,
    char_id
  ))
  cur.executemany(insert_char_weps_stmt, character_weapons_records)

  con.commit()
  con.close()

  return { "new_character_id": char_id }

def get_user_characters(user_id: int):
  char_table_joined_query = "SELECT ch.id, ch.class_id, cl.class_name, cl.hit_dice, f.feat_name, f.feat_desc, ch.character_name, ch.lvl, ch.xp, ch.str, ch.dex, ch.con, ch.intl, ch.wis, ch.cha, ch.armor_class, ch.hp, ch.max_hp, ch.notes, ch.status_effects, ch.lvl_1_spell_slots, ch.lvl_2_spell_slots, ch.lvl_3_spell_slots, ch.lvl_4_spell_slots, ch.proficiency_bonus, ch.speed, ch.rages, ch.rage_damage, ch.second_wind, ch.martial_arts, ch.sneak_attack FROM characters AS ch INNER JOIN classes AS cl ON ch.class_id = cl.id INNER JOIN feats AS f ON cl.feat_id = f.id WHERE ch.user_id = ?"

  con = _get_db_connection()

  cur = con.cursor()
  cur.execute(char_table_joined_query, (user_id,))
  raw_char_records: list[list] = cur.fetchall()

  formatted_records = []
  for raw_char_record in raw_char_records:
    char_record = {
      "id": raw_char_record[0],
      "class_id": raw_char_record[1],
      "class_name": raw_char_record[2],
      "hit_dice": raw_char_record[3],
      "feat_name": raw_char_record[4],
      "feat_desc": raw_char_record[5],
      "character_name": raw_char_record[6],
      "lvl": raw_char_record[7],
      "xp": raw_char_record[8],
      "str": raw_char_record[9],
      "dex": raw_char_record[10],
      "con": raw_char_record[11],
      "intl": raw_char_record[12],
      "wis": raw_char_record[13],
      "cha": raw_char_record[14],
      "armor_class": raw_char_record[15],
      "hp": raw_char_record[16],
      "max_hp": raw_char_record[17],
      "notes": raw_char_record[18],
      "status_effects": raw_char_record[19],
      "lvl_1_spell_slots": raw_char_record[20],
      "lvl_2_spell_slots": raw_char_record[21],
      "lvl_3_spell_slots": raw_char_record[22],
      "lvl_4_spell_slots": raw_char_record[23],
      "proficiency_bonus": raw_char_record[24],
      "speed": raw_char_record[25],
      "rages": raw_char_record[26],
      "rage_damage": raw_char_record[27],
      "second_wind": raw_char_record[28],
      "martial_arts": raw_char_record[29],
      "sneak_attack": raw_char_record[30],
      "saves": [],
      "skills": [],
      "spells": [],
      "weapons": [],
      "items": []
    }

    char_id = raw_char_record[0]
    class_id = raw_char_record[1]
    _assign_class_saves(cur, class_id, char_record)
    _assign_class_skills(cur, class_id, char_record)
    char_record["spells"] = get_spells_by_class(class_id)["spells"]
    char_record["weapons"] = get_character_weapons(char_id)["weapons"]
    char_record["items"] = get_character_items(char_id)["items"]

    formatted_records.append(char_record)

  con.close()

  return { "characters": formatted_records }

def update_character(id: int, xp: int, notes: str, hp: int):
  update_query = "UPDATE characters SET xp = ?, notes = ?, hp = ? WHERE id = ?"

  con = _get_db_connection()

  cur = con.cursor()
  cur.execute(update_query, (xp, notes, hp, id))
  con.commit()

  con.close()

  return { "updated_character_id": id }

def unlink_character_from_user(char_id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE characters SET user_id = 'null' WHERE id = ?", (char_id,))
  con.commit()

  con.close()

  return { "unlinked_character_id": char_id }

def get_skills():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT skill_name, ability_name FROM skills")
  skills_records: list[list] = cur.fetchall()

  con.close()

  formatted_records = []
  for skill_record in skills_records:
    formatted_records.append({
      "skill_name": skill_record[0],
      "ability_name": skill_record[1]
    })
  
  return { "skills": formatted_records }

def get_class_level_stats(lvl: int, class_id: int):
  query = "SELECT proficiency_bonus, rages, rage_damage, lvl_1_spell_slots, lvl_2_spell_slots, lvl_3_spell_slots, lvl_4_spell_slots, second_wind, martial_arts, sneak_attack FROM class_levels WHERE lvl = ? AND class_id = ?"

  con = _get_db_connection()

  cur = con.cursor()
  cur.execute(query, (lvl, class_id))
  record: list = cur.fetchone()

  con.close()

  return {
    "proficiency_bonus": record[0],
    "rages": record[1],
    "rage_damage": record[2],
    "lvl_1_spell_slots": record[3],
    "lvl_2_spell_slots": record[4],
    "lvl_3_spell_slots": record[5],
    "lvl_4_spell_slots": record[6],
    "second_wind": record[7],
    "martial_arts": record[8],
    "sneak_attack": record[9]
  }

def level_up_character(char_id: int, next_lvl: int, class_id: int, abilities_to_upgrade: str, num_abilities_to_upgrade: int, hit_die: str, con_score: int):
  initial_update_stmt = "UPDATE characters SET lvl = ?, proficiency_bonus = ?, rages = ?, rage_damage = ?, lvl_1_spell_slots = ?, lvl_2_spell_slots = ?, lvl_3_spell_slots = ?, lvl_4_spell_slots = ?, second_wind = ?, martial_arts = ?, sneak_attack = ? WHERE id = ?"
  new_stats = get_class_level_stats(next_lvl, class_id)
  initial_con_mod = _get_ability_modifier(con_score)
  new_con_score = con_score
  new_con_mod = _get_ability_modifier(new_con_score)

  con = _get_db_connection()
  cur = con.cursor()
  
  cur.execute(initial_update_stmt, (
    next_lvl,
    new_stats["proficiency_bonus"],
    new_stats["rages"],
    new_stats["rage_damage"],
    new_stats["lvl_1_spell_slots"],
    new_stats["lvl_2_spell_slots"],
    new_stats["lvl_3_spell_slots"],
    new_stats["lvl_4_spell_slots"],
    new_stats["second_wind"],
    new_stats["martial_arts"],
    new_stats["sneak_attack"],
    char_id
  ))

  if abilities_to_upgrade.find("str") != -1:
    cur.execute("UPDATE characters SET str = str + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  if abilities_to_upgrade.find("dex") != -1:
    cur.execute("UPDATE characters SET dex = dex + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  if abilities_to_upgrade.find("con") != -1:
    new_con_score += 1 if num_abilities_to_upgrade == 2 else 2
    new_con_mod = _get_ability_modifier(new_con_score)
    cur.execute("UPDATE characters SET con = con + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  if abilities_to_upgrade.find("intl") != -1:
    cur.execute("UPDATE characters SET intl = intl + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  if abilities_to_upgrade.find("wis") != -1:
    cur.execute("UPDATE characters SET wis = wis + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  if abilities_to_upgrade.find("cha") != -1:
    cur.execute("UPDATE characters SET cha = cha + ? WHERE id = ?", (
      1 if num_abilities_to_upgrade == 2 else 2,
      char_id
    ))
  
  health_upgrade_stmt = "UPDATE characters SET max_hp = max_hp + ? WHERE id = ?"
  avg_hit_die_roll = _get_avg_die_roll(hit_die)
  cur.execute(health_upgrade_stmt, (avg_hit_die_roll + new_con_mod, char_id))

  if new_con_mod - initial_con_mod >= 1:
    cur.execute(health_upgrade_stmt, (next_lvl, char_id))

  con.commit()
  con.close()

  return { "leveled_up_character": char_id }
