# mailbot
Autonomous AI newsletter service

This is an autonomous AI newletter service that searches for AI related news, creates a 5 headlines and short description of each news and sends it to the chosen email(s).
This project is insipired by youtuber AllAboutAI's video 'Create Your Fully Autonomous AI Newsletter Service 📧': https://youtu.be/FWnwlR09Z3U

To use this code:
1. Add your own Google API key as a plain text to the file googleapikey.txt
2. Add OpenAi API key as a plain text to the file openaiapikey.txt
3. In file automail.py add your Mailgun API key and domain name to the lines 23 and 24
4. Add recipiens email as a plain text to the recipiens.txt

Notice that the emails can end up into the trashmail.

If you want to change the subject of the newsletter, you have to change the search query of newsletter.py line 27 and edit the instructions for the AI at prompt1.txt.
