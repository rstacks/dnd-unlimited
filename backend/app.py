# All API endpoints are defined here.

from flask import Flask
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












@app.get("/skills")
def get_skills():
  skills = db_functions.get_skills()
  return skills

# @app.get("/test-var/<int:num>")
# def show_num(num):
#   return f"your number: {num}"
