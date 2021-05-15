import requests
from datetime import datetime
from my_conf import NUTRITIONIX_ID, NUTRITIONIX_KEY, NUTRITIONIX_ENDP, SHEETY_ENDP, TOKEN

GENDER = 'male'
WEIGHT_KG = 58
HEIGHT_CM = 165
AGE = 35

headers = {'x-app-id': NUTRITIONIX_ID,
           'x-app-key': NUTRITIONIX_KEY,
           'x-remote-user-id': '0'}

s_headers = {"Authorization": TOKEN}

text = input('Tell me which exercises you did: ')

n_prm = {'query': text,
       "gender":GENDER,
       "weight_kg":WEIGHT_KG,
       "height_cm":HEIGHT_CM,
       "age":AGE,}

n_resp = requests.post(NUTRITIONIX_ENDP, json=n_prm, headers=headers)
print(n_resp.json()['exercises'])
now = datetime.now()
date = now.date().strftime('%d/%m/%Y')
time = now.time().strftime('%H:%M:%S')

for e in n_resp.json()['exercises']:
    s_prm = {'workout':{'date': date,
                        'time': time,
                        'exercise': e['name'].title(),
                        'duration': e['duration_min'],
                        'calories': e['nf_calories'], }}

    s_resp = requests.post(SHEETY_ENDP, json=s_prm, headers=s_headers)
    print(s_resp.text)
