from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, We are going to die"

app.run(host='0.0.0.0') 