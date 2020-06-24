from flask import Flask, render_template
app = Flask(__name__)

import views

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/about')
def about():
    return render_template('about.htm')

@app.route('/submit')
def submit():
    return views.submit_form()

@app.route('/squad')
def squad():
    return views.squad_board()

@app.route('/squad-zhao')
def squad():
    return views.squadrevdev_board()

@app.route('/newsqa')
def squad():
    return views.newsqa_board()

@app.route('/naturalquestions')
def squad():
    return views.nq_board()

@app.route('/msmarco')
def squad():
    return views.msmarco_board()

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)