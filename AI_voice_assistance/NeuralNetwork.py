import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()

def tokenize(sentence):
    return word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, word_list):
    text_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(word_list), dtype=np.float32)
    
    #stam_word_list=[stem(word) for word in word_list]
    for index, w in enumerate(word_list):
        if w in text_word:
            bag[index] = 1
    
    return bag