from flask import Flask

app = Flask(__name__)

# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"

@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"
