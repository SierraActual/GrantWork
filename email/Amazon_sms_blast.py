import boto3
import os

#TODO need to fix the / no subject / issue (only seems to happen for TMobile so far, not on Verizon); does a space fix this?
#TODO need to modify for Amazon instead. 62,000/mo email limit rather than 100/day
#TODO fix link error (may fix when we switch to SES)
#TODO need to possibly add message personalization to prevent spam triggers
#TODO think about adding time delay so we don't hit servers super hard all at once
#TODO need to test on large random number set with myself and Grant on the bottom to see if there's droppage or spam detection


NUMBERS = [
    '9199248442' 
]

CARRIER_MAP = {
    "verizon": "vtext.com",
    "tmobile": "tmomail.net",
    "sprint": "messaging.sprintpcs.com",
    "at&t": "txt.att.net",
    "boost": "smsmyboostmobile.com",
    "cricket": "sms.cricketwireless.net",
    "uscellular": "email.uscc.net",
}

MMS_CARRIER_MAP = {
    "verizon": "vzwpix.com",
    "tmobile": "tmomail.net",
    "sprint": "pm.sprint.com",
    "at&t": "mms.att.net",
    "boost": "myboostmobile.com",
    "cricket": "mms.cricketwireless.net",
    "uscellular": "mms.uscc.net",
}


def create_message():
    msg1 = 'Hey, this is Grant with the Breathe Oxygen Bar. I just tried calling you about the sales position you applied for.'
    msg2 = 'Please call back at your nearest convenience, or simply pick the time/location you\'d like to schedule an interview with this link:'
    msg3 = 'https://calendy.com/breatheoxygen/harmon-corner-interview\n(You may need to respond to this message for the link to appear)'
    msg4 = 'Thanks!\nGrant Barnes\n865.321.2915\nhttps://breatheoxygenbar.com/'
    message = [msg1, msg2, msg3, msg4]
    return message


def send_texts(message, NUMBERS, CARRIER_MAP):
    for number in NUMBERS:
        for carrier in CARRIER_MAP:
            # Your AWS Region. For example, "us-west-2"
            AWS_REGION = "us-east-1"

            # The subject line of the email
            SUBJECT = " "

            # The email body
            BODY_TEXT = message

            # The email addresses to send from and to
            SENDER = "brantgarnestest@breatheo22.com"
            RECIPIENT = f"{number}@{CARRIER_MAP[carrier]}"

            # Create a new SES client
            client = boto3.client('ses', region_name=AWS_REGION)

            # Construct the email message
            email = {
                'Source': SENDER,
                'Destination': {
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                'Message': {
                    'Subject': {
                        'Data': SUBJECT,
                    },
                    'Body': {
                        'Text': {
                            'Data': BODY_TEXT,
                        },
                    },
                },
            }

            print(RECIPIENT)
            # Send the email using Amazon SES
            try:
                response = client.send_email(**email)
                print("Email sent! Message ID:", response['MessageId'])
            except Exception as e:
                print("Error sending email:", e)


def main():
    message = create_message()
    send_texts(message[0], NUMBERS, CARRIER_MAP)


if __name__ == "__main__":
    main()