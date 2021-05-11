import requests
from datetime import datetime, timezone

MY_LAT = 59.934280
MY_LNG = 30.335098

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

now = datetime.now(timezone.utc)

print(data['results']['sunset'], sunrise, sunset, now.hour)
