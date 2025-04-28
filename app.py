from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
  return "<h1>Howdy, world!</h1>"

@app.get("/test-var/<int:num>")
def show_num(num):
  return f"your number: {num}"
