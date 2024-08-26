from flask import Flask, render_template, url_for, current_app, g

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


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/fukuhara?page=1
    print(url_for("show_name", name="fukuhara", page="1"))


# アプリケーションコンテキストを取得してスタックへpushする
ctx = app.app_context()
ctx.push()

# current_appにアクセスが可能になる
print(current_app)
# >> apps.minimalapp.app

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)