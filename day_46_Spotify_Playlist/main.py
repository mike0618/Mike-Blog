import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from my_conf import SPOTIFY_ID, SPOTIFY_SECRET

#  ===Scraping track titles====
date = input('Which year would you like to travel to? Type the date in this format: YYYY-MM-DD: ')
print(f'Scraping Billboard.com for top-100 tracks on {date}...')
billboard = requests.get(f'https://www.billboard.com/charts/hot-100/{date}').text
soup = BeautifulSoup(billboard, 'html.parser')
top100 = soup.find_all('span', class_='chart-element__information')
year = date[:4]

tracks = []
artists = []
for entry in top100:
    song = entry.select_one('span.chart-element__information__song').getText()
    artist = entry.select_one('span.chart-element__information__artist').getText()
    tracks.append(song)
    artists.append(artist)

# ===Spotify authentication===
print('Authentication on Spotify...')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_ID,
                                               client_secret=SPOTIFY_SECRET,
                                               redirect_uri='http://example.com',
                                               scope='playlist-modify-private',
                                               cache_path='token.txt',
                                               show_dialog=True))
user_id = sp.current_user()['id']
# print(user_id)

# ===Searching for track URIs on Spotify===
print('Searcing for tracks on Spotify...')
track_uris = []
for i in range(len(tracks)):
    try:
        # track_uris.append(sp.search(q=f'track:{tracks[i]} year: {year}', type='track')['tracks']['items'][0]['uri'])
        track_uris.append(
            sp.search(q=f'track:{tracks[i]} artist: {artists[i]}', type='track')['tracks']['items'][0]['uri'])
    except IndexError as err:
        print(f'There is no thack "{artists[i]} - {tracks[i]}" on Spotify')
print(f'\n{len(track_uris)} tracks found\n')

# ===Creating a playlist on Spotify===
playlist_id = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)['id']
print(f'The playlist "{date} Billboard 100" ID - {playlist_id} was created')

# ===Adding tracks into the playlist===
print('Adding tracks into the playlist')
sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)
print('Tracks were added!')
