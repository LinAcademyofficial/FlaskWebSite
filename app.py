# import Libris & Configs
from flask import Flask
form mongokit import Connection, Document
from .config import Development

# create the little application object
app = Flask(__name__)
app.config.from_object(Development)
# connect to the database
connection = Connection(app.config[MONGODB_HOST], app.config[MONGODB_PORT])


@app.route('/')
def hello():
    return 'Hello World!'

