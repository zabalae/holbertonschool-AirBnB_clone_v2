#!/usr/bin/python3
'''
Script that starts a Flask web application
'''


if __name__ == "__main__":
    from flask import Flask


    app = Flask(__name__)
    app.url_map.strict_slashes = False


    @app.route('/')
    def index():
        return "Hello HBNB!"


    @app.route('/hbnb')
    def index2():
        return "HBNB"
    app.run(host='0.0.0.0', port=5000)
