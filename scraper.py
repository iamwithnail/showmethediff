__author__ = 'chris'
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

DATABASE = '/tmp/smtd.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_envvar('SMTD_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])




if __name__ == '__main__':
    app.run()
