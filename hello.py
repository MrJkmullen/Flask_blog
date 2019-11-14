from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/projects')
def projects_page():
    return 'Hello, World!'    