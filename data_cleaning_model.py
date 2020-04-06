# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 09:40:46 2019

@author: anjali.dharmik
"""

import re,string
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

def preprocessing_model(doc1):
    doc1 = doc1.lower()
    doc1 = re.sub(r'\d+', '', doc1)
    pun = list(string.punctuation)
    pun.extend(["“","”"])
    doc1 =" ".join([doc1.replace(str_pun,"") for str_pun in pun])
    doc1 = doc1.strip()
    stop_word_lst = []
    from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
    from spacy.lang.en.stop_words import STOP_WORDS
    stop_word_lst.extend(ENGLISH_STOP_WORDS)
    stop_word_lst.extend(list(STOP_WORDS))
    stop_word_lst = list(set(stop_word_lst))
    tokens = word_tokenize(doc1)
    doc1 = [i for i in tokens if not i in stop_word_lst]
    
    #from nltk.stem import PorterStemmer
    #stemmer= PorterStemmer()
    #doc1 =[stemmer.stem(word) for word in doc1]
    
    from nltk.stem import WordNetLemmatizer
    lemmatizer=WordNetLemmatizer()
    doc1 =' '.join([lemmatizer.lemmatize(word) for word in doc1])
    
    doc1 = BeautifulSoup(doc1, "lxml").text
    #
    #from textblob import TextBlob
    #doc1 = TextBlob(doc1)
    ##print(doc1.tags)
    
    #reg_exp = "NP: {<DT>?<JJ>*<NN>}"
    #rp = nltk.RegexpParser(reg_exp)
    #doc1 = rp.parse(doc1.tags)
    #
    #from nltk import word_tokenize, pos_tag, ne_chunk
    #print(ne_chunk(pos_tag(word_tokenize(doc1))))
    ##print(doc1)
    #    
    return doc1