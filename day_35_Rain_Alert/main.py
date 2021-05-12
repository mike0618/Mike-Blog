import requests
import os
from twilio.rest import Client

OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('OWM_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
prm = {'lat': 59.947065,
       'lon': 30.229199,
       'appid': api_key,
       'exclude': 'current,minutely,daily'}
resp = requests.get(OWM_Endpoint, params=prm)
resp.raise_for_status()
w_data = resp.json()

for i in range(12):
    condition = w_data['hourly'][i]['weather'][0]['id']
    if condition < 600 or condition in range(611, 617):
        client = Client(account_sid, auth_token)
        message = client.messages.create(body="It's going to rain today. Remember to bring an ☔",
                                         from_='+17344555555',
                                         to='+79966555555')

        print(message.status)
        break
