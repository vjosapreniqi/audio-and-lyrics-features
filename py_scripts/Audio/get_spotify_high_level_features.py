import pandas as pd
import numpy as np
import time
from tqdm import tqdm
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

# Create a dataset with high level feature data
track_audio_data = pd.DataFrame(columns = ['Artist', 'track_title', 'track_spotify_id', 'loudness', 'tempo', 'key',
                                           'mode', 'acousticness', 'danceability', 'energy', 'instrumentalness',
                                           'liveness', 'speechiness', 'valence'])

track_audio_data['Artist'] = artist_song_data['Artist']
track_audio_data['track_title'] = artist_song_data['track_title']
track_audio_data['track_spotify_id'] = artist_song_data['track_spotify_id'] 

for i in tqdm(range(len(track_audio_data))):    
    if i % 5 == 0: # trigger sleep function after 5 iterations 
        time.sleep(1)
    try:   
        track_meta_analysis = sp.track(track_audio_data['track_spotify_id'][i])
        track_analysis = sp.audio_features(track_audio_data['track_spotify_id'][i])
    except :
        pass
    else:
        if None not in track_analysis:
                
            track_audio_data['loudness'][i] = track_analysis[0]['loudness']
            track_audio_data['tempo'][i] = track_analysis[0]['tempo']
            track_audio_data['key'][i] = track_analysis[0]['key']
            track_audio_data['mode'][i] = track_analysis[0]['mode']
            track_audio_data['acousticness'][i] = track_analysis[0]['acousticness']
            track_audio_data['danceability'][i] = track_analysis[0]['danceability']
            track_audio_data['energy'][i] = track_analysis[0]['energy']
            track_audio_data['instrumentalness'][i] = track_analysis[0]['instrumentalness'] 
            track_audio_data['liveness'][i] = track_analysis[0]['liveness']          
            track_audio_data['speechiness'][i] = track_analysis[0]['speechiness']
            track_audio_data['valence'][i] = track_analysis[0]['valence']         

# Save the dataset:
track_audio_data.to_csv('/path to the new data with pitch and timbre features/', index = None)