import json

import re
from collections import defaultdict

from nltk.tokenize import TreebankWordTokenizer, sent_tokenize

import numpy as np

SOS = '<Sent>'
EOS = '</Sent>'
PAD='<PAD>'
OOV='<OOV>'

def load_squad_dataset(path, dev=False, test=False, v2=False):
    expected_version = 'v2.0' if v2 else '1.1'
    if v2:
        filename = 'train-v2.0.json' if not dev else 'dev-v2.0.json'
    elif test and not dev:
        filename = 'test-v1.1.json'
    else:
        filename = 'train-v1.1.json' if not dev else 'dev-v1.1.json'
    with open(path+filename) as dataset_file:
        dataset_json = json.load(dataset_file)
        if (dataset_json['version'] != expected_version):
            print('Expected SQuAD v-' + expected_version +
                  ', but got dataset with v-' + dataset_json['version'])
        dataset = dataset_json['data']
        return(dataset)

def load_squad_triples(path, dev=False, test=False, v2=False, as_dict=False, ans_list=False):
    raw_data = load_squad_dataset(path, dev=dev, test=test, v2=v2)
    triples=[] if not as_dict else {}
    for doc in raw_data:
        for para in doc['paragraphs']:
            for qa in para['qas']:
                id = qa['id']
                # NOTE: this only takes the first answer per question! ToDo handle this more intelligently
                if ans_list:
                    ans_text = [a['text'] for a in qa['answers']]
                    ans_pos = [int(a['answer_start']) for a in qa['answers']]
                else:
                    ans_text = qa['answers'][0]['text']
                    ans_pos = int(qa['answers'][0]['answer_start'])
                if v2:
                    if qa['is_impossible']:
                        el = (para['context'], qa['question'], qa['plausible_answers'][0]['text'] if not dev else "", int(qa['plausible_answers'][0]['answer_start']) if not dev else None, True)
                    else:
                        el =  (para['context'], qa['question'], qa['answers'][0]['text'], int(qa['answers'][0]['answer_start']), False)
                else:
                    el =  (para['context'], qa['question'], ans_text, ans_pos)
                if as_dict:
                    triples[id] = el
                else:
                    triples.append(el)
    return triples



if __name__ == "__main__":
    import sys
    sys.path.insert(0, "/Users/tom/Dropbox/msc-ml/project/src/")
    from preprocessing import char_pos_to_word, tokenise
    item = load_squad_dataset('./data/',False)[0]['paragraphs'][0]
    a = item['qas'][0]['answers'][0]
    context = item['context']
    toks = tokenise(context,asbytes=False)
    print(context)
    print(a)
    print(context[a['answer_start']:])
    ans_span=char_pos_to_word(context.encode(), [t.encode() for t in toks], a['answer_start'])
    ans_span=(ans_span, ans_span+len(tokenise(a['text'],asbytes=False)))
    print(toks[ans_span[0]:ans_span[1]])
