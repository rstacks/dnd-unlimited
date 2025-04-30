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

  (spellcaster_class_ids["Cleric"], "cantrip", "Guidance", "You touch a willing creature and choose a skill. Until the spell ends, the creature adds 1d4 to any ability check using the chosen skill."),
  (spellcaster_class_ids["Cleric"], "cantrip", "Thaumaturgy", "You manifest a minor wonder within range. You can create one of the following effects: Altered Eyes, Booming Voice, Fire Play, Invisible Hand, Phantom Sound, or Tremors."),
  (spellcaster_class_ids["Cleric"], "cantrip", "Sacred Flame", "Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 damage. The target gains no benefit from cover for this save."),
  (spellcaster_class_ids["Cleric"], "casted", "Guiding Bolt", "You hurl a bolt of light toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 4d6 damage, and the next attack roll made against it before the end of your next turn has Advantage. The damage increases by 1d6 for each spell slot level above 1."),
  (spellcaster_class_ids["Cleric"], "casted", "Inflict Wounds", "A creature you touch makes a Constitution saving throw, taking 2d10 damage on a failed save or half as much damage on a successful one. The damage increases by 1d10 for each spell slot level above 1."),
  (spellcaster_class_ids["Cleric"], "casted", "Purify Food and Drink", "You remove poison and rot from nonmagical food and drink in a 5-foot-radius."),
  (spellcaster_class_ids["Cleric"], "casted", "Bane", "Up to three creatures of you choice that you can see within range must each make a Charisma saving throw. Whenever a target that fails this save makes an attack roll or a saving throw before the spell ends, the target must subtract 1d4 from the attack roll or save. You can target one additional creature for each spell slot level above 1."),

  (spellcaster_class_ids["Druid"], "cantrip", "Message", "You point toward a creature within range and whisper a message. The target (and only the target) hears the message and can reply in a whisper that only you can hear. You can cast this spell through solid objects if you are familiar with the target and know it is beyond the barrier."),
  (spellcaster_class_ids["Druid"], "cantrip", "Create Bonfire", "You create a bonfire on ground that you can see within range. Until the spell ends, the magic bonfire fills a 5-foot cube. Any creature in the bonfire's space when you cast the spell must succeed on a Dexterity saving throw or take 1d8 damage. A creature must also make the saving throw when it moves into the bonfire's space for the first time on a turn or ends its turn there. The bonfire ignites flammable objects in its area that aren't being worn or carried."),
  (spellcaster_class_ids["Druid"], "casted", "Entangle", "Grasping plants sprout from the ground in a 20-foot square within range. Each creature (other than you) in the area when you cast the spell must succeed on a Strength saving throw or have the Restrained condition until the spell ends. A Restrained creature can take an action to make an Athletics check against your spell save DC. On a success, it frees itself from the grasping plants and is no longer Restrained by them."),
  (spellcaster_class_ids["Druid"], "casted", "Fog Cloud", "You create a 20-foot-radius sphere of fog centered on a point within range. The sphere is heavily obscured. It lasts until a strong wind disperses it. The fog's radius increases by 20 feet for each spell slot level above 1."),
  (spellcaster_class_ids["Druid"], "casted", "Ice Knife", "You create a shard of ice and fling it at one creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 damage. Hit or miss, the shard then explodes. The target and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 2d6 damage. Explosive damage increases by 1d6 for each spell slot level above 1."),
  (spellcaster_class_ids["Druid"], "casted", "Speak with Animals", "You can comprehend and verbally communicate with Beasts, and you can urge them to do something. Most Beasts have little to say about topics that don't pertain to survival or companionship, but at minimum, a Beast can give you information about nearby locations and monsters, including whatever it has perceived within the past day."),

  (spellcaster_class_ids["Paladin"], "casted", "Bless", "You bless up to three creatures within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target adds 1d4 to the attack roll or save. You can target on additional creature for each spell slot level above 1."),
  (spellcaster_class_ids["Paladin"], "casted", "Heroism", "A willing creature you touch is imbued with bravery. Until the spell ends, the creature is immune to the Frightened condition and gains temporary hit points equal to your spellcasting ability modifier at the start of each of its turns. Temporary hit points do not stack. You can target one additional creature for each spell slot level above 1."),

  (spellcaster_class_ids["Ranger"], "casted", "Longstrider", "You touch a creature. The target's Speed increases by 10 feet until the spell ends. You can target one additional creature for each spell slot level above 1."),
  (spellcaster_class_ids["Ranger"], "casted", "Goodberry", "Ten berries appear in your hand and are infused with magic for the duration. A creature can take a Bonus Action to eat one berry. Eating a berry restores 1 Hit Point. Uneaten berries disappear when the spell ends."),

  (spellcaster_class_ids["Sorcerer"], "cantrip", "Chill Touch", "Channeling the chill of the grave, make a melee spell attack against a target within reach. On a hit, the target takes 1d10 damage, and it can't regain Hit Points until the end of your next turn."),
  (spellcaster_class_ids["Sorcerer"], "cantrip", "Frostbite", "You cause numbing frost to form on one creature that you can see within range. The target must make a Constitution saving throw. On a failed save, the target takes 1d6 damage, and it has disadvantage on the next weapon attack roll it makes before the end of its next turn."),
  (spellcaster_class_ids["Sorcerer"], "cantrip", "Sorcerous Burst", "You cast sorcerous energy at one creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d8 damage. If you roll an 8 on a d8 for this spell, you can roll another d8, and add it to the damage. When you cast this spell, the maximum number of these d8s you can add to the spell's damage equals your spellcasting ability modifier."),
  (spellcaster_class_ids["Sorcerer"], "cantrip", "Ray of Frost", "A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 damage, and its Speed is reduced by 10 feet until the start of your next turn."),
  (spellcaster_class_ids["Sorcerer"], "casted", "Sleep", "Each creature of you choice in a 5-foot-radius sphere centered on a point within range must succeed on a Wisdom saving throw or have the Incapacitated condition until the end of its next turn, at which point it must repeat the save. If the target fails the second save, the target has the Unconscious condition for the duration. The spell ends on a target if it takes damage or someone within 5 feet of it takes an action to shake it out of the spell's effect."),
  (spellcaster_class_ids["Sorcerer"], "casted", "Catapult", "Choose one object weighing 1 to 5 pounds within range that isn't being worn or carried. The object flies in a straight line up to 90 feet in a direction you choose before falling to the ground, stopping early if it impacts against a solid surface. If the object would strike a creature, that creature must make a Dexterity saving throw. On a failed save, the object strikes the target and stops moving. When the object strikes something, the object and what it strikes each take 3d8 damage. When you cast this spell using a spell slot of 2nd level or higher, the maximum weight of objects that you can target with this spell increases by 5 pounds, and the damage increases by 1d8, for each slot level above 1st."),


]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()


con.commit()

con.close()
