## Django and twillio 

### Twilio Settings

settings.py file

```python

#Twilio settings

ACCOUNT_SID = 'add your ACCOUNT_SID'
AUTH_TOKEN = ' add your AUTH_TOKEN'

```

### add twilio phone

app.sms.views

```python

message = clientSend.messages.create(
                "+52"+str(user),
                body="Hi, you send a sms :)" ,
                from_='twilio number')
        

```
