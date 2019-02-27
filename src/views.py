from flask import render_template


def squad_board():
    return render_template('board.htm')

def submit_form():
    return render_template('submit_form.htm')