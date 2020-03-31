import os
import re
import string
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords


# Function to load documents into memory
def load_doc(filename):
    """
    Parameters:
    filename: a filename

    Return:
    text: a loaded text
    """
    # Open the file as read only
    file = open(filename, 'r')
    # Read all text
    text = file.read()
    # Close the file
    file.close()
    return text


# Function to clean up a loaded document
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


# Function to load documents and add to vocabulary
def add_doc_to_vocab(filename, vocab):
    """
    Parameters:
    filename: A document filename
    Vocab: Counter vocabulary

    Return:
    Counter update
    """
    # load document
    document = load_doc(filename)
    # clean document
    tokens = clean_doc(document)
    # Update counter
    vocab.update(tokens)


# Function to load all documents in a directory
def process_docs(directory, vocab):
    """
    Parameters:
    directory: A directory containing all documents of a class
    vocab: Counter vocabulary

    Return:
    Vocabulary counter update
    """
    for filename in os.listdir(directory):
        # if not filename.endswith('.txt'):
        #     next
        if filename.startswith('cv9'):
            continue
        # create the full path of the file to open
        path = directory + '/' + filename
        # add document to vocabulary
        add_doc_to_vocab(path, vocab)


# Function to truncate vocabulary
def remove_min(occurrence, vocab):
    """
    Parameters:
    occurrence: a minimum occurrence threshold
    vocab: cleaned vocabulary"""
    # Keep tokens with > 5 occurrence
    tokens = [i for i, j in vocab.items() if j >= occurrence]
    return tokens


# Function to save final vocabulary
def save_list(lines, filename):
    """
    Parameters:
    lines:
    filename: Filename to save data to.

    """
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()
    print('Done saving vocabulary to %s ...' % filename)


def create_tokenizer(lines):
    """

    :param lines: cleaned out text for a class
    :return: The tokenizer used to fit on texts.
    """
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer
