class Notification_managers:
    def send_message(self,body):
        from twilio.rest import Client

        account_sid = 'ACd92151af03bcf3d5a2500184102e4d28'
        auth_token = 'e0db08887f5c1732bff8053ffc25ba2f'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=body,
            from_='+17752589981',
            to='+251953485998'
        )

        print(message.sid)


