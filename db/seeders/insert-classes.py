# Script for inserting classes into the database.
# Relevant table schema below.

# CREATE TABLE classes (
#   id INTEGER PRIMARY KEY,
#   class_name TEXT,
#   class_desc TEXT,
#   hit_dice TEXT
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

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

class_records = [
  (),
]

con.commit()
con.close()
