import sqlite3
import os.path
from flask import Flask, request, g, redirect, url_for, \
                  render_template, flash

DATABASE = os.path.join(os.path.dirname(__file__), 'data.db')
DEBUG = True
SECRET_KEY = 'dfdouererlejdfndlgdf'

app = Flask(__name__)
app.config.from_object(__name__)


def init_db():
    db = get_db()
    with app.open_resource('schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()

def get_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('''SELECT datetime(created, "localtime"),
                          message FROM entries ORDER BY id DESC''')
    entries = [dict(created=row[0], message=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    print request.form['message']
    g.db.execute('INSERT INTO entries (message) VALUES (?)',
                 (request.form['message'],))
    g.db.commit()
    flash("Gracias por tu mensaje! :)")
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    #init_db()
    app.run(host='0.0.0.0', port=80)
