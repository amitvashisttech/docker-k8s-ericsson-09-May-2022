from flask import Flask 
import os 
import socket 

app = Flask(__name__)

@app.route("/")
def hello():
  html = "<h1> Hello From Flask Web App </h1>"
  return html

if __name__ == "__main__": 
  app.run(host="0.0.0.0",port=8080)
