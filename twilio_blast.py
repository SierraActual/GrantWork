# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACa91e77a28bf6cd94f9b3927de996b253"
auth_token = os.environ["b119d6d5e34a63c685d6533d58c6e51b"]
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+18775897006",
  to="+19199248442"
)
print(message.sid)