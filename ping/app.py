#!/usr/bin/env python
from flask import Flask
import socket
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    response = requests.get("http://pong:6000/books").json()
    return f"your request served by {socket.gethostname()} and remote host {response}"


app.run(host="0.0.0.0", port=5000)
