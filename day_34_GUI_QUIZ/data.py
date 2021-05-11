import requests

params = {'amount': 10,
          'type': 'boolean'}
resp = requests.get('https://opentdb.com/api.php', params=params)
resp.raise_for_status()
question_data = resp.json()['results']
