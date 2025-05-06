# All API endpoints are defined here.

from flask import Flask, request, abort, Request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import db_functions

app = Flask(__name__)
CORS(app, origins=["https://localhost:5173"]) # Update on deployment
load_dotenv()
API_KEY = os.getenv("API_KEY")

def is_authorized_request(req: Request) -> bool:
  auth_header = req.authorization
  return auth_header and auth_header.type.lower() == "bearer" and auth_header.token == API_KEY

@app.get("/ping")
def pong():
  if not is_authorized_request(request):
    abort(401)
  return "Pong!"

@app.get("/users")
def get_users():
  if not is_authorized_request(request):
    abort(401)
  return db_functions.get_users()

@app.get("/users/<int:id>")
def get_user_by_id(id: int):
  if not is_authorized_request(request):
    abort(401)

  user_data = {}
  try:
    user_data = db_functions.get_user_by_id(id)
  except ValueError as e:
    abort(404, e)

  return user_data

@app.post("/users/<int:id>")
def set_user_name(id: int):
  if not is_authorized_request(request):
    abort(401)

  req_json: dict = request.get_json()
  new_name = req_json["userName"]
  return db_functions.set_user_name(id, new_name)

@app.post("/login")
def login():
  if not is_authorized_request(request):
    abort(401)

  req_json: dict = request.get_json()
  user_id = req_json["userId"]
  session_id = req_json["sessionId"]
  return db_functions.login_user(user_id, session_id)

@app.post("/logout")
def logout():
  if not is_authorized_request(request):
    abort(401)
  
  req_json: dict = request.get_json()
  user_id = req_json["userId"]
  return db_functions.logout_user(user_id)

@app.post("/register")
def register():
  if not is_authorized_request(request):
    abort(401)

  req_json: dict = request.get_json()
  phone_hash = req_json["phoneHash"]
  user_name = req_json["userName"]
  session_id = req_json["sessionId"]
  return db_functions.register_user(phone_hash, user_name, session_id)

@app.get("/classes")
def get_classes():
  if not is_authorized_request(request):
    abort(401)
  return db_functions.get_classes()

@app.post("/create-character")
def create_character():
  if not is_authorized_request(request):
    abort(401)

  req_json: dict = request.get_json()
  user_id = req_json["userId"]
  class_id = req_json["classId"]
  char_name = req_json["charName"]
  ability_scores = req_json["abilityScores"],
  notes = req_json["notes"]
  melee_wep_name = req_json["meleeWep"]
  ranged_wep_name = req_json["rangedWep"]

  weapon_ids: list[int] = []
  weapon_ids.append(db_functions.create_weapon(melee_wep_name, "melee"))
  weapon_ids.append(db_functions.create_weapon(ranged_wep_name, "ranged"))

  return db_functions.create_character(user_id, class_id, char_name, ability_scores, notes, weapon_ids)
