"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

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
