import os 
from twilio.rest import Client 
from dotenv import load_dotenv 

def send_SMS():

    load_dotenv()
    account_sid = os.getenv("TWILIOAPI")
    auth_token = os.getenv("TWILIOAUTH")
    fromNumber = os.getenv("TWILIONUMBER")
    toNumber = os.getenv("TWILIOCLIENTNUMBER")

    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create( 
                        body= "Hello this is a reminder to complete your daily wellness check! Please visit https://loved-crawdad-privately.ngrok-free.app/?id=1 to complete your check.",
                        from_=fromNumber,
                        to=toNumber,
                    )
    print(message.sid)
