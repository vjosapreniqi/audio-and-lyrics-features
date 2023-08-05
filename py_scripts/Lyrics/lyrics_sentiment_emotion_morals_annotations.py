import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import nltk.data
# Sentiment analysis with VADER:
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
from tqdm import tqdm

# There are several libraries that can be used to calculate word emotion association for the NRC Lexicon 
# (http://saifmohammad.com/WebPages/lexicons.html)

# Example of libraries:
# https://github.com/dropofwill/py-lex
# https://pypi.org/project/NRCLex/

# Morality library from moral streng lexicon
# https://github.com/oaraque/moral-foundations
import moralstrength
from moralstrength.moralstrength import estimate_morals
from moralstrength import lexicon_use
lexicon_use.select_version("latest")


def apply_vader_sentiment(df):
    negative = []
    neutral = []
    positive = []
    compound = []

    # Initialize the model:

    sid = SentimentIntensityAnalyzer()

    # Iterate through each lyrics for all the records and append the sentiment scores:

    for i in df.index:
        scores = sid.polarity_scores(df['cleaned_lyrics'][i])
        negative.append(scores['neg'])
        neutral.append(scores['neu'])
        positive.append(scores['pos'])
        compound.append(scores['compound'])
        
    # Create 4 columns to the artist_lyrics data frame for each score:

    df['vader_neg'] = negative
    df['vader_neu'] = neutral
    df['vader_pos'] = positive
    df['vader_comp'] = compound

    return df

def apply_nrc_sentiment_emo(df, en_lexicon, lemmas_column):
    
    df['negative'] = 0.0
    df['positive'] = 0.0
    df['anger'] = 0.0
    df['disgust'] = 0.0
    df['fear'] = 0.0
    df['sadness'] = 0.0
    df['anticipation'] = 0.0
    df['surprise'] = 0.0
    df['joy'] = 0.0
    df['trust'] = 0.0 

    for index, _ in df.iterrows():
        try:
            lyrics = list(map(lambda x:x, df[lemmas_column][index]))
            summary = en_lexicon.summarize_doc(lyrics)
            for key in summary.keys():
                df.at[index, key] = summary[key]
        except:
            continue   

    return df    

def list_of_lemmas_to_text(lyrics_spacy_lemmas):
    preprocessed_and_lemmatized_lyrics = []
    for i in tqdm(range(len(lyrics_spacy_lemmas))):
        joined_lyrics = ' '.join(lyrics_spacy_lemmas[i])
        preprocessed_and_lemmatized_lyrics.append(joined_lyrics) 
    return preprocessed_and_lemmatized_lyrics    

# Calculate moral scores:
# based on this repo: https://github.com/oaraque/moral-foundations
def calculate_moral_scores(preprocessed_and_lemmatized_lyrics):
    lyrics_moral_strength_score_dt = estimate_morals(
        preprocessed_and_lemmatized_lyrics, process=True)
    
    return lyrics_moral_strength_score_dt    

