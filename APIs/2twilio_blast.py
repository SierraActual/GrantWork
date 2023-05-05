from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'ACa91e77a28bf6cd94f9b3927de996b253'
auth_token = 'b119d6d5e34a63c685d6533d58c6e51b'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Your Twilio phone number
twilio_phone_number = '+18775897006'

# The phone number you want to send the SMS to
to_phone_number = '+19199248442'

# The message you want to send
message_body = 'This is a test SMS message from Twilio.'

# Send the SMS
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=to_phone_number
)

print(f"Message sent. SID: {message.sid}")
