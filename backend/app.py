# All API endpoints are defined here.

from flask import Flask
import db_functions

app = Flask(__name__)

@app.get("/ping")
def pong():
  return "Pong!"

@app.get("/users/")














@app.get("/skills")
def get_skills():
  skills = db_functions.get_skills()
  return skills

# @app.get("/test-var/<int:num>")
# def show_num(num):
#   return f"your number: {num}"
