DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS saving_throws;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS class_saving_throw_proficiencies;
DROP TABLE IF EXISTS class_skill_proficiencies;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  phone TEXT,
  user_type TEXT,
  user_name TEXT
);
CREATE TABLE spells (
  id INTEGER PRIMARY KEY,
  spell_name TEXT,
  spell_desc TEXT
);
CREATE TABLE weapons (
  id INTEGER PRIMARY KEY,
  weapon_name TEXT,
  weapon_type TEXT,
  weapon_desc TEXT
);
CREATE TABLE classes (
  id INTEGER PRIMARY KEY,
  class_name TEXT,
  class_desc TEXT,
  speed INTEGER,
  proficiency_bonus INTEGER,
  hit_dice TEXT,
  armor_class_type TEXT
);
CREATE TABLE characters (
  id INTEGER PRIMARY KEY,
  user_id INTEGER REFERENCES users,
  class_id INTEGER REFERENCES classes,
  character_name TEXT,
  lvl TEXT,
  xp INTEGER,
  str INTEGER,
  dex INTEGER,
  con INTEGER,
  intl INTEGER,
  wis INTEGER,
  cha INTEGER,
  armor_class INTEGER,
  hp INTEGER,
  max_hp INTEGER,
  notes TEXT
);
CREATE TABLE saving_throws (
  id INTEGER PRIMARY KEY,
  st_name TEXT
);
CREATE TABLE skills (
  id INTEGER PRIMARY KEY,
  skill_name TEXT,
  ability_name TEXT
);
CREATE TABLE class_saving_throw_proficiencies (
  class_id INTEGER REFERENCES classes,
  saving_throw_id INTEGER REFERENCES saving_throws,
  PRIMARY KEY (class_id, saving_throw_id)
);
CREATE TABLE class_skill_proficiencies (
  class_id INTEGER REFERENCES classes,
  skill_id INTEGER REFERENCES skills,
  PRIMARY KEY (class_id, skill_id)
);
