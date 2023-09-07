import numpy as np
import os
import string,re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

stop = set(stopwords.words('english'))
punctuation = list(string.punctuation)
stop.update(punctuation)

nltk.download('averaged_perceptron_tagger')
lemmatizer = WordNetLemmatizer()

import pickle


def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# Removing the square brackets
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

# Removing URL's
def remove_urls(text):
    return re.sub(r'http\S+', '', text)

# Removing the stopwords from text
def remove_stopwords(text):
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stop:
            final_text.append(i.strip().lower())
    return " ".join(final_text)
def remove_punctuation(text):
    punctuationfree="".join([i for i in text if i not in string.punctuation])
    return punctuationfree
# Final function to clean the text
def clean_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = remove_urls(text)
    text = remove_stopwords(text)
    text = remove_punctuation(text)
    return text

def pre_process(title,body,tfidf,selector):
    text = title+" "+body
    
    text = clean_text(text)
    tokens = word_tokenize(text)
    lemmas = " ".join([lemmatizer.lemmatize(token) for token in tokens])
#     print(lemmas)
    tfidf_vector = tfidf.transform([lemmas])
    X = tfidf_vector.toarray()
    red_x = selector.transform(X)
    return red_x