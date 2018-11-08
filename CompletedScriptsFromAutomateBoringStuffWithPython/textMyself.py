#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = 'AC8abecc1dee36de15032981ea7e8f154f'
authToken = '4030fae0e11c5cba674e89766fd92f36'
myNumber = '+447719299511'
TwilioNumber = '+447480619517'

from twilio.rest import Client

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
    
