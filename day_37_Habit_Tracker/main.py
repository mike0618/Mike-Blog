import requests
from my_pixela_conf import USER, TOKEN, GRAPH
from datetime import date, timedelta

pixela_endp = 'https://pixe.la/v1/users'
user_prm = {'token': TOKEN,
            'username': USER,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes', }
# resp = requests.post(pixela_endp, json=user_prm)

graph_endp = f'{pixela_endp}/{USER}/graphs'
graph_conf = {'id': GRAPH,
              'name': 'Programming Time Graph',
              'unit': 'min',
              'type': 'int',
              'color': 'ajisai', }

headers = {'X-USER-TOKEN': TOKEN}
# resp = requests.post(graph_endp, json=graph_conf, headers=headers)

pix_endp = f'{pixela_endp}/{USER}/graphs/{GRAPH}'
d_ago = 0
date = (date.today() - timedelta(days=d_ago)).strftime('%Y%m%d')
pix_conf = {'date': date,
            'quantity': '120', }
# resp = requests.post(pix_endp, json=pix_conf, headers=headers)

pix_upd_endp = f'{pix_endp}/{date}'
pix_upd_conf = {'quantity': input("How many minutes did you code today?: ")}
resp = requests.put(pix_upd_endp, json=pix_upd_conf, headers=headers)
# resp = requests.delete(pix_upd_endp, headers=headers)

print(resp.text)
