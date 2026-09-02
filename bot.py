import os

from twilio.rest import Client


class bot():

    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.messaging_service_sid = os.environ["TWILIO_MESSAGING_SERVICE_SID"]
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, num, key):
        self.message = self.client.messages.create(
            messaging_service_sid=self.messaging_service_sid,
            body=str(key),
            to='+972' + num
        )