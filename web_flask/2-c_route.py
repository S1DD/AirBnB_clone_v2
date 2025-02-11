#!/usr/bin/python3

"""Starts a Flask web app
   
   Listens on 0.0.0.0 on port 5000
   
   Routes: 
          /: display “Hello HBNB!”
          /hbnb: display “HBNB”
          /c/<text>: display “C ” followed by the value of the text variable 
                     (replace underscore _ symbols with a space )
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
"""Displays HBNB"""
def display_hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
"""Displays C followed by the value of text"""
def display_c():
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
