<h1 align="center">
docGPT 📄
</h1>
<h2 align="center">
ChatGPT directly integrated into Google Docs 📑
</h2>


<b>Feel free to make any pull requests to update this project. I will review and then approve them.</b>

Thank you to the wonderful devs who are building ChatGPT APIs!


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

5. Use the extension! (click Start instead of Ask to access the chat pop-up)

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

