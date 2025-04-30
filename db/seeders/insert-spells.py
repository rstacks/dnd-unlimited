# https://www.dndbeyond.com/spells
# Script for inserting spells into the database.
# Relevant table schema below.

# CREATE TABLE spells (
#   id INTEGER PRIMARY KEY,
#   class_id INTEGER REFERENCES classes,
#   spell_name TEXT,
#   spell_desc TEXT,
#   spell_type TEXT
# );

import sqlite3

DB_CONNECTION_STR = "../dnd-db.db"

spellcaster_class_ids = {
  "Bard": 2,
  "Cleric": 3,
  "Druid": 4,
  "Paladin": 7,
  "Ranger": 8,
  "Sorcerer": 10,
  "Wizard": 12
}

# Tuple schema: class_id, spell_type, spell_name, spell_desc
spell_records = [
  (spellcaster_class_ids["Bard"], "cantrip", "Vicious Mockery", "You unleash a string of insults laced with subtle enchantments at one creature you can see or hear within range. The target must succeed on a Wisdown saving throw or take 1d6 damage and have Disadvantage on the next attack roll it makes before the end of its next turn."),
  (spellcaster_class_ids["Bard"], "cantrip", "Mage Hand", "A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration. The hand vanishes if it is ever more than 30 feet away from you or if you cast this spell again. When you cast the spell, you can use the hand to manipulate an object, open an unlocked door or container, stow or retrieve an item from an open container, or pour the contents out of a vial. As an action on your later turns, you can control the hand thus again. As part of that action, you can move the hand up to 30 feet. The hand can't attack, activate magic items, or carry more than 10 pounds."),
  (spellcaster_class_ids["Bard"], "casted", "Animal Friendship", "Target a Beast that you can see within range. The target must succeed on a Wisdom saving throw or have the Charmed condition for the duration. If you or one of your allies deals damage to the target, the spell ends. You can target one additional Beast for each spell slot level above 1."),
  (spellcaster_class_ids["Bard"], "casted", "Command", "You speak a one-word command to a creature you can see within range. The target must succeed on a Wisdom saving throw or follow the command on its next turn. You can affect one additional creature for each spell slot level above 1."),
  (spellcaster_class_ids["Bard"], "casted", "Dissonant Whispers", "One creature of your choice that you can see within range hears a discordant melody in its mind. The target makes a Wisdom saving throw. On a failed save, it takes 3d6 damage and must immediately move as far away from you as it can, using the safest route. On a successful save, the target takes half as much damage only. The damage increases by 1d6 for each spell slot level above 1."),
  (spellcaster_class_ids["Bard"], "casted", "Earth Tremor", "You cause a tremor in the ground within range. Each creature other than you in that area must make a Dexterity saving throw. On a failed save, a creature takes 1d6 damage and is knocked prone. When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d6 for each slot above 1st."),
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()


con.commit()

con.close()
