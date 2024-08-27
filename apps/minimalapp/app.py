from flask import Flask, render_template, url_for, request, redirect

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=['GET', "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
