# Functions for interacting with the database are defined here.

import sqlite3

DB_CONNECTION_STR = "./db/dnd-db.db"

def _get_db_connection() -> sqlite3.Connection:
  con = sqlite3.connect(DB_CONNECTION_STR)
  return con















def get_skills():
  con = _get_db_connection()

  cur = con.cursor()
  cur.execute("SELECT * FROM skills;")
  res = cur.fetchall()

  con.close()
  return res
