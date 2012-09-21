from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html', name='world')

@app.route('/static/<path:filename>')
def static(filename):
    return send_from_directory('/home/xleo/tests/flask-py27/static', filename)

app.debug = True
app.run()
