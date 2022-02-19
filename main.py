# Download the helper library from https://www.twilio.com/docs/python/install
import os
import time
from twilio.rest import Client
from datetime import datetime


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

date = datetime.now()
while True:
  if date.hour == 1 and date.minute == 53:

    message = client.messages \
                    .create(
                        body="Hello there! Have a good morning",
                        from_='+19378724705',
                        to='+19022297944'
                    )

    print(message.sid)
  time.sleep(60)
