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

slack_event__adapter = SlackEventAdapter('2b3e220199a2e01f2b0f9198aeb18c52', '/slack/events' , app)

client = slack.WebClient(token='xoxb-1697344368020-1696311666130-hGJWTsjHbztsDmbSMq5t2QW5')
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
    
    client.chat_postMessage(channel=channel_id, text=f"Message: {message_count}")
    return Response(), 200

if __name__ == "__main__":
    app.run(debug=True)