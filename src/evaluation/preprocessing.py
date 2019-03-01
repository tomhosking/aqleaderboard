import numpy as np
import string
# import tensorflow as tf

from nltk.tokenize import TreebankWordTokenizer, sent_tokenize
use_nltk = True


def tokenise(text, asbytes=True, append_eos=False):

    text = text.decode() if asbytes else text
    if use_nltk:
        sents = [s for s in sent_tokenize(text)]

        tokens = [tok.lower() for sent in sents for tok in TreebankWordTokenizer().tokenize(sent)]
    else:
        for char in string.punctuation+'()-–':
            text = text.replace(char, ' '+char+' ')
        tokens = text.lower().split(' ')
    tokens = [w.encode() if asbytes else w for w in tokens if w.strip() != '']
    if append_eos:
        tokens.append(EOS.encode() if asbytes else EOS)
    # tokens = np.asarray(tokens)
    # return np.asarray(tokens)
    return tokens
