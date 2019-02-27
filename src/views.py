from flask import render_template

import json, os

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
PROJECT_DIR = os.path.dirname(CURRENT_DIR)

def squad_board():

    with open(PROJECT_DIR+'/data/scores.json') as fp:
        scores = json.load(fp)

    ranked = [{ **x, 'rank': ix+1} for ix, x in enumerate(sorted(scores, key=lambda x: x['bleu_score'], reverse=True))]

    return render_template('board.htm', scores=ranked, title="Du et al 2017 split of SQuAD")

def submit_form():
    return render_template('submit_form.htm')