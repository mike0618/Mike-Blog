import requests
from flight_search import FlightSearch
from my_conf import S_ENDP, S_HEADERS


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = requests.get(S_ENDP, headers=S_HEADERS).json()['prices']

    def write_iata(self, flightsearch: FlightSearch):
        for entry in self.sheet_data:
            if not entry['iataCode']:
                entry['iataCode'] = flightsearch.get_iatacode(entry['city'])
                endp = f"{S_ENDP}/{entry['id']}"
                prm = {'price': {'iataCode': entry['iataCode']}}
                self.resp = requests.put(endp, json=prm, headers=S_HEADERS)
                # print(self.resp.json())

