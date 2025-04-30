# Script for inserting classes into the database.
# Relevant table schema below.

# CREATE TABLE classes (
#   id INTEGER PRIMARY KEY,
#   class_name TEXT,
#   class_desc TEXT,
#   hit_dice TEXT,
#   feat TEXT
# );
# CREATE TABLE class_saving_throw_proficiencies (
#   class_id INTEGER REFERENCES classes,
#   saving_throw_id INTEGER REFERENCES saving_throws,
#   PRIMARY KEY (class_id, saving_throw_id)
# );
# CREATE TABLE class_skill_proficiencies (
#   class_id INTEGER REFERENCES classes,
#   skill_id INTEGER REFERENCES skills,
#   PRIMARY KEY (class_id, skill_id)
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

save_ids = {
  "str": 1,
  "dex": 2,
  "con": 3,
  "intl": 4,
  "wis": 5,
  "cha": 6
}

skill_ids = {
  "Acrobatics": 1,
  "Arcana": 2,
  "History": 3,
  "Nature": 4,
  "Religion": 5,
  "Performance": 6,
  "Animal Handling": 7,
  "Athletics": 8,
  "Deception": 9,
  "Insight": 10,
  "Intimidation": 11,
  "Investigation": 12,
  "Medicine": 13,
  "Perception": 14,
  "Persuasion": 15,
  "Sleight of Hand": 16,
  "Stealth": 17,
  "Survival": 18
}

class_records = [
  (class_ids["Barbarian"], "Barbarian", "A fierce warrior of primal rage.", "d12", "Rage"),
  (class_ids["Bard"], "Bard", "An inspiring performer of music, dance, and magic.", "d8", "Spellcasting"),
  (class_ids["Cleric"], "Cleric", "A miraculous priest of divine power.", "d8", "Spellcasting"),
  (class_ids["Druid"], "Druid", "A nature priest of primal power.", "d8", "Spellcasting"),
  (class_ids["Fighter"], "Fighter", "A master of all arms and armor.", "d10", "Second Wind"),
  (class_ids["Monk"], "Monk", "A martial artist of supernatural focus.", "d8", "Martial Arts"),
  (class_ids["Paladin"], "Paladin", "A devout warrior of sacred oaths.", "d10", "Spellcasting"),
  (class_ids["Ranger"], "Ranger", "A wandering warrior imbued with primal magic.", "d10", "Spellcasting"),
  (class_ids["Rogue"], "Rogue", "A dexterous expert in stealth and subterfuge.", "d8", "Sneak Attack"),
  (class_ids["Sorcerer"], "Sorcerer", "A dazzling mage filled with innate magic.", "d6", "Spellcasting"),
  (class_ids["Warlock"], "Warlock", "An occultist empowered by otherworldly pacts." "d8", "Gaze of Two Minds"),
  (class_ids["Wizard"], "Wizard", "A scholarly magic-user of arcane power.", "d6", "Spellcasting")
]

class_save_proficiencies_records = [
  (class_ids["Barbarian"], save_ids["str"]),
  (class_ids["Barbarian"], save_ids["con"]),
  (class_ids["Bard"], save_ids["dex"]),
  (class_ids["Bard"], save_ids["cha"]),
  (class_ids["Cleric"], save_ids["cha"]),
  (class_ids["Cleric"], save_ids["wis"]),
  (class_ids["Druid"], save_ids["intl"]),
  (class_ids["Druid"], save_ids["wis"]),
  (class_ids["Fighter"], save_ids["str"]),
  (class_ids["Fighter"], save_ids["con"]),
  (class_ids["Monk"], save_ids["str"]),
  (class_ids["Monk"], save_ids["dex"]),
  (class_ids["Paladin"], save_ids["wis"]),
  (class_ids["Paladin"], save_ids["cha"]),
  (class_ids["Ranger"], save_ids["str"]),
  (class_ids["Ranger"], save_ids["dex"]),
  (class_ids["Rogue"], save_ids["dex"]),
  (class_ids["Rogue"], save_ids["intl"]),
  (class_ids["Sorcerer"], save_ids["con"]),
  (class_ids["Sorcerer"], save_ids["cha"]),
  (class_ids["Warlock"], save_ids["wis"]),
  (class_ids["Warlock"], save_ids["cha"]),
  (class_ids["Wizard"], save_ids["intl"]),
  (class_ids["Wizard"], save_ids["wis"])
]

class_skill_proficiencies_records = [
  (class_ids["Barbarian"], skill_ids["Intimidation"]),
  (class_ids["Barbarian"], skill_ids["Athletics"]),
  (class_ids["Bard"], skill_ids["Persuasion"]),
  (class_ids["Bard"], skill_ids["Performance"]),
  (class_ids["Bard"], skill_ids["Insight"]),
  (class_ids["Cleric"], skill_ids["History"]),
  (class_ids["Cleric"], skill_ids["Religion"]),
  (class_ids["Druid"], skill_ids["Arcana"]),
  (class_ids["Druid"], skill_ids["Nature"]),
  (class_ids["Fighter"], skill_ids["Acrobatics"]),
  (class_ids["Fighter"], skill_ids["Survival"]),
  (class_ids["Monk"], skill_ids["Religion"]),
  (class_ids["Monk"], skill_ids["Stealth"]),
  (class_ids["Paladin"], skill_ids["Medicine"]),
  (class_ids["Paladin"], skill_ids["Intimidation"]),
  (class_ids["Ranger"], skill_ids["Perception"]),
  (class_ids["Ranger"], skill_ids["Investigation"]),
  (class_ids["Ranger"], skill_ids["Animal Handling"]),
  (class_ids["Rogue"], skill_ids["Deception"]),
  (class_ids["Rogue"], skill_ids["Persuasion"]),
  (class_ids["Rogue"], skill_ids["Sleight of Hand"]),
  (class_ids["Rogue"], skill_ids["Stealth"]),
  (class_ids["Sorcerer"], skill_ids["Arcana"]),
  (class_ids["Sorcerer"], skill_ids["Insight"]),
  (class_ids["Warlock"], skill_ids["Nature"]),
  (class_ids["Warlock"], skill_ids["History"]),
  (class_ids["Wizard"], skill_ids["Investigation"]),
  (class_ids["Wizard"], skill_ids["Medicine"])
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

cur.executemany("INSERT INTO classes VALUES (?, ?, ?, ?, ?)", class_records)
cur.executemany("INSERT INTO class_saving_throw_proficiencies VALUES (?, ?)", class_save_proficiencies_records)
cur.executemany("INSERT INTO class_skill_proficiencies VALUES (?, ?)", class_skill_proficiencies_records)
con.commit()

con.close()
