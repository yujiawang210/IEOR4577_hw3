# ------ Import Required Libraries ------
import os
import string
import numpy as np
from nltk import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer


# ------ GloVe embedding dictionary ------
glove_dim = 100  
root_path = os.getcwd()
glove_file = '/glove.twitter.27B/glove.twitter.27B.' + str(glove_dim) + 'd.txt'

emb_index = {}
glove = open(root_path+glove_file)
for row, line in enumerate(glove):
    values = line.split()
    word = values[0]
    emb_index[word] = row
glove.close()


# ------ Define TwitterPreprocessor Class ------
class TwitterPreprocessor:
    
    # - dunder function -
    def __init__(self, text:str, max_length_tweet=30, max_length_dictionary=1000):
        self.text = text
        self.max_length_tweet = max_length_tweet
        self.max_length_dictionary = max_length_dictionary
    
    # - supporting functions -
    def remove_url(self):
        pattern = re.compile(r'https?:\/\/[A-Za-z0-9\/\.\-\#]*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
        
    def remove_hashtag(self):
        pattern = re.compile(r'#\w*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
    
    def remove_mentions(self):
        pattern = re.compile(r'@\w*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
    
    def remove_twitter_handle(self):
        pattern = re.compile(r'RT')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
    
    def remove_numbers(self):
        pattern = re.compile(r'[0-9]+')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
        
    def remove_punctuation(self):
        pattern = re.compile(r'[^\w\s]')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self
        
    def lower(self):
        self.text = self.text.lower()
        return self
    
    # - twitter preprocessor main methods -
    def clean_text(self):
        return self\
            .remove_url()\
            .remove_hashtag()\
            .remove_mentions()\
            .remove_twitter_handle()\
            .remove_numbers()\
            .remove_punctuation()\
            .lower()

    def tokenize_text(self):
        tknzr = TweetTokenizer()
        self.text = tknzr.tokenize(self.text)
        return self
    
    def replace_token_with_index(self):
        for i in range(len(self.text)):
            self.text[i] = emb_index[self.text[i]]
        return self
    
    def pad_sequence(self):
        max_length_tweet = self.max_length_tweet
        if len(self.text) < max_length_tweet:
            self.text.extend([0] * (max_length_tweet - len(self.text)))
        elif len(self.text) >= max_length_tweet:
            self.text = self.text[0:max_length_tweet]
        return self