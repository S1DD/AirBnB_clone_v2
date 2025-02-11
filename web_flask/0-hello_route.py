#!/usr/bin/python3

"""Starts a flask application

   The app listens on 0.0.0.0 on port 5000
   Routes: 
          /: Displays 'Hello HBNB!'
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays Hello HNBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
