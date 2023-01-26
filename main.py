import os
import dotenv
from twilio.rest import Client

dotenv.load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv('account_sid')
# Your Auth Token from twilio.com/console
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

message = client.messages.create(
    to=os.getenv('to'),
    from_=os.getenv('from'),
    body="Cuidado!")

print(message.sid)
