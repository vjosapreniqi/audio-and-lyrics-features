import nltk
import spacy
from nltk.corpus import stopwords
stop_words = stopwords.words('english')


spacy_nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

# Lyrics Cleanup:
def clean_lyrics(df,column):
    
    """
    This function is used to clean the lyrics  
    parameters:
    df: dataframe
    column = name of the column to clean
    """
    df = df
    df.loc[:,column] =  df.loc[:, column].str.replace(r"[\(\[].*?[\)\]]", "",)
    df.loc[:,column] =  df.loc[:, column].str.replace('http\S+|www.\S+', '', case=False)
    df.loc[:,column] =  df.loc[:, column].str.replace(r"verse |[1|2|3]|chorus|bridge|outro","").str.replace("[","").str.replace("]","")
    df.loc[:,column] =  df.loc[:,column].str.replace(r"instrumental|intro|guitar|solo","").str.replace(r"instrumental|intro|guitar|solo","").str.replace(r"[^\w\d'\s[.!?,]]+","") 
    # We remove some of the generic words encountered after extracting the original lyrics 
    df.loc[:,column] = df.loc[:, column].str.replace("\n"," ").str.replace("urlcopyembedcopy", "").str.replace("embedshare", "").str.replace("EmbedShare", "").str.replace("URLCopyEmbedCopy", "")
    df.loc[:,column] = df.loc[:, column].str.strip()
    
    return df

# Lyrics tokenization:

def tokenize_lyrics(lyrics):
    
    tokens_list = []
    song_length_in_words = []
    
    tokenizer = nltk.RegexpTokenizer(r"\w+") # remove punctuation
    for each_lyric in lyrics:
        tokenized = tokenizer.tokenize(each_lyric.lower())
        tokens_list.append(tokenized)
        song_length_in_words.append(len(tokenized))
    
    return tokens_list, song_length_in_words

# Lyrics lemmatization using spacy lemmas:

def spacy_lematization(lyrics_col, allowed_postags = ['NOUN', 'ADJ', 'VERB', 'ADV']):
    
    lemmatized_lyrics = []
    
    for i in range(len(lyrics_col)):
        lyrics = spacy_nlp(lyrics_col[i])
        lemmatized_token = []
        for token in lyrics:
            if (not token.is_space) & (not token.is_punct) & (token.pos_ in allowed_postags): 
                lemmatized_token.append(token.lemma_)
        lemmatized_lyrics.append(lemmatized_token)  
    
    return lemmatized_lyrics

# Remove stopwords from the lyrics:

def remove_stop_words(lemmatized_list):
    
    # Here we extend the list of the stopwords:
    extended_stop_words = ['ooh','yeah','hey','whoa','woah', 'ohh', 'mmm', 'oooh','yah',
                      'yeh','mmm', 'hmm','deh','doh','jah','wa', 'dem', 'ohoh', 'nah',
                      'yuh', 'doo', 'boom' ,'doo', 'oohooh']

    stop_words.extend(extended_stop_words)

    # Clean stopwords for lyrics lemmas:
    lemmas_without_stopwords = []
    lemmas_count = []
    
    for song in lemmatized_list:
        filtered_text = []    
        for token in song:
            if token not in stop_words and (not token.isnumeric()):
                filtered_text.append(token)
        lemmas_without_stopwords.append(filtered_text)
        lemmas_count.append(len(filtered_text))
    
    return lemmas_without_stopwords, lemmas_count


