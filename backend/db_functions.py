# Functions for interacting with the database are defined here.

import sqlite3

DB_CONNECTION_STR = "./db/dnd-db.db"
SAVE_SHORT_TO_LONG = {
  "str": "Strength",
  "dex": "Dexterity",
  "con": "Constitution",
  "intl": "Intelligence",
  "wis": "Wisdom",
  "cha": "Charisma"
}

def _get_db_connection() -> sqlite3.Connection:
  con = sqlite3.connect(DB_CONNECTION_STR)
  return con

def _assign_class_saves(cur: sqlite3.Cursor, class_id: int, class_data: dict) -> None:
  saves_query = "SELECT st.st_name FROM class_saving_throw_proficiencies AS cstp INNER JOIN saving_throws AS st ON cstp.saving_throw_id = st.id WHERE cstp.class_id = ?"
  cur.execute(saves_query, (class_id,))
  class_saves: list[list] = cur.fetchall()
  for class_save in class_saves:
    class_data["saves"].append(SAVE_SHORT_TO_LONG[class_save[0]])

def _assign_class_skills(cur: sqlite3.Cursor, class_id: int, class_data: dict) -> None:
  skills_query = "SELECT s.skill_name FROM class_skill_proficiencies AS csp INNER JOIN skills AS s ON csp.skill_id = s.id WHERE csp.class_id = ?"
  cur.execute(skills_query, (class_id,))
  class_skills: list[list] = cur.fetchall()
  for class_skill in class_skills:
    class_data["skills"].append(class_skill[0])

def get_users():
  con = _get_db_connection()
  cur = con.cursor()
  cur.execute("SELECT id, phone_hash, session_uuid FROM users")
  raw_result: list[list] = cur.fetchall()
  con.close()
  
  formatted_records = []
  for user_data in raw_result:
    user_dict = {"id": user_data[0], "phone_hash": user_data[1], "session_uuid": user_data[2]}
    formatted_records.append(user_dict)

  return { "users": formatted_records }

def get_user_by_id(id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT phone_hash, user_type, user_name, session_uuid FROM users WHERE id = ?", (id,))
  user_data: list[str] = cur.fetchone()

  con.close()

  if not user_data:
    raise ValueError("User not found")

  return {
    "phone_hash": user_data[0],
    "user_type": user_data[1],
    "user_name": user_data[2],
    "session_uuid": user_data[3]
  }

def set_user_name(user_id: int, name: str):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET user_name = ? WHERE id = ?", (name, user_id))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def register_user(phone_hash: str, user_name: str, session_id: str):
  values = (phone_hash, user_name, session_id)

  con = _get_db_connection()
  
  cur = con.cursor()
  cur.execute("INSERT INTO users (user_type, phone_hash, user_name, session_uuid) VALUES ('player', ?, ?, ?)", values)
  con.commit()

  cur.execute("SELECT id FROM users WHERE session_uuid = ?", (session_id,))
  new_user_id: list[int] = cur.fetchone()
  
  con.close()

  return { "new_user_id": new_user_id[0] }

def login_user(user_id: int, session_id: str):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET session_uuid = ? WHERE id = ?", (session_id, user_id))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def logout_user(user_id: int):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET session_uuid = '' WHERE id = ?", (user_id,))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }

def get_classes():
  class_and_feat_query = "SELECT c.id, c.class_name, c.class_desc, c.hit_dice, f.feat_name, f.feat_desc FROM classes AS c INNER JOIN feats AS f ON c.feat_id = f.id"

  con = _get_db_connection()
  cur = con.cursor()
  cur.execute(class_and_feat_query)
  class_and_feat_records: list[list] = cur.fetchall()

  formatted_records = []
  for class_and_feat_record in class_and_feat_records:    
    record_dict = {
      "id": class_and_feat_record[0],
      "class_name": class_and_feat_record[1],
      "class_desc": class_and_feat_record[2],
      "hit_dice": class_and_feat_record[3],
      "feat_name": class_and_feat_record[4],
      "feat_desc": class_and_feat_record[5],
      "saves": [],
      "skills": []
    }

    _assign_class_saves(cur, class_and_feat_record[0], record_dict)
    _assign_class_skills(cur, class_and_feat_record[0], record_dict)

    formatted_records.append(record_dict)

  con.close()

  return { "classes": formatted_records }




def get_skills():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT * FROM skills;")
  res = cur.fetchall()

  con.close()
  return res
