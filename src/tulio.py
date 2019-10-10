from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


class tulio:
    def __init__(self):
        account_sid = 'AC3eb32cd8e90f9482401435ecab993e1a'
        auth_token = '5d2af95154e2b24cffdf71af38dae97e'
        self.client = Client(account_sid, auth_token)

    def enviarMensaje(self, msg, numero):
        message = self.client.messages.create(
                              body=msg,
                              from_='+13128364203',
                              to=numero
                          )
        return message