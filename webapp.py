from flask import Flask, redirect, url_for, session, request, jsonify, Markup
from flask import render_template

app = Flask(__name__)

app.debug = True #Change this to False for production

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/test')
def test():
    return Markup('<h2>Updated Div 1</h2><p>This is the updated content from the server.</p>')

if __name__ == '__main__':
    app.run()
