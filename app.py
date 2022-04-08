# from dotenv import load_dotenv
from flask import Flask, request
import os
from twilio.rest import Client
from dotenv import load_dotenv
from twilio.twiml.messaging_response import Message, MessagingResponse

load_dotenv()
 
app = Flask(__name__)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

@app.route('/bot', methods=['GET','POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    # if 'hours' in incoming_msg:
    #     # return a quote
    #     msg.body('This is hours')
    #     responded = True
    # if 'services' in incoming_msg:
    #     # return a cat pic
    #     msg.body('This is services')
    #     responded = True
    # if not responded:
    print('Hello world!', file=sys.stderr)
    response = 'I only know about famous quotes and cats, sorry!'
    resp = MessagingResponse()
    resp.message(response)
    # responded = False
    return str(resp)


@app.route('/test', methods=['POST'])
def test():
    incoming_msg = request.values.get('Body', '').lower()
    return "All Good"

if __name__ == '__main__':
    app.run()


