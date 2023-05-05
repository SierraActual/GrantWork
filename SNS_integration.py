import boto3

# Create an SNS client
sns = boto3.client('sns', region_name='us-east-1')

# Set the phone numbers
phone_numbers = [
    '+19199248442'
]

message = "This is a test SMS message from Amazon SNS"

print("Starting to send messages...")

# Send the SMS to each phone number
for number in phone_numbers:
    print(f"Sending message to {number}")
    try:
        response = sns.publish(
            PhoneNumber=number,
            Message=message
        )
        print(f"Message sent to {number}: {response}")
    except Exception as e:
        print(f"Error sending message to {number}: {e}")

print("Finished sending messages.")
