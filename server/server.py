"""Make some requests to OpenAI's chatbot"""
from dotenv import load_dotenv
import os
import flask
from flask import Flask
from PyChatGPT import pychat as PyChatGPT

# Fancy stuff
import colorama
from colorama import Fore

colorama.init(autoreset=True)

load_dotenv()

app = Flask(__name__)

gptBot = PyChatGPT.PyChatGPT()

@app.route("/", methods=["GET"])
def index():
  return 'ok'

@app.route("/chat", methods=["POST"])
def chat():
  message = flask.request.json.get("message")
  response = gptBot.conversate(message)
  return response

# retrieve port
def get_port():
  return int(os.environ.get("PORT", 8080))


if __name__ == "__main__":
  success = gptBot.initialise()
  from waitress import serve
  if(success):
    print("Server started at http://0.0.0.0:" + str(get_port()))
    serve(app, host="0.0.0.0", port=get_port())
  else:
    exit(1)