import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

#TODO need to fix the / no subject / issue (only seems to happen for TMobile so far, not on Verizon)
#TODO need to modify for Amazon instead. 62,000/mo email limit rather than 100/day
#TODO fix link error (may fix when we switch to SES)
#TODO need to possibly add message personalization to prevent spam triggers
#TODO think about adding time delay so we don't hit servers super hard all at once
#TODO need to test on large random number set with myself and Grant on the bottom to see if there's droppage or spam detection

msg1 = 'Hey, this is Grant with the Breathe Oxygen Bar. I just tried calling you about the sales position you applied for.'
msg2 = 'Please call back at your nearest convenience, or simply pick the time/location you\'d like to schedule an interview with this link:'
msg3 = 'https://calendy.com/breatheoxygen/harmon-corner-interview\n(You may need to respond to this message for the link to appear)'
msg4 = 'Thanks!\nGrant Barnes\n865.321.2915\nhttps://breatheoxygenbar.com/'

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

def main(msg):
    for number in range(len(NUMBERS)):
        for carrier in CARRIER_MAP:
            SENDGRID_API_KEY = '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'
            email = 'brantgarnes442@gmail.com'
            sms_gateway = NUMBERS[number]+'@'+ CARRIER_MAP[carrier]

            message = Mail(
                from_email=email,
                to_emails=sms_gateway,
                subject=" ",
                plain_text_content=msg
            )

            try:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                response = sg.send(message)
                print(f"Message sent. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error: {e}")

main(msg1)
main(msg2)
main(msg3)
main(msg4)