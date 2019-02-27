from flask import Flask, render_template
app = Flask(__name__)

from views import squad_board, submit_form

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/about')
def about():
    return render_template('about.htm')

@app.route('/submit')
def submit():
    return submit_form()

@app.route('/squad')
def squad():
    return squad_board()

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)