DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS spells;
DROP TABLE IF EXISTS weapons;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS saving_throws;
DROP TABLE IF EXISTS skills;
DROP TABLE IF EXISTS class_saving_throw_proficiencies;
DROP TABLE IF EXISTS class_skill_proficiencies;
DROP TABLE IF EXISTS character_spells;
DROP TABLE IF EXISTS character_weapons;

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
CREATE TABLE character_spells (
  character_id INTEGER REFERENCES characters,
  spell_id INTEGER REFERENCES spells,
  PRIMARY KEY (character_id, spell_id)
);
CREATE TABLE character_weapons (
  character_id INTEGER REFERENCES characters,
  weapon_id INTEGER REFERENCES spells,
  PRIMARY KEY (character_id, weapon_id)
);

BEGIN;

INSERT INTO spells (spell_name, spell_desc) VALUES
  (
    'Fire Bolt',
    'On hit, target takes 1d6 damage. Target must succeed
    with a CON saving throw at the start of the round for flames to
    douse; otherwise, they continue taking 1d6 damage.'
  ),
  (
    'Command',
    'Target must succeed with a WIS saving throw; otherwise, they
    will carry out any one-word command that does not directly harm them.'
  ),
  (
    'Cure Wounds',
    'Target gains HP equivalent to 1d6 + your spell attack modifier.'
  ),
  (
    'Bless',
    'User and all allies can add 1d4 to damage rolls or saving throws while
    user is concentrating. If user takes damage, make a CON saving throw vs.
    half of incoming damage; upon failure, concentration breaks and spell
    effects end.'
  );

COMMIT;
