<h1 align="center">Lyrics Feature Modelling: Sentiments, Emotion Associations, Morals, and Topics</h1>
<div align="center">
</div>

This directory contains the code for retreiving artists song lyrics data, as well as audio and lyrics features as described in our paper: "Soundscapes of morality: Linking music preferences and moral 2
values through lyrics and audio" that have been submited for PLOS ONE Journal.
Here we cannot share the Moral Scores of the participants in our experiments due to the Pricacy implications but we share all the code that we used to create the features that we use as predictors for MFT values.

## Install:

To reuse this repo, install the requested libraries  
```bash
pip install -r requirements.txt
```
## Data:
In this directory, we have added the initial `artist page names` that were liked by the _LikeYouth_ (read more about this data [here](https://www.isi.it/media/255)) participants on Facebook.  Also, we have provided the best obtained LDA model file and the topic visualisation (.html) file. 

To get access to artists' lyrics and the lyrics' content features, please download the data as a `zip file` from the [Lyrics and audio annotated_data](https://osf.io/9z4dg) hosted in the [OSF](https://osf.io/45njf/) directory. When cloning/downloading the repo, add the `.csv files` into this directory to re-run the experiments we described. When using the initial `artist_lyrics_initial_dt.csv` and re-running the scripts we have provided here, you should be able to reproduce the features as in the dataset we shared in OSF (Artist_Songs_Lyrics_And_Audio_Features.xlsx).

## Implementation:
The `notebooks` directory contains the Jupyter scripts for obtaining lyrics features: 
sentiment analysis with [VADER](https://github.com/cjhutto/vaderSentiment), Valence, Arousal and Dominance scores with [BERT](https://huggingface.co/), emotion associations with 
[NRC lexicon](https://saifmohammad.com/WebPages/AccessResource.htm), moral scores with [MoralStrength](\https://github.com/oaraque/moral-foundations)) lexicon and lyrics topics using LDA topic modeling.
Whereas, the `py_scripts` folder contains the python code for extracting lyrics using [Genius API](https://docs.genius.com/) cleaning and preprocessing and language detection using [spaCy](https://spacy.io/), and also extracting the aduio feature using [Spotify API](https://developer.spotify.com/).


<!-- ## Citation
```bibtex
@article{preniqi2022lyrics_and_morals,
    title={{Soundscapes of morality: Linking music preferences and moral 2
values through lyrics and audio}},
    author={Preniqi, Vjosa and Kalimeri, Kyriaki and Saitis, Charalampos},
    journal={Plos One Journal},
    year={2023}
}
```
 -->