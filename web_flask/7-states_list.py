#!/usr/bin/python3
"""Script to start a Flask web application"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states_list')
def state_list():
    states = storage.all('State')
    return render_template('7-states_list.html', state=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
