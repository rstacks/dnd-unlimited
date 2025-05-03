# Functions for interacting with the database are defined here.

import sqlite3

DB_CONNECTION_STR = "./db/dnd-db.db"

def _get_db_connection() -> sqlite3.Connection:
  con = sqlite3.connect(DB_CONNECTION_STR)
  return con

def get_users():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT id, phone_hash FROM users")
  raw_result: list[list] = cur.fetchall()
  con.close()
  
  formatted_records = []
  for user_data in raw_result:
    user_dict = {"id": user_data[0], "phone_hash": user_data[1]}
    formatted_records.append(user_dict)

  return { "users": formatted_records }












def get_skills():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT * FROM skills;")
  res = cur.fetchall()

  con.close()
  return res
