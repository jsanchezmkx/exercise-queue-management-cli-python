# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC9706b47d65d3d7da5f0ba9b0f521ced2'
    auth_token = '291554e1cb43a6df5bcbe5812ce26dab'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+12058757677',
                        to='+56951147400'
                    )

    print(message.sid)
mensaje="hola mmgvo"
send(mensaje)