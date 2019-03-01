from evaluation.loader import load_squad_triples
from evaluation.metrics import bleu_corpus

import spacy

if __name__ == "__main__":
    nlp = spacy.load('en')

    dataset = load_squad_triples('../data/', test=True)

    q_gold = []
    q_pred = []

    for example in dataset:
        doc = nlp(example[0])
        for sent in doc.sents:
            if sent.start_char <= example[3] and sent.end_char > example[3] + len(example[2]):
                q_pred.append(sent.text)
                q_gold.append(example[1])
                break

        
    
    print(bleu_corpus(q_gold, q_pred))