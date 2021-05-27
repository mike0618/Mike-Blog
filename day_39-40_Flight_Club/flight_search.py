import requests
from my_conf import T_HEADERS
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDP = 'https://tequila-api.kiwi.com'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iatacode(self, city):
        prm = {'term': city,
               'location_types': 'city',
               'limit': 1}
        resp = requests.get(f'{TEQUILA_ENDP}/locations/query', params=prm, headers=T_HEADERS)
        return resp.json()['locations'][0]['code']

    def check_flight(self, origin_city_code, dest_city_code, from_time, to_time):
        prm = {'fly_from': origin_city_code,
               'fly_to': dest_city_code,
               'date_from': from_time,
               'date_to': to_time,
               'curr': 'USD',
               'flight_type': 'round',
               'max_stopovers': 0,
               'nights_in_dst_from': 7,
               'nights_in_dst_to': 28,
               'one_for_city': 1, }
        resp = requests.get(f'{TEQUILA_ENDP}/v2/search', headers=T_HEADERS, params=prm)
        data = resp.json().get('data')

        if data:
            index = 0
        else:
            prm['max_stopovers'] = 2
            resp = requests.get(f'{TEQUILA_ENDP}/v2/search', headers=T_HEADERS, params=prm)
            index = 1
            # print('\n')
            # pprint(resp.json())

        # except (IndexError, KeyError):
        #     print(f'No flights found for {dest_city_code}.')
        #     return None
        try:
            data = resp.json()['data'][0]
            route = data['route'][0]
            flightdata = FlightData(price=data['price'],
                                    origin_city=route['cityFrom'],
                                    origin_airport=route['flyFrom'],
                                    dest_city=data['route'][index]['cityTo'],
                                    dest_airport=data['route'][index]['flyTo'],
                                    stop_overs=prm['max_stopovers'] // 2,
                                    via_city=route['cityTo'],
                                    out_date=route['local_departure'].split('T')[0],
                                    return_date=data['route'][-1]['local_departure'].split('T')[0], )
            print(f'{flightdata.origin_city} - {flightdata.dest_city}: ${flightdata.price} from {flightdata.via_city}')
            return flightdata
        except (TypeError, IndexError):
            print(f'No flights found for {dest_city_code}.')
            return None
        except KeyError:
            print('Origin city unknown.')
            return 'origin unknown'
