 #!/usr/bin/python3
"""starts a Flask web application
    
   Routes:
          /: display “Hello HBNB!”
          /hbnb: display “HBNB”
"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB"

@app.route("/", strict_slashes=False)
def display_hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
