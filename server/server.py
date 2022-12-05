"""Make some requests to OpenAI's chatbot"""
from dotenv import load_dotenv
import os
import flask
from flask import Flask
from revChatGPT.revChatGPT import Chatbot

load_dotenv()

app = Flask(__name__)
token = os.environ['session_token']

config = {
  "Authorization": "<API_KEY>",  # This is optional
  "session_token": token  # This is used to refresh the authentication
}


@app.route("/chat", methods=["POST"])
def index():
  message = flask.request.json.get("message")
  chatbot = Chatbot(config, conversation_id=None)
  chatbot.reset_chat()  # Forgets conversation
  chatbot.refresh_session()  # Uses the session_token to get a new bearer token
  resp = chatbot.get_chat_response(message)
  return resp['message']


if __name__ == "__main__":
  from waitress import serve
  print("Server started at http://localhost:8080")
  serve(app, host="0.0.0.0", port=8080)
