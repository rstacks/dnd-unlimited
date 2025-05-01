# https://www.dndbeyond.com/classes/2190875-barbarian
# https://www.dndbeyond.com/classes/2190879-fighter
# https://www.dndbeyond.com/classes/2190880-monk
# https://www.dndbeyond.com/classes/2190883-rogue
# Script for inserting non-spellcaster feats into the database.
# Relevant table schema below.

# CREATE TABLE feats (
#   id INTEGER PRIMARY KEY,
#   class_id INTEGER REFERENCES classes,
#   feat_name TEXT,
#   feat_desc TEXT
# );

import sqlite3

DB_CONNECTION_STR = "../dnd-db.db"

nonspellcaster_class_ids = {
  "Barbarian": 1,
  "Fighter": 5,
  "Monk": 6,
  "Rogue": 9,
}

# Tuple schema: class_id, feat_name, feat_desc
feat_records = [
  (nonspellcaster_class_ids["Barbarian"], ""),
  (),
  (),
  ()
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

con.commit()

con.close()
