# docGPT 📄
ChatGPT directly integrated into Google Docs 🤌

### Table of Contents
**[Setup](#setup)**<br>
**[Installation](#installation)**<br>
**[Usage](#usage)**<br>

## Setup

You can choose to either do everything locally, or just use a premade template document I have, and make a copy of that.

Template document with ChatGPT integrated: https://docs.google.com/document/d/1N7qvw5mZdVe2u2IQ5pnVDmUjHsLEfq9_Z0Tf8PHloZA/edit?usp=sharing

## Installation

1. Clone this repo with 

  ```
  git clone https://github.com/cesarhuret/docGPT.git
  ```

2. Visit https://chat.openai.com/chat and log in or sign up
  - Open console with `F12`
  - Open `Application` tab > Cookies
  ![image](https://user-images.githubusercontent.com/36258159/205494773-32ef651a-994d-435a-9f76-a26699935dac.png)
  - Copy the value for `__Secure-next-auth.session-token` and paste it into `.env.example` under `session_token`.
  - Rename `.env.example` to `.env`

3. Set up and host the web server: 

  ```
  cd server
  ## Install Requirements
  pip install -r requirements.txt

  ## Run the server
  python3 server.py
  ```

4. Get the URL of the server. Ex: http://localhost:8080/chat

5. Enter your server URL into the Google Docs add-on script. 

6. Google Docs
  ⋅⋅- Go to Google Docs and create a new document.
  ⋅⋅- Click on Extension > Apps Script
  ⋅⋅- Copy the contents of `add-on/ask.js` into the script editor
  ⋅⋅- Replace the `SERVER_URL` variable with your server URL
  ⋅⋅- Save the script
  ⋅⋅- Go back to the Google Doc and refresh the page
  ⋅⋅- Click on Extension - `ChatGPT` should be visible under Apps Script

## Usage

1. Type something in your Google Doc

  ![alt text](https://i.imgur.com/287n0U0l.png)
  
2. Select your question, or whatever text you want to send to ChatGPT
  
  ![alt text](https://i.imgur.com/62tfu0kl.png)

3. Use the extension! 

  ![alt text](https://i.imgur.com/g7w6Qgfl.png)

4. Accept the Authorization request & sign into google

5. Get your result!

  ![alt text](https://i.imgur.com/MEidlLYl.png)
