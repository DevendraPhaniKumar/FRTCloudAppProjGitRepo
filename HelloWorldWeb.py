from flask import Flask
app = Flask(__name__)

@app.route('/https://frtcloudappproject.azurewebsites.py')

def hello():
    return "Hello World!\n"