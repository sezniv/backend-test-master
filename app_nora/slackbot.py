import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event__adapter = SlackEventAdapter('6e4f10573ffe7d97862c20415e1a66bb', '/slack/events' , app)

client = slack.WebClient(token='xoxb-1697344368020-1696311666130-9QDdijOCdA3to5HeAFJPqSQj')
BOT_ID = client.api_call("auth.test")['user_id']

message_counts = {}

@slack_event__adapter.on('message')
def message(playload):
    print(playload)
    event = playload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        if user_id in message_counts:
            message_counts[user_id] +=1
        else:
            message_counts[user_id] = 1

        client.chat_postMessage(channel=channel_id, text=text)

@app.route('/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)
    
    client.chat_postMessage(channel=channel_id, text=f"Message: {message_counts}")
    return Response(), 200

@app.route('/interactive', methods=['POST'])
def interactive():
    payload = json.loads(request.form["payload"])
    print(payload)
    # Extra Credit: Uncomment out this section
     #thank_you_channel = "your_channel_id"
     #user_text = payload["view"]["state"]["values"]["my_block"]["my_action"]["value"]
     #client.chat_postMessage(channel=thank_you_channel, text=user_text)
    return Response(), 200
  
# Step 5: Payload is sent to this endpoint, we extract the `trigger_id` and call views.open
@app.route('/slashcommand', methods=['GET', 'POST'])
def slashcommand():
    with open("app_nora/modal.txt") as modalfile:
        client.views_open(user_id=request.form["user_id"], view=json.load(modalfile))
    return Response()

if __name__ == "__main__":
    app.run(debug=True)