# https://www.dndbeyond.com/classes
# Script for initializing class_level records in the database.
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

def get_proficiency_bonus(lvl: int) -> int:
  if lvl < 5:
    return 2
  if lvl < 9:
    return 3
  if lvl < 13:
    return 4
  if lvl < 17:
    return 5
  return 6

initial_records = []
for lvl in range(1, 20):
  for class_id in range(12):
    initial_records.append((lvl + 1, class_id + 1, get_proficiency_bonus(lvl + 1)))

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

cur.executemany("INSERT INTO class_levels (lvl, class_id, proficiency_bonus) VALUES (?, ?, ?)", initial_records)
con.commit()

con.close()
