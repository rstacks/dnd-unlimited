# https://www.dndbeyond.com/classes/2190875-barbarian
# https://www.dndbeyond.com/classes/2190879-fighter
# https://www.dndbeyond.com/classes/2190880-monk
# https://www.dndbeyond.com/classes/2190883-rogue
# https://www.dndbeyond.com/spells
# Script for inserting feats into the database.
# Relevant table schema below.

# CREATE TABLE feats (
#   id INTEGER PRIMARY KEY,
#   feat_name TEXT,
#   feat_desc TEXT
# );

import sqlite3

DB_CONNECTION_STR = "../dnd-db.db"

# Tuple schema: feat_name, feat_desc
feat_records = [
  ("Spellcasting", ""),
  ("Rage", "You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.\nWhile active, your Rage follows the rules below.\nRage Damage: When you make an attack using Strength (with either a weapon or an Unarmed Strike) and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian.\nStrength Advantage: You have Advantage on Strength checks and Strength saving throws.\nDuration: The Rage lasts until the end of your next turn, and it ends early if you don Heavy armor or have the Incapacitated condition. If your Rage is still active on your next turn, you can extend the Rage for another round by doing one of the following:\n- Make an attack roll against an enemy.\n- Force an enemy to make a saving throw.\n- Take a Bonus Action (if available) to extend your Rage.\nEach time the Rage is extended, it lasts until the end of your next turn."),
  ("Second Wind", ""),
  ("Martial Arts"),
  ("Sneak Attack")
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

con.commit()

con.close()
