# from dotenv import load_dotenv
from flask import Flask, request
import os
from twilio.rest import Client
from dotenv import load_dotenv
import sys
from twilio.twiml.messaging_response import Message, MessagingResponse

load_dotenv()
 
app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/bot', methods=['GET','POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    From = request.values.get('From', '').lower()
    print(request.values)

    print(incoming_msg)

    message = client.messages.create(
                                body='Hello there!',
                                from_='whatsapp:+14155238886',
                                to=From
                            )

    print(message.sid)
    return str(message) 


@app.route('/test', methods=['POST'])
def test():
    incoming_msg = request.values.get('Body', '').lower()
    return "All Good"

if __name__ == '__main__':
    app.run()


