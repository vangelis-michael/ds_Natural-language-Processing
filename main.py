from collections import Counter
import requests
from save_processed import *
from text_prep import *

if __name__ == '__main__':
    # # Call the url for the specific data
    # url = 'http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'
    # r = requests.get(url, allow_redirects=True)
    # open('Data/review_polarity.tar.gz', 'wb').write(r.content)
    # # Uncompress the file

    # Define a counter vocabulary
    vocab = Counter()
    # Add all docs to vocab
    directory_neg = input('Input your negative review directory: ')  # Data/txt_sentoken/neg
    directory_pos = input('Input your positive review directory: ')  # Data/txt_sentoken/pos
    process_docs(directory_neg, vocab)
    process_docs(directory_pos, vocab)
    # print the size of the vocabulary
    tokens = remove_min(5, vocab)
    print(len(vocab))
    print(len(tokens))
    # Save tokens to a vocab file
    save_list(tokens, 'Data/vocab.txt')

    # load vocabulary from file
    vocab_filename = 'Data/vocab.txt'
    vocab = load_doc(vocab_filename)
    vocab = vocab.split()
    vocab = set(vocab)
    print('Loaded and set vocabulary with length %s...' % len(vocab))

    # Prepare negative reviews
    negative_lines = process_docs_full('Data/txt_sentoken/neg', vocab, is_train=True)
    save_list(negative_lines, 'Data/negative.txt')

    # Prepare positive reviews
    positive_lines = process_docs_full('Data/txt_sentoken/pos', vocab, is_train=True)
    save_list(positive_lines, 'Data/positive.txt')
    print('Number of positives and negatives are %s and %f' % (len(positive_lines), int(len(negative_lines))))
    print('Cleaned and saved both positive and negative reviews to file...')

    # Fix to download the file, unzip and extract the file before loading.
