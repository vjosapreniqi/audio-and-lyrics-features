import pandas as pd
import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector

'''
Use this script when you want to detect the language of a lyrics
'''
def get_lang_detector(nlp, name):
    return LanguageDetector()

nlp = spacy.load("en_core_web_sm")
Language.factory("language_detector", func=get_lang_detector)
nlp.add_pipe('language_detector', last=True)

languages_spacy = []

# Read the lyrics data for detecting the language.
artist_lyrics_data = pd.read_csv('../../Data/artist_original_and_cleaned_lyrics.csv')

artist_lyrics_data = artist_lyrics_data[:10] # comment out this line, this is just to test the method

for lyrics in artist_lyrics_data['cleaned_lyrics']:
    doc = nlp(lyrics)
    # cheking if the doc._.languages is not empty
    # then appending the first detected language in a list
    if(doc._.language):
        languages_spacy.append(doc._.language['language'])
    # if it is empty, we append the list by unknown
    else:
        languages_spacy.append('unknown')

# Add a column with the detected language for for each:
artist_lyrics_data.loc[:,'lang_detect_spacy'] = languages_spacy

# Save the dataset:
artist_lyrics_data.to_csv('../../Data/artist_lyrics_detected_lang_test.csv', index = None)