import json
import re
import spotipy
from spotipy import SpotifyClientCredentials

f = open('spotify_data.json')

data = json.load(f)

top_songs = []

pattern = r"[{}]".format('\'') 

# Populating top_songs and cleaning the data
for song in data:
    if song['msPlayed'] > 60000:    # the songs were played for at least one minute
        top_songs.append((re.sub(pattern, '', song['artistName']), re.sub(pattern, '', song['trackName'])))

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id='e038f8c6d9e14a499a360d17e83981f9', 
                                                      client_secret='5a397378786942d290fa2b50e07195d1')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager, requests_timeout=10, retries=10)



all_song_ids = []       # all song ids, regardless of count

file_read = open('all_songs.txt', 'r')
file_write = open('distinct_songs.txt', 'w')
names_file = open('song_names.txt', 'w')


distinct_ids = []       # all the distinct song ids
lines = file_read.readlines()



distinct_songs = []

f.close()