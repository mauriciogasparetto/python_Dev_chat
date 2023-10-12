# BACKEND

# pip install flask 
# website with the scripts
# pip install python-socketio flask-socketio simple-websocket

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
SocketIO = SocketIO(app, cars_allowed_origins="*")

# message sending functionality
@SocketIO.on("message")
def manage_message(message):
    send(message, broadcast=True)

# CREATE THE FIRST PAGE = FIRST ROUTE
@app.route("/")
def homepage():
    return render_template("homepage.html")

# RUN OUR APPLICATION
SocketIO.run(app, host="localhost")