import custom2 as cl
from collections import Counter


if __name__ == '__main__':
    occur = int(input('input an occurence value: '))
    vocab = Counter()
    cl.process_docs('/home/michael/Documents/Programming#/txt_sentoken/neg', vocab)
    cl.process_docs('/home/michael/Documents/Programming#/txt_sentoken/pos', vocab)
    tokens = cl.occurence(vocab, occur)
    path = 'vocab_'+ str(len(tokens))+'.txt'
    cl.save_list(tokens, path)
    print(len(tokens))
    print('All documents loaded and vocab created, saved as %s'%(path))
