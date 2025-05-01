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
  ("Spellcasting", "You have the ability to cast spells as an action. Depending on the class, you will have access to a specific set of cantrips and casted spells.\nCantrips are spells with no cost that can be cast as often as you desire.\nCasted spells consume a Spell Slot upon casting.\nYour character has a limited number of Spell Slots. As you gain levels, the number of Spell Slots available to you increases. You may also gain higher level Spell Slots."),
  ("Rage", "You can imbue yourself with a primal power called Rage, a force that grants you extraordinary might and resilience. You can enter it as a Bonus Action if you aren't wearing Heavy armor.\nWhile active, your Rage follows the rules below.\nRage Damage: When you make an attack using Strength (with either a weapon or an Unarmed Strike) and deal damage to the target, you gain a bonus to the damage that increases as you gain levels as a Barbarian.\nStrength Advantage: You have Advantage on Strength checks and Strength saving throws.\nDuration: The Rage lasts until the end of your next turn, and it ends early if you don Heavy armor or have the Incapacitated condition. If your Rage is still active on your next turn, you can extend the Rage for another round by doing one of the following:\n- Make an attack roll against an enemy.\n- Force an enemy to make a saving throw.\n- Take a Bonus Action to extend your Rage.\nEach time the Rage is extended, it lasts until the end of your next turn."),
  ("Second Wind", "You have a limited well of physical and mental stamina that you can draw on. As a Bonus Action, you can use it to regain Hit Points equal to 1d10 plus your Fighter level.\nWhen you reach certain Fighter levels, you gain more uses of this feature. You start with two uses at level 1."),
  ("Martial Arts", "Your practice of martial arts gives you mastery of combat with Unarmed Strike. You gain the following benefits while you aren't wearing armor or wielding a Shield:\nBonus Unarmed Strike: You can make an Unarmed Strike as a Bonus Action.\nMartial Arts Die: At Monk level 1, you can roll 1d6 in place of the normal damage of your Unarmed Strike. This die changes as you gain Monk levels.\nDexterous Attacks: You can use your Dexterity modifier instead of your Strength modifier for the attack and damage rolls of your Unarmed Strikes. In addition, when you use the Grapple or Shove option of your Unarmed Strike, you can use your Dexterity modifier instead of your Strength modifier to determine the save DC."),
  ("Sneak Attack", "You know how to strike subtly and exploit a foe's distraction. At Rogue level 1, once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack roll if you have Advantage on the roll and the attack uses a ranged weapon.\nYou don't need Advantage on the attack roll if at least one of your allies is within 5 feet of the target, the ally doesn't have the Incapacitated condition, and you don't have Disadvantage on the attack roll.\nThe extra damage increases as you gain Rogue levels.")
]

con = sqlite3.connect(DB_CONNECTION_STR)
cur = con.cursor()

cur.executemany("INSERT INTO feats (feat_name, feat_desc) VALUES (?, ?)", feat_records)
con.commit()

con.close()
