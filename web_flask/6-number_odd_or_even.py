#!/usr/bin/python3
'''
Script that starts a Flask web application
'''


from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def ctext(text):
    return "C {}".format(text).replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def iscool(text="is cool"):
    return "Python {}".format(text).replace("_", " ")


@app.route('/number/<int:n>')
def isnumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'

    return render_template(
        '6-number_odd_or_even.html', n=n, odd_or_odd=odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
