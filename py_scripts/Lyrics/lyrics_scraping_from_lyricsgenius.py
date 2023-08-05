import pandas as pd
import lyricsgenius
from lyricsgenius import Genius
from requests.exceptions import HTTPError, Timeout
from urllib.request import HTTPError

def search_lyrics_from_api(artist,n,access_token):
    """
    The function make use of the lyricsgenius library for extracting
    title, artist, and lyrics fields. Then it stores them into a pandas dataframe.
    
    Parameters:
    artist: artist/band to search in API
    n: maximum numbers of songs to search
    access_token: the access token of the genius api 
    that should be generated to extracting the data
    """
    
    try:
        genius_api = Genius(access_token, skip_non_songs=False, 
                            verbose = True,
                            timeout=10, 
                            sleep_time=0.2,
                            excluded_terms=["(Remix)", "(Live)", "[Instrumental]", "Remix"],
                            retries=2)

        list_lyrics = []
        list_title = []
        list_artist = []

        artist = genius_api.search_artist(artist,max_songs=n,
                                   sort='popularity', 
                                   allow_name_change = False)  

        if artist is not None:
            songs = artist.songs


            for song in songs:
                list_lyrics.append(song.lyrics)
                list_title.append(song.title)
                list_artist.append(song.artist)

    except (Timeout, AssertionError, HTTPError) as e:
        pass
    
    
    df = pd.DataFrame({'artist':list_artist,'title':list_title,'lyrics':list_lyrics})

    return df


# chose the list of the artists you want to extract the lyrics data for
liked_artists = pd.read_csv('../../Data/artists_fb_pages_liked_by_mft_participants.csv')

# When we what to test the method, we only use a handful number of artists:
liked_artists = liked_artists[:10] # comment this line when you want to extract the lyrics for all artists
liked_artists.reset_index(drop = True, inplace = True)

access_token = 'generate-your-own-token'
df = pd.DataFrame(columns = ['artist', 'title', 'lyrics'])
for i in range(len(liked_artists)):
    df0 = search_lyrics_from_api(liked_artists['Artist'][i], 10, access_token)
    df = pd.concat([df,df0])
    df.to_csv('../../Data/artists_songs_lyrics.csv', index = None)