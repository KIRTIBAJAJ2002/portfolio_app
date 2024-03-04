import json
import re
from app.createRepo import createrepo
#from llmapi import Chatbot #new


with open("app/configtemplate.json", "r") as configfile:
    config_data = json.load(configfile)

def formatdata(resumedata):
    chatbot = Chatbot()  # Initialize the chatbot
    chat_message = f"This is my resume data {resume_data} and I want this data to be in this JSON format {config_data} and just please give me this as JSON data separately and Generate Output Like json''' ''' and please don't generate some extra text apart from that"

    chatbot_response = chatbot.send_message(chat_message)  # Send a message to the chatbot #new code


    # Create new chat thread
    # Streamed example:

    # for chunk in client.send_message(bot, message):
    #     pass
    # newconfigfile = chunk["text"]
    json_pattern = r'```json(.*?)```'
    json_matches = re.findall(json_pattern, newconfigfile, re.DOTALL)

    # If there are multiple matches, you can choose the first one or iterate through them
    if json_matches:
        json_data = json_matches[0].strip()  # Choose the first match
        # Parse the JSON data
        try:
            
            json_obj = json.loads(json_data)
            name=json_obj['name']
            # Save the formatted JSON to config_file.json and overwrite it
            with open("app/config_file.json", "w") as jsonfile:
                json.dump(json_obj, jsonfile, indent=2)
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
    else:
        print("No JSON data found in the text.")
    
    finallink=createrepo(name)
    return finallink

# Poe.chat_with_bot(token)
