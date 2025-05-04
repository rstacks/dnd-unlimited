# Functions for interacting with the database are defined here.

import sqlite3

DB_CONNECTION_STR = "./db/dnd-db.db"

def _get_db_connection() -> sqlite3.Connection:
  con = sqlite3.connect(DB_CONNECTION_STR)
  return con

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

def set_user_name(user_id: int, name: str):
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("UPDATE users SET user_name = ? WHERE id = ?", (name, user_id))
  con.commit()

  con.close()

  return { "updated_user_id": user_id }







def get_skills():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT * FROM skills;")
  res = cur.fetchall()

  con.close()
  return res
