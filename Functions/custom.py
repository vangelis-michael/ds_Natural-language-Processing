import re
import string
import os
from collections import Counter
from nltk.corpus import stopwords


def load_doc(filename):
    if filename==None:
        return 'No file has been selected, please input a valid text file path...'
    else:
        file = open(filename, 'rt')
        text = file.read()
        file.close()
    return text

 
def clean_doc(doc):
    """
    Parameters:
    doc: a loaded document

    Return
    tokens: a cleaned document"""
    # Split into tokens by white space.
    tokens = doc.split()
    # Prepare regex for character filtering.
    re_punctuation = re.compile('[%s]' % re.escape(string.punctuation))
    # remove punctuation from each word.
    tokens = [re_punctuation.sub('', w) for w in tokens]
    # remove remaining non-alphabetic tokens.
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stopwords.
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if w not in stop_words]
    # Filter out short tokens.
    tokens = [word for word in tokens if len(word) > 1]
    return tokens


def add_to_vocab(filename, vocab):
    doc = load_doc(filename)
    tokens = clean_doc(doc)
    vocab.update(tokens)


def process_docs(directory, vocab):
    for filename in os.listdir(directory):
        if not filename.endswith('.txt'):
            next
        path = directory + '/' + filename
        add_to_vocab(path, vocab)


def occurence(vocab, occur=5):
    tokens = [k for k,c in vocab.items() if c >= occur]
    return tokens


def save_list(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()
