DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS saving_throws;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS class_saving_throw_proficiencies;
DROP TABLE IF EXISTS class_skill_proficiencies;
DROP TABLE IF EXISTS character_spells;
DROP TABLE IF EXISTS character_weapons;
DROP TABLE IF EXISTS character_items;

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  phone TEXT,
  user_type TEXT,
  user_name TEXT
);
CREATE TABLE weapons (
  id INTEGER PRIMARY KEY,
  weapon_name TEXT,
  weapon_type TEXT,
  weapon_desc TEXT
);
CREATE TABLE items (
  id INTEGER PRIMARY KEY,
  item_name TEXT,
  item_desc TEXT
);
CREATE TABLE classes (
  id INTEGER PRIMARY KEY,
  class_name TEXT,
  class_desc TEXT,
  hit_dice TEXT
);
CREATE TABLE spells (
  id INTEGER PRIMARY KEY,
  class_id INTEGER REFERENCES classes,
  spell_name TEXT,
  spell_desc TEXT
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
  notes TEXT,
  status_effects TEXT,
  img_path TEXT
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
CREATE TABLE character_spells (
  character_id INTEGER REFERENCES characters,
  spell_id INTEGER REFERENCES spells,
  PRIMARY KEY (character_id, spell_id)
);
CREATE TABLE character_weapons (
  character_id INTEGER REFERENCES characters,
  weapon_id INTEGER REFERENCES spells,
  damage_die TEXT,
  PRIMARY KEY (character_id, weapon_id)
);
CREATE TABLE character_items (
  character_id INTEGER REFERENCES characters,
  item_id INTEGER REFERENCES items,
  amount INTEGER,
  PRIMARY KEY (character_id, item_id)
);

BEGIN;

INSERT INTO saving_throws (st_name) VALUES
  ('str'),
  ('dex'),
  ('con'),
  ('intl'),
  ('wis'),
  ('cha');
INSERT INTO skills (skill_name, ability_name) VALUES
  ('Acrobatics', 'dex'),
  ('Arcana', 'intl'),
  ('History', 'intl'),
  ('Nature', 'intl'),
  ('Religion', 'intl'),
  ('Performance', 'cha'),
  ('Animal Handling', 'wis'),
  ('Athletics', 'str'),
  ('Deception', 'cha'),
  ('Insight', 'wis'),
  ('Intimidation', 'cha'),
  ('Investigation', 'intl'),
  ('Medicine', 'wis'),
  ('Perception', 'wis'),
  ('Persuasion', 'cha'),
  ('Sleight of Hand', 'dex'),
  ('Stealth', 'dex'),
  ('Survival', 'wis');

COMMIT;
