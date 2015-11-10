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
app.config.from_object(__name__)
#app.config.from_envvar('SMTD_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


from contextlib import closing

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/urls')
def show_url():
    cur = g.db.execute('select title, url from urls order by id desc')
    urls = [dict(title=row[0], url=row[1]) for row in cur.fetchall()]
    return render_template('show_urls.html', urls=urls)

@app.route('/tos')
def show_tos():
    cur = g.db.execute('select title, contents, date_scraped from tos order by id desc')
    tos = [dict(title=row[0], contents=row[1], date_scraped=row[2], url_id=row[3]) for row in cur.fetchall()]
    return render_template('show_tos.html', tos=tos)


@app.route('/addurl', methods=['POST'])
def add_url():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into urls (title, url) values (?, ?)',
                 [request.form['title'], request.form['url']])
    g.db.commit()
    flash('New url was successfully posted')
    return redirect(url_for('show_url'))

@app.route('/addtos', methods=['POST'])
def add_tos():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into tos (title, date_scraped, content, url) values (?, ?, ?, ?)',
                 [request.form['title'],
                  request.form['date_scraped'],
                  request.form['content'],
                  request.form['url']])
    g.db.commit()
    flash('New tos were successfully posted')
    return redirect(url_for('show_tos'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_url'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_url'))


if __name__ == '__main__':
    app.run()
