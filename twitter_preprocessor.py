"""
Tweets Preprocessor
"""
import os
import zipfile
from nltk import re
from nltk.tokenize import TweetTokenizer

# load GloVe embedding dictionary
EMB_DIC = {}

ROOT_PATH = os.getcwd()
ARCHIVE_PATH = os.path.join(ROOT_PATH, "glove.twitter.27B.zip")
INSIDE_PATH = "glove.twitter.27B/glove.twitter.27B.25d.txt"

if ".zip" in ARCHIVE_PATH:
    ARCHIVE = zipfile.ZipFile(ARCHIVE_PATH, "r")
    EMBEDDINGS = ARCHIVE.read(INSIDE_PATH).decode("utf8").split("\n")
else:
    EMBEDDINGS = open(ARCHIVE_PATH, "r", encoding='utf8').read().split("\n")

for index, row in enumerate(EMBEDDINGS):
    split = row.split(" ")
    if index >= 50000:
        pass
    EMB_DIC[split[0]] = index + 1

EMB_DIC.pop('<unknown>', None)
EMB_DIC.pop('<unk>', None)
EMB_DIC['<pad>'] = 0
EMB_DIC['<unknown>'] = 1

# GLOVE_DIM = 25
# ROOT_PATH = os.getcwd()
# GLOVE_FILE = '/glove.twitter.27B/glove.twitter.27B.' + str(GLOVE_DIM) + 'd.txt'
# EMB_INDEX = {}
# GLOVE = open(ROOT_PATH+GLOVE_FILE)
# for row, value in enumerate(GLOVE):
#     word = value.split('\n')[0]
#     EMB_INDEX[word] = row
# GLOVE.close()

class TwitterPreprocessor:
    """define twitter preprocessor Class"""

    # - dunder function -
    def __init__(self, text: str, max_length_tweet=20, max_length_dictionary=5000):
        self.text = text
        self.max_length_tweet = max_length_tweet
        self.max_length_dictionary = max_length_dictionary

    # - supporting functions -
    def remove_url(self):
        """remove urls"""
        pattern = re.compile(r'https?:\/\/[A-Za-z0-9\/\.\-\#]*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def remove_hashtag(self):
        """remove hashtags"""
        pattern = re.compile(r'#\w*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def remove_mentions(self):
        """remove @ mentions"""
        pattern = re.compile(r'@\w*')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def remove_twitter_handle(self):
        """remove twitter handles"""
        pattern = re.compile(r'RT')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def remove_numbers(self):
        """remove any numbers"""
        pattern = re.compile(r'[0-9]+')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def remove_punctuation(self):
        """remove any punctutations"""
        pattern = re.compile(r'[^\w\s]')
        self.text = re.sub(pattern=pattern, repl='', string=self.text)
        return self

    def lower(self):
        """lower text"""
        self.text = self.text.lower()
        return self

    def strip(self):
        """strip text"""
        self.text = self.text.strip()
        return self

    # - twitter preprocessor main methods -
    def clean_text(self):
        """cleaning the raw text"""
        return self\
            .remove_url()\
            .remove_hashtag()\
            .remove_mentions()\
            .remove_twitter_handle()\
            .remove_numbers()\
            .remove_punctuation()\
            .lower()\
            .strip()

    def tokenize_text(self):
        """converting a string into an array of tokens"""
        tknzr = TweetTokenizer()
        self.text = tknzr.tokenize(self.text)
        return self

    def replace_token_with_index(self):
        """replacing tokens with index"""
        emb_index = dict(list(EMB_DIC.items())[:self.max_length_dictionary])
        for i in range(len(self.text)):
            self.text[i] = emb_index[self.text[i]]
        return self

    def pad_sequence(self):
        """padding a list of indices with 0 until a maximum length"""
        max_length_tweet = self.max_length_tweet
        if len(self.text) < max_length_tweet:
            self.text.extend([0] * (max_length_tweet - len(self.text)))
        elif len(self.text) >= max_length_tweet:
            self.text = self.text[0:max_length_tweet]
        return self

    def preprocessing(self):
        """run the preprocessing end to end"""
        return self.clean_text().tokenize_text().replace_token_with_index().pad_sequence()
