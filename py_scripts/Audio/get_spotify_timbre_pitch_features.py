import pandas as pd
import numpy as np
import time
from tqdm import tqdm
import time
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
from scipy.stats import skew, kurtosis

client_id = '' # ddd your client id
client_secret = '' # add your client secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

# If you want to replicate the results please see te artist data we have published in OSF (the link is provided in readme file) you need a spotify id of the song for this experiment
artist_track_id = pd.read_csv('/path to artists and songs data')


# Create a dataset with artist song, and all pitch and timbre dimensions:
track_audio_data = pd.DataFrame(columns = ['Artist', 'track_title', 'track_spotify_id',
'timbre_1_mean', 'timbre_1_std', 'timbre_1_mean_diff', 'timbre_1_std_diff',
'timbre_2_mean', 'timbre_2_std', 'timbre_2_mean_diff', 'timbre_2_std_diff', 
'timbre_3_mean', 'timbre_3_std', 'timbre_3_mean_diff', 'timbre_3_std_diff',
'timbre_4_mean', 'timbre_4_std', 'timbre_4_mean_diff', 'timbre_4_std_diff',
'timbre_5_mean', 'timbre_5_std', 'timbre_5_mean_diff', 'timbre_5_std_diff',
'timbre_6_mean', 'timbre_6_std', 'timbre_6_mean_diff', 'timbre_6_std_diff',
'timbre_7_mean', 'timbre_7_std', 'timbre_7_mean_diff', 'timbre_7_std_diff',
'timbre_8_mean', 'timbre_8_std', 'timbre_8_mean_diff', 'timbre_8_std_diff',
'timbre_9_mean', 'timbre_9_std', 'timbre_9_mean_diff', 'timbre_9_std_diff',
'timbre_10_mean', 'timbre_10_std', 'timbre_10_mean_diff', 'timbre_10_std_diff',
'timbre_11_mean', 'timbre_11_std', 'timbre_11_mean_diff', 'timbre_11_std_diff',
'timbre_12_mean', 'timbre_12_std', 'timbre_12_mean_diff', 'timbre_12_std_diff',
'pitch_1_mean', 'pitch_1_std', 'pitch_1_mean_diff', 'pitch_1_std_diff',
'pitch_2_mean', 'pitch_2_std', 'pitch_2_mean_diff', 'pitch_2_std_diff', 
'pitch_3_mean', 'pitch_3_std', 'pitch_3_mean_diff', 'pitch_3_std_diff',
'pitch_4_mean', 'pitch_4_std', 'pitch_4_mean_diff', 'pitch_4_std_diff',
'pitch_5_mean', 'pitch_5_std', 'pitch_5_mean_diff', 'pitch_5_std_diff',
'pitch_6_mean', 'pitch_6_std', 'pitch_6_mean_diff', 'pitch_6_std_diff',
'pitch_7_mean', 'pitch_7_std', 'pitch_7_mean_diff', 'pitch_7_std_diff',
'pitch_8_mean', 'pitch_8_std', 'pitch_8_mean_diff', 'pitch_8_std_diff',
'pitch_9_mean', 'pitch_9_std', 'pitch_9_mean_diff', 'pitch_9_std_diff',
'pitch_10_mean', 'pitch_10_std', 'pitch_10_mean_diff', 'pitch_10_std_diff',
'pitch_11_mean', 'pitch_11_std', 'pitch_11_mean_diff', 'pitch_11_std_diff',
'pitch_12_mean', 'pitch_12_std', 'pitch_12_mean_diff', 'pitch_12_std_diff'])

# Add the artist and track info to the new dataset:

track_audio_data['Artist'] = artist_track_id['Artist']
track_audio_data['track_title'] = artist_track_id['track_title']
track_audio_data['track_spotify_id'] = artist_track_id['track_spotify_id']

#Extracting timbre and pitch for all the song segments:

for i in tqdm(range(len(track_audio_data))):
    #Timbres over segments:
    t1 = []; t2 = []; t3 = []; t4 = []; t5 = []; t6 = []; t7 = []; t8 = []; t9 = []; t10 = []; t11 = []; t12 = []
    # Pitches over segments:
    p1 = []; p2 = []; p3 = []; p4 = []; p5 = []; p6 = []; p7 = []; p8 = []; p9 = []; p10 = []; p11 = []; p12 = []
    
    if i % 5 == 0: # trigger sleep function after 5 iterations 
        time.sleep(1)
    try:   
        track_analysis = sp.audio_analysis(track_audio_data['track_spotify_id'][i])   
    
    except :
        pass
    else:
        for j in range(len(track_analysis['segments'])):
            # Timbre:
            t1.append(track_analysis['segments'][j]['timbre'][0])
            t2.append(track_analysis['segments'][j]['timbre'][1])
            t3.append(track_analysis['segments'][j]['timbre'][2])
            t4.append(track_analysis['segments'][j]['timbre'][3])
            t5.append(track_analysis['segments'][j]['timbre'][4])
            t6.append(track_analysis['segments'][j]['timbre'][5])
            t7.append(track_analysis['segments'][j]['timbre'][6])
            t8.append(track_analysis['segments'][j]['timbre'][7])
            t9.append(track_analysis['segments'][j]['timbre'][8])
            t10.append(track_analysis['segments'][j]['timbre'][9])
            t11.append(track_analysis['segments'][j]['timbre'][10])
            t12.append(track_analysis['segments'][j]['timbre'][11])
            # Pitches
            p1.append(track_analysis['segments'][j]['pitches'][0])
            p2.append(track_analysis['segments'][j]['pitches'][1])
            p3.append(track_analysis['segments'][j]['pitches'][2])
            p4.append(track_analysis['segments'][j]['pitches'][3])
            p5.append(track_analysis['segments'][j]['pitches'][4])
            p6.append(track_analysis['segments'][j]['pitches'][5])
            p7.append(track_analysis['segments'][j]['pitches'][6])
            p8.append(track_analysis['segments'][j]['pitches'][7])
            p9.append(track_analysis['segments'][j]['pitches'][8])
            p10.append(track_analysis['segments'][j]['pitches'][9])
            p11.append(track_analysis['segments'][j]['pitches'][10])
            p12.append(track_analysis['segments'][j]['pitches'][11])

        # ****************************Timbre Features****************************
        track_audio_data.timbre_1_mean[i] = np.mean(t1) 
        track_audio_data.timbre_1_std[i] = np.std(t1)
        track_audio_data.timbre_1_mean_diff[i] = np.mean(np.diff(t1))
        track_audio_data.timbre_1_std_diff [i] = np.std(np.diff(t1))

        track_audio_data.timbre_2_mean[i] = np.mean(t2)
        track_audio_data.timbre_2_std[i] = np.std(t2)
        track_audio_data.timbre_2_mean_diff[i] = np.mean(np.diff(t2))
        track_audio_data.timbre_2_std_diff [i] = np.std(np.diff(t2))

        track_audio_data.timbre_3_mean[i] = np.mean(t3)
        track_audio_data.timbre_3_std[i] = np.std(t3)
        track_audio_data.timbre_3_mean_diff[i] = np.mean(np.diff(t3))
        track_audio_data.timbre_3_std_diff [i] = np.std(np.diff(t3))

        track_audio_data.timbre_4_mean[i] = np.mean(t4)
        track_audio_data.timbre_4_std[i] = np.std(t4)
        track_audio_data.timbre_4_mean_diff[i] = np.mean(np.diff(t4))
        track_audio_data.timbre_4_std_diff [i] = np.std(np.diff(t4))

        track_audio_data.timbre_5_mean[i] = np.mean(t5)
        track_audio_data.timbre_5_std[i] = np.std(t5)
        track_audio_data.timbre_5_mean_diff[i] = np.mean(np.diff(t5))
        track_audio_data.timbre_5_std_diff [i] = np.std(np.diff(t5))

        track_audio_data.timbre_6_mean[i] = np.mean(t6)
        track_audio_data.timbre_6_std[i] = np.std(t6)
        track_audio_data.timbre_6_mean_diff[i] = np.mean(np.diff(t6))
        track_audio_data.timbre_6_std_diff [i] = np.std(np.diff(t6))

        track_audio_data.timbre_7_mean[i] = np.mean(t7)
        track_audio_data.timbre_7_std[i] = np.std(t7) 
        track_audio_data.timbre_7_mean_diff[i] = np.mean(np.diff(t7))
        track_audio_data.timbre_7_std_diff [i] = np.std(np.diff(t7))

        track_audio_data.timbre_8_mean[i] = np.mean(t8)
        track_audio_data.timbre_8_std[i] = np.std(t8)
        track_audio_data.timbre_8_mean_diff[i] = np.mean(np.diff(t8))
        track_audio_data.timbre_8_std_diff [i] = np.std(np.diff(t8))

        track_audio_data.timbre_9_mean[i] = np.mean(t9)
        track_audio_data.timbre_9_std[i] = np.std(t9)
        track_audio_data.timbre_9_mean_diff[i] = np.mean(np.diff(t9))
        track_audio_data.timbre_9_std_diff [i] = np.std(np.diff(t9))

        track_audio_data.timbre_10_mean[i] = np.mean(t10)
        track_audio_data.timbre_10_std[i] = np.std(t10)
        track_audio_data.timbre_10_mean_diff[i] = np.mean(np.diff(t10))
        track_audio_data.timbre_10_std_diff [i] = np.std(np.diff(t10))

        track_audio_data.timbre_11_mean[i] = np.mean(t11)
        track_audio_data.timbre_11_std[i] = np.std(t11)
        track_audio_data.timbre_11_mean_diff[i] = np.mean(np.diff(t11))
        track_audio_data.timbre_11_std_diff [i] = np.std(np.diff(t11))

        track_audio_data.timbre_12_mean[i] = np.mean(t12)
        track_audio_data.timbre_12_std[i] = np.std(t12)
        track_audio_data.timbre_12_mean_diff[i] = np.mean(np.diff(t12))
        track_audio_data.timbre_12_std_diff [i] = np.std(np.diff(t12))
        
        # ****************************Pitch Features****************************
        track_audio_data.pitch_1_mean[i] = np.mean(p1)
        track_audio_data.pitch_1_std[i] = np.std(p1)
        track_audio_data.pitch_1_mean_diff[i] = np.mean(np.diff(p1))
        track_audio_data.pitch_1_std_diff [i] = np.std(np.diff(p1))

        track_audio_data.pitch_2_mean[i] = np.mean(p2)
        track_audio_data.pitch_2_std[i] = np.std(p2)
        track_audio_data.pitch_2_mean_diff[i] = np.mean(np.diff(p2))
        track_audio_data.pitch_2_std_diff [i] = np.std(np.diff(p2))

        track_audio_data.pitch_3_mean[i] = np.mean(p3)
        track_audio_data.pitch_3_std[i] = np.std(p3)
        track_audio_data.pitch_3_mean_diff[i] = np.mean(np.diff(p3))
        track_audio_data.pitch_3_std_diff [i] = np.std(np.diff(p3))

        track_audio_data.pitch_4_mean[i] = np.mean(p4)
        track_audio_data.pitch_4_std[i] = np.std(p4)
        track_audio_data.pitch_4_mean_diff[i] = np.mean(np.diff(p4))
        track_audio_data.pitch_4_std_diff [i] = np.std(np.diff(p4))

        track_audio_data.pitch_5_mean[i] = np.mean(p5)
        track_audio_data.pitch_5_std[i] = np.std(p5)
        track_audio_data.pitch_5_mean_diff[i] = np.mean(np.diff(p5))
        track_audio_data.pitch_5_std_diff [i] = np.std(np.diff(p5))

        track_audio_data.pitch_6_mean[i] = np.mean(p6)
        track_audio_data.pitch_6_std[i] = np.std(p6)
        track_audio_data.pitch_6_mean_diff[i] = np.mean(np.diff(p6))
        track_audio_data.pitch_6_std_diff [i] = np.std(np.diff(p6))

        track_audio_data.pitch_7_mean[i] = np.mean(p7)
        track_audio_data.pitch_7_std[i] = np.std(p7) 
        track_audio_data.pitch_7_mean_diff[i] = np.mean(np.diff(p7))
        track_audio_data.pitch_7_std_diff [i] = np.std(np.diff(p7))

        track_audio_data.pitch_8_mean[i] = np.mean(p8)
        track_audio_data.pitch_8_std[i] = np.std(p8)
        track_audio_data.pitch_8_mean_diff[i] = np.mean(np.diff(p8))
        track_audio_data.pitch_8_std_diff [i] = np.std(np.diff(p8))

        track_audio_data.pitch_9_mean[i] = np.mean(p9)
        track_audio_data.pitch_9_std[i] = np.std(p9)
        track_audio_data.pitch_9_mean_diff[i] = np.mean(np.diff(p9))
        track_audio_data.pitch_9_std_diff [i] = np.std(np.diff(p9))

        track_audio_data.pitch_10_mean[i] = np.mean(p10)
        track_audio_data.pitch_10_std[i] = np.std(p10)
        track_audio_data.pitch_10_mean_diff[i] = np.mean(np.diff(p10))
        track_audio_data.pitch_10_std_diff [i] = np.std(np.diff(p10))

        track_audio_data.pitch_11_mean[i] = np.mean(p11)
        track_audio_data.pitch_11_std[i] = np.std(p11)
        track_audio_data.pitch_11_mean_diff[i] = np.mean(np.diff(p11))
        track_audio_data.pitch_11_std_diff [i] = np.std(np.diff(p11))

        track_audio_data.pitch_12_mean[i] = np.mean(p12)
        track_audio_data.pitch_12_std[i] = np.std(p12)
        track_audio_data.pitch_12_mean_diff[i] = np.mean(np.diff(p12))
        track_audio_data.pitch_12_std_diff [i] = np.std(np.diff(p12))

# Save the dataset after feature extraction:
track_audio_data.to_csv('/path to the new data with pitch and timbre features/', index = None)