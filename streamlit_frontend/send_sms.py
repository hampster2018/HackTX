import os 
from twilio.rest import Client 
from dotenv import load_dotenv 

load_dotenv()

account_sid = os.getenv("TWILIOAPI")
auth_token = os.getenv("TWILIOAUTH")
client = Client(account_sid, auth_token)

message = client.messages \
                .create( 
                    body= "Yo what is good",
                    from_='+18334172178',
                    to='+14693989895'
                )
print(message.sid)
