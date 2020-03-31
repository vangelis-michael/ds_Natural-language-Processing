# import modules as in  text_prep.py
# load_doc() function
# clean_doc() function
# save_list() function
from text_prep import *


# Function to load document, clean it and return line of tokens
def doc_to_line(filename, vocab):
    """
    Parameters:
    filename: A document filename
    vocab: Counter vocabulary (a set)

    Return:
    Counter update
    """
    # load document
    document = load_doc(filename)
    # clean document (tokenize)
    tokens = clean_doc(document)
    # filter by vocab
    tokens = [w for w in tokens if w in vocab]
    return ' '.join(tokens)


# Function to load all documents in a directory
# Load all docs in a directory
def process_docs_full(directory, vocab, is_train):
    """
    Parameters:
    directory: a directory to traverse
    vocab: set of vocabularies

    Return:
    lines: cleaned and straightened documents from a directory"""
    lines = list()
    # walkthrough all files in the folder
    for filename in os.listdir(directory):
        # Skip files that do not have the right extension
        # if not filename.endswith('.txt'):
        #     next
        if is_train and filename.startswith('cv9'):
            continue
        if not is_train and not filename.startswith('cv9'):
            continue
        # create the full path of the file to open
        path = directory + '/' + filename
        # Load and clean the doc
        line = doc_to_line(path, vocab)
        # Add to list
        lines.append(line)
    return lines
