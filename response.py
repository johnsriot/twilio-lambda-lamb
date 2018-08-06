import os

import phonenumbers
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


class Caller:
    """ Automated call helper operations """
    def __init__(self, phonenumber, message_payload):
        self.phonenumber = phonenumber
        self.message_payload = int(message_payload) #Ensure we are passing an int
        self.dispatch = {
            1: 'https://handler.twilio.com/twiml/EHdf6d3bfcb64fa9121736d3ea5d0b2b6a', # Ice cream truck
            2: 'https://handler.twilio.com/twiml/EH50d84562bb51478300e08a017371c3e4', # Boom shaka lakka
            3: 'https://handler.twilio.com/twiml/EHfa775c7c156e3fb95d642bae052d6e3f', # Rick Rolled
            4: 'https://handler.twilio.com/twiml/EH0d97af2131d29ad0ca35a5768452392b' # Brother
        }

    def return_message(self):
        return self.dispatch[self.message_payload]

    def format_number(self):
        call_to = str("+1" + self.phonenumber)
        if self.validate_number(call_to):
            return call_to

    def validate_number(self, phonenumber):
        parse = phonenumbers.parse(phonenumber)
        return phonenumbers.is_valid_number(parse)


def lambda_handler(event, context):
    # Take raw string and turn into usable variables
    raw_data = event['Body'].split("+")
    caller = Caller(raw_data[1], raw_data[2])
    url_bin = caller.return_message() #TEST
    call_to = caller.format_number()
    # Initialize Twilio Client
    client = Client(os.environ['ACCOUNT_SID'], os.environ['AUTH_TOKEN'])
    call = client.calls.create(
                        url=url_bin,
                        to=call_to,
                        from_=os.environ['SOURCE']
                    )
    # Create success message for user
    resp = MessagingResponse()
    resp.message('Awesomesauce')
    return str(resp)
