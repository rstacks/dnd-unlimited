# All API endpoints are defined here.

from flask import Flask, request
from flask_cors import CORS
import db_functions

app = Flask(__name__)
CORS(app, origins=["https://localhost:5173"]) # Update on deployment

@app.get("/ping")
def pong():
  return "Pong!"

@app.get("/users")
def get_users():
  return db_functions.get_users()

@app.post("/login")
def login():
  req_json: dict = request.get_json()
  user_id = req_json["userId"]
  session_id = req_json["sessionId"]
  return db_functions.login_user(user_id, session_id)

@app.post("/register")
def register():
  req_json: dict = request.get_json()
  phone_hash = req_json["phoneHash"]
  user_name = req_json["userName"]
  session_id = req_json["sessionId"]
  return db_functions.register_user(phone_hash, user_name, session_id)









@app.get("/skills")
def get_skills():
  skills = db_functions.get_skills()
  return skills

# @app.get("/test-var/<int:num>")
# def show_num(num):
#   return f"your number: {num}"
