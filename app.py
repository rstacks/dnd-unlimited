from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
  return {"balls": 2}

@app.get("/name/<int:username>")
def show_name(username):
  return f"Hey there, {username}"
