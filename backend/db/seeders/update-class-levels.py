# https://www.dndbeyond.com/classes
# Script for finalizing class_level records for each class in the database.
# Relevant table schema below.

# CREATE TABLE class_levels (
#   lvl INTEGER,
#   class_id INTEGER REFERENCES classes,
#   proficiency_bonus INTEGER,
#   rages INTEGER,
#   rage_damage INTEGER,
#   lvl_1_spell_slots INTEGER,
#   lvl_2_spell_slots INTEGER,
#   lvl_3_spell_slots INTEGER,
#   lvl_4_spell_slots INTEGER,
#   second_wind INTEGER,
#   martial_arts TEXT,
#   sneak_attack TEXT,
#   PRIMARY KEY (lvl, class_id)
# );

import sqlite3

DB_CONNECTION_STR = "../dnd-db.db"

class_ids = {
  "Barbarian": 1,
  "Bard": 2,
  "Cleric": 3,
  "Druid": 4,
  "Fighter": 5,
  "Monk": 6,
  "Paladin": 7,
  "Ranger": 8,
  "Rogue": 9,
  "Sorcerer": 10,
  "Warlock": 11,
  "Wizard": 12
}

barbarian_stmt = "UPDATE class_levels SET rages = ?, rage_damage = ? WHERE lvl = ? AND class_id = 1"
barbarian_lvl_stats = [
  (2, 2, 2),
  (3, 2, 3),
  (3, 2, 4),
  (3, 2, 5),
  (4, 2, 6),
  (4, 2, 7),
  (4, 2, 8),
  (4, 3, 9),
  (4, 3, 10),
  (4, 3, 11),
  (5, 3, 12),
  (5, 3, 13),
  (5, 3, 14),
  (5, 3, 15),
  (5, 4, 16),
  (6, 4, 17),
  (6, 4, 18),
  (6, 4, 19),
  (6, 4, 20),
]

big_spellcaster_stmt = "UPDATE class_levels SET lvl_1_spell_slots = ?, lvl_2_spell_slots = ?, lvl_3_spell_slots = ?, lvl_4_spell_slots = ? WHERE lvl = ? AND class_id = ?"
big_spellcaster_lvl_stats = [
  (3, 0, 0, 0, 2, class_ids["Bard"]),
  (4, 2, 0, 0, 3, class_ids["Bard"]),
  (4, 3, 0, 0, 4, class_ids["Bard"]),
  (4, 3, 2, 0, 5, class_ids["Bard"]),
  (4, 3, 3, 0, 6, class_ids["Bard"]),
  (4, 3, 3, 1, 7, class_ids["Bard"]),
  (4, 3, 3, 2, 8, class_ids["Bard"]),
  (4, 3, 3, 3, 9, class_ids["Bard"]),
  (4, 3, 3, 3, 10, class_ids["Bard"]),
  (5, 3, 3, 3, 11, class_ids["Bard"]),
  (5, 3, 3, 3, 12, class_ids["Bard"]),
  (5, 4, 3, 3, 13, class_ids["Bard"]),
  (5, 4, 3, 3, 14, class_ids["Bard"]),
  (5, 4, 4, 3, 15, class_ids["Bard"]),
  (5, 4, 4, 3, 16, class_ids["Bard"]),
  (5, 4, 4, 4, 17, class_ids["Bard"]),
  (5, 4, 4, 4, 18, class_ids["Bard"]),
  (5, 4, 4, 4, 19, class_ids["Bard"]),
  (5, 4, 4, 4, 20, class_ids["Bard"]),

  (3, 0, 0, 0, 2, class_ids["Cleric"]),
  (4, 2, 0, 0, 3, class_ids["Cleric"]),
  (4, 3, 0, 0, 4, class_ids["Cleric"]),
  (4, 3, 2, 0, 5, class_ids["Cleric"]),
  (4, 3, 3, 0, 6, class_ids["Cleric"]),
  (4, 3, 3, 1, 7, class_ids["Cleric"]),
  (4, 3, 3, 2, 8, class_ids["Cleric"]),
  (4, 3, 3, 3, 9, class_ids["Cleric"]),
  (4, 3, 3, 3, 10, class_ids["Cleric"]),
  (5, 3, 3, 3, 11, class_ids["Cleric"]),
  (5, 3, 3, 3, 12, class_ids["Cleric"]),
  (5, 4, 3, 3, 13, class_ids["Cleric"]),
  (5, 4, 3, 3, 14, class_ids["Cleric"]),
  (5, 4, 4, 3, 15, class_ids["Cleric"]),
  (5, 4, 4, 3, 16, class_ids["Cleric"]),
  (5, 4, 4, 4, 17, class_ids["Cleric"]),
  (5, 4, 4, 4, 18, class_ids["Cleric"]),
  (5, 4, 4, 4, 19, class_ids["Cleric"]),
  (5, 4, 4, 4, 20, class_ids["Cleric"]),

  (3, 0, 0, 0, 2, class_ids["Druid"]),
  (4, 2, 0, 0, 3, class_ids["Druid"]),
  (4, 3, 0, 0, 4, class_ids["Druid"]),
  (4, 3, 2, 0, 5, class_ids["Druid"]),
  (4, 3, 3, 0, 6, class_ids["Druid"]),
  (4, 3, 3, 1, 7, class_ids["Druid"]),
  (4, 3, 3, 2, 8, class_ids["Druid"]),
  (4, 3, 3, 3, 9, class_ids["Druid"]),
  (4, 3, 3, 3, 10, class_ids["Druid"]),
  (5, 3, 3, 3, 11, class_ids["Druid"]),
  (5, 3, 3, 3, 12, class_ids["Druid"]),
  (5, 4, 3, 3, 13, class_ids["Druid"]),
  (5, 4, 3, 3, 14, class_ids["Druid"]),
  (5, 4, 4, 3, 15, class_ids["Druid"]),
  (5, 4, 4, 3, 16, class_ids["Druid"]),
  (5, 4, 4, 4, 17, class_ids["Druid"]),
  (5, 4, 4, 4, 18, class_ids["Druid"]),
  (5, 4, 4, 4, 19, class_ids["Druid"]),
  (5, 4, 4, 4, 20, class_ids["Druid"]),

  (3, 0, 0, 0, 2, class_ids["Sorcerer"]),
  (4, 2, 0, 0, 3, class_ids["Sorcerer"]),
  (4, 3, 0, 0, 4, class_ids["Sorcerer"]),
  (4, 3, 2, 0, 5, class_ids["Sorcerer"]),
  (4, 3, 3, 0, 6, class_ids["Sorcerer"]),
  (4, 3, 3, 1, 7, class_ids["Sorcerer"]),
  (4, 3, 3, 2, 8, class_ids["Sorcerer"]),
  (4, 3, 3, 3, 9, class_ids["Sorcerer"]),
  (4, 3, 3, 3, 10, class_ids["Sorcerer"]),
  (5, 3, 3, 3, 11, class_ids["Sorcerer"]),
  (5, 3, 3, 3, 12, class_ids["Sorcerer"]),
  (5, 4, 3, 3, 13, class_ids["Sorcerer"]),
  (5, 4, 3, 3, 14, class_ids["Sorcerer"]),
  (5, 4, 4, 3, 15, class_ids["Sorcerer"]),
  (5, 4, 4, 3, 16, class_ids["Sorcerer"]),
  (5, 4, 4, 4, 17, class_ids["Sorcerer"]),
  (5, 4, 4, 4, 18, class_ids["Sorcerer"]),
  (5, 4, 4, 4, 19, class_ids["Sorcerer"]),
  (5, 4, 4, 4, 20, class_ids["Sorcerer"]),

  (3, 0, 0, 0, 2, class_ids["Wizard"]),
  (4, 2, 0, 0, 3, class_ids["Wizard"]),
  (4, 3, 0, 0, 4, class_ids["Wizard"]),
  (4, 3, 2, 0, 5, class_ids["Wizard"]),
  (4, 3, 3, 0, 6, class_ids["Wizard"]),
  (4, 3, 3, 1, 7, class_ids["Wizard"]),
  (4, 3, 3, 2, 8, class_ids["Wizard"]),
  (4, 3, 3, 3, 9, class_ids["Wizard"]),
  (4, 3, 3, 3, 10, class_ids["Wizard"]),
  (5, 3, 3, 3, 11, class_ids["Wizard"]),
  (5, 3, 3, 3, 12, class_ids["Wizard"]),
  (5, 4, 3, 3, 13, class_ids["Wizard"]),
  (5, 4, 3, 3, 14, class_ids["Wizard"]),
  (5, 4, 4, 3, 15, class_ids["Wizard"]),
  (5, 4, 4, 3, 16, class_ids["Wizard"]),
  (5, 4, 4, 4, 17, class_ids["Wizard"]),
  (5, 4, 4, 4, 18, class_ids["Wizard"]),
  (5, 4, 4, 4, 19, class_ids["Wizard"]),
  (5, 4, 4, 4, 20, class_ids["Wizard"])
]

small_spellcaster_stmt = "UPDATE class_levels SET lvl_1_spell_slots = ?, lvl_2_spell_slots = ?, lvl_3_spell_slots = ?, lvl_4_spell_slots = ? WHERE lvl = ? AND class_id = ?"
small_spellcaster_lvl_stats = [
  (2, 0, 0, 0, 2, class_ids["Paladin"]),
  (3, 0, 0, 0, 3, class_ids["Paladin"]),
  (3, 0, 0, 0, 4, class_ids["Paladin"]),
  (4, 2, 0, 0, 5, class_ids["Paladin"]),
  (4, 2, 0, 0, 6, class_ids["Paladin"]),
  (4, 3, 0, 0, 7, class_ids["Paladin"]),
  (4, 3, 0, 0, 8, class_ids["Paladin"]),
  (4, 3, 2, 0, 9, class_ids["Paladin"]),
  (4, 3, 2, 0, 10, class_ids["Paladin"]),
  (4, 3, 3, 0, 11, class_ids["Paladin"]),
  (4, 3, 3, 0, 12, class_ids["Paladin"]),
  (4, 3, 3, 1, 13, class_ids["Paladin"]),
  (4, 3, 3, 1, 14, class_ids["Paladin"]),
  (4, 3, 3, 2, 15, class_ids["Paladin"]),
  (4, 3, 3, 2, 16, class_ids["Paladin"]),
  (4, 3, 3, 3, 17, class_ids["Paladin"]),
  (4, 3, 3, 3, 18, class_ids["Paladin"]),
  (4, 3, 3, 3, 19, class_ids["Paladin"]),
  (4, 3, 3, 3, 20, class_ids["Paladin"]),

  (2, 0, 0, 0, 2, class_ids["Ranger"]),
  (3, 0, 0, 0, 3, class_ids["Ranger"]),
  (3, 0, 0, 0, 4, class_ids["Ranger"]),
  (4, 2, 0, 0, 5, class_ids["Ranger"]),
  (4, 2, 0, 0, 6, class_ids["Ranger"]),
  (4, 3, 0, 0, 7, class_ids["Ranger"]),
  (4, 3, 0, 0, 8, class_ids["Ranger"]),
  (4, 3, 2, 0, 9, class_ids["Ranger"]),
  (4, 3, 2, 0, 10, class_ids["Ranger"]),
  (4, 3, 3, 0, 11, class_ids["Ranger"]),
  (4, 3, 3, 0, 12, class_ids["Ranger"]),
  (4, 3, 3, 1, 13, class_ids["Ranger"]),
  (4, 3, 3, 1, 14, class_ids["Ranger"]),
  (4, 3, 3, 2, 15, class_ids["Ranger"]),
  (4, 3, 3, 2, 16, class_ids["Ranger"]),
  (4, 3, 3, 3, 17, class_ids["Ranger"]),
  (4, 3, 3, 3, 18, class_ids["Ranger"]),
  (4, 3, 3, 3, 19, class_ids["Ranger"]),
  (4, 3, 3, 3, 20, class_ids["Ranger"])
]

warlock_stmt = "UPDATE class_levels SET lvl_1_spell_slots = ?, lvl_2_spell_slots = ?, lvl_3_spell_slots = ?, lvl_4_spell_slots = ? WHERE lvl = ? AND class_id = 11"
warlock_lvl_stats = [
  (2, 0, 0, 0, 2),
  (0, 2, 0, 0, 3),
  (0, 2, 0, 0, 4),
  (0, 0, 2, 0, 5),
  (0, 0, 2, 0, 6),
  (0, 0, 0, 2, 7),
  (0, 0, 0, 2, 8),
  (0, 0, 0, 2, 9),
  (0, 0, 0, 2, 10),
  (0, 0, 0, 3, 11),
  (0, 0, 0, 3, 12),
  (0, 0, 0, 3, 13),
  (0, 0, 0, 3, 14),
  (0, 0, 0, 3, 15),
  (0, 0, 0, 3, 16),
  (0, 0, 0, 4, 17),
  (0, 0, 0, 4, 18),
  (0, 0, 0, 4, 19),
  (0, 0, 0, 4, 20),
]

fighter_stmt = "UPDATE class_levels SET second_wind = ? WHERE lvl = ? AND class_id = 5"
fighter_lvl_stats = [
  (2, 2),
  (2, 3),
  (3, 4),
  (3, 5),
  (3, 6),
  (3, 7),
  (3, 8),
  (3, 9),
  (4, 10),
  (4, 11),
  (4, 12),
  (4, 13),
  (4, 14),
  (4, 15),
  (4, 16),
  (4, 17),
  (4, 18),
  (4, 19),
  (4, 20)
]

monk_stmt = "UPDATE class_levels SET martial_arts = ? WHERE lvl = ? AND class_id = 6"
monk_lvl_stats = [
  ("1d6", 2),
  ("1d6", 3),
  ("1d6", 4),
  ("1d8", 5),
  ("1d8", 6),
  ("1d8", 7),
  ("1d8", 8),
  ("1d8", 9),
  ("1d8", 10),
  ("1d10", 11),
  ("1d10", 12),
  ("1d10", 13),
  ("1d10", 14),
  ("1d10", 15),
  ("1d10", 16),
  ("1d12", 17),
  ("1d12", 18),
  ("1d12", 19),
  ("1d12", 20),
]

rogue_stmt = "UPDATE class_levels SET sneak_attack = ? WHERE lvl = ? AND class_id = 9"
rogue_lvl_stats = [
  ("1d6", 2),
  ("2d6", 3),
  ("2d6", 4),
  ("3d6", 5),
  ("3d6", 6),
  ("4d6", 7),
  ("4d6", 8),
  ("5d6", 9),
  ("5d6", 10),
  ("6d6", 11),
  ("6d6", 12),
  ("7d6", 13),
  ("7d6", 14),
  ("8d6", 15),
  ("8d6", 16),
  ("9d6", 17),
  ("9d6", 18),
  ("10d6", 19),
  ("10d6", 20),
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

cur.executemany(barbarian_stmt, barbarian_lvl_stats)
cur.executemany(big_spellcaster_stmt, big_spellcaster_lvl_stats)
cur.executemany(small_spellcaster_stmt, small_spellcaster_lvl_stats)
cur.executemany(warlock_stmt, warlock_lvl_stats)
cur.executemany(fighter_stmt, fighter_lvl_stats)
cur.executemany(monk_stmt, monk_lvl_stats)
cur.executemany(rogue_stmt, rogue_lvl_stats)
con.commit()

con.close()
