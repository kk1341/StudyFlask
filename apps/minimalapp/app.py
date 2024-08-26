from flask import Flask, render_template

app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


# Endpoint : URIと紐づけられた関数名または関数につけた名前
@app.route("/hello/<name>",
           methods=['GET', 'POST'],
           endpoint="hello-endpoint",)
def hello():
    return "Hello, World!"


# show_nameエンドポイントを作る
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html", name=name)
