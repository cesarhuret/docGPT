<h1 align="center">
docGPT 📄
</h1>
<p align="center">
ChatGPT directly integrated into Google Docs 📑
</p>

_If you want me to maintain this repo, please star ⭐️_

### Table of Contents
**[Notes](#Notes)**<br>
**[Usage](#usage)**<br>
**[Run your own ChatGPT API (Devs only)](#API)**<br>
**[Credits](#credits)**<br>

## Notes

This is still in development. There may be times when it doesn't work, because of OpenAI's overloads. I made this at 4 am, so I might not have the best error handlings, but I'll be fixing all that within the next few days.

You can choose to either do everything locally, or just use a premade template document I have, and make a copy of that.

**Skip to the **[USAGE](#usage)** section if you are using the PREMADE TEMPLATE.**

Template document with ChatGPT integrated: https://docs.google.com/document/d/1N7qvw5mZdVe2u2IQ5pnVDmUjHsLEfq9_Z0Tf8PHloZA/edit?usp=sharing

This project is unofficial, and an unofficial ChatGPT api (revChatGPT) is being used for this. Will be updated when OpenAI releases ChatGPT as a full API.

## Usage

- **Google Docs**<br>
- **MS Word**<br>

### Google Docs

1. Get the template: https://docs.google.com/document/d/1N7qvw5mZdVe2u2IQ5pnVDmUjHsLEfq9_Z0Tf8PHloZA/edit?usp=sharing

2. Make a copy of the document

  ![alt text](https://i.imgur.com/YlWvBEzl.png)

3. Type something in your Google Doc

  ![alt text](https://i.imgur.com/287n0U0l.png)
  
4. Select your question, or whatever text you want to send to ChatGPT
  
  ![alt text](https://i.imgur.com/62tfu0kl.png)

5. Use the extension! 

  ![alt text](https://i.imgur.com/g7w6Qgfl.png)

6. Accept the Authorization request & sign into google

  ![alt text](https://i.imgur.com/LbmKDmpl.png)
  
7. Click Advanced, go to ChatGPT & allow the scopes required

  ![alt text](https://i.imgur.com/D7gzZpal.png)


8. Get your result!

  ![alt text](https://i.imgur.com/MEidlLYl.png)
  
### MS Word

1. Open a new word document

2. Enable the Developer Tab on Word

3. Click Macros
  ![alt text](https://i.imgur.com/946Lupxl.png)

4. Create a new macro with the name AddToShortcut
  ![alt text](https://i.imgur.com/1DSMx78l.png)
  
5. Copy the code in `wordGPT/ask.bas` of this repo, and paste it into the Word VBA Editor

6. Click `Tools > References` in the navbar <br>
  ![alt text](https://i.imgur.com/eiWU4Ecl.png)

7. Search for Microsoft Scripting Runtime and enable it <br>
  ![image](https://user-images.githubusercontent.com/67405604/205881130-c82f1ace-2c06-462e-a196-e7188077e9c5.png)

8. Click OK and Save the file containing the code you pasted.

9. Right click selected text in Word and click `Ask ChatGPT`

![image](https://user-images.githubusercontent.com/67405604/205882403-1fee052b-1a40-45e0-838b-f0c9268611ed.png)

10. Wait for your result! (Word may become temporarily unresponsive while waiting for the result)

## API 

Follow this guide if you don't want to use my premade template, and want to start a ChatGPT REST API server of your own!

### Without Docker

1. Clone this repo with 

  ```
  git clone https://github.com/cesarhuret/docGPT.git
  ```

2. Visit https://chat.openai.com/chat and log in or sign up
  - Rename `.env.example` to `.env`
  - Get your OpenAI email and password, and insert them into the `.env` file. 

3. Set up and host the web server: 

  ```
  cd server
  ## Install Requirements
  pip install -r requirements.txt

  ## Run the server
  python server.py
  ```

### Docker Installation

1. Make sure you have docker installed and running

2. Build your docker image

```
cd server

#Build the image
docker build -t chatgpt-api

```

3. Run your docker image

```
docker run -p 8080:8080 -e email=YOUR_EMAIL_GOES_HERE -e password=YOUR_PASSWORD_GOES_HERE chatgpt-api

```

### Using the REST API

- Send a POST request to https://docgpt.kesarx.repl.co with an application/json body:

```
{
  'message': 'Your questions go here'
}
```
- returns a string: 

```
"here's the response to your question"
```


### In Google Docs

4. Get the URL of the server. Ex: http://localhost:8080/chat

5. Enter your server URL into the Google Docs add-on script. 

6. Google Docs
  - Go to Google Docs and create a new document.
  - Click on Extension > Apps Script
  - Copy the contents of `add-on/ask.js` into the script editor
  - Replace the `SERVER_URL` variable with your server URL
  - Save the script
  - Go back to the Google Doc and refresh the page
  - Click on Extension - `ChatGPT` should be visible under Apps Script
  
## Credits

- https://github.com/rawandahmad698/PyChatGPT :pray:
