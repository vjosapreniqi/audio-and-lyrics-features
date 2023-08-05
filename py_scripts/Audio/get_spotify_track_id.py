import pandas as pd
import time
import numpy as np
from tqdm import tqdm
import sys
import time
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data


client_id = '' # ddd your client id
client_secret = '' # add your client secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API


artist_song_data = pd.read_csv('/path to artists and songs data')

artist_song_data['track_spotify_id'] = ''
# add the spotify track id for each song:
for i in tqdm(range(len(artist_song_data))):
if i % 5 == 0: # trigger sleep function after 5 iterations 
    time.sleep(1)
    try:
        track_id = sp.search(q='artist:' + artist_song_data.Artist[i] \
                                + ' track:' + artist_song_data.track_title[i], type='track')
    except :
        pass
    else:
        if (track_id['tracks']['items'] !=[]): 
            artist_song_data['track_spotify_id'][i] = track_id['tracks']['items'][0]['id']
        else:
            artist_song_data['track_spotify_id'][i] = np.nan 


# save the data:
artist_song_data.to_csv('/path to the new data with pitch and timbre features/', index = None)