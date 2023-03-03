"""Make some requests to OpenAI's chatbot"""
import os
from dotenv import load_dotenv
import openai
import flask
from flask import Flask

api_key = os.environ['api_key']

# Fancy stuff
import colorama

colorama.init(autoreset=True)

load_dotenv()

app = Flask(__name__)

openai.api_key = api_key


@app.route("/", methods=["GET"])
def index():
  return 'docGPT is up! <a href="https://github.com/cesarhuret/docGPT#using-the-rest-api">Read the docs</a>'


@app.route("/chat", methods=["POST"])
def chat():
  message = flask.request.json.get("message")

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "user",
      "content": message
    }]
  )
  
  return completion


def application():
  return app
