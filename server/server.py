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

@app.route("/chat", methods=["POST"])
def index():
  message = flask.request.json.get("message")
  response = gptBot.conversate(message)
  return response

def application():
  success = gptBot.initialise()
  if(success):
    return app
  else:
    exit(1)