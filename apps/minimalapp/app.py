from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    flash,
)

app = Flask(__name__)
# SECRET_KEYを追加
app.config["SELECT_KEY"] = ""


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook!"


# Endpoint : URIと紐づけられた関数名または関数につけた名前
@app.route(
    "/hello/<name>",
    methods=["GET", "POST"],
    endpoint="hello-endpoint",
)
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


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # メールを送る
        # form属性を使ってPOSTされたフォームの値を取得する
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        # 入力チェック
        is_valid = True

        if not username:
            flash("ユーザー名は必須です")
            is_valid = False

        if not email:
            flash("メールアドレスは必須です")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("メールアドレスの形式で入力してください")
            is_valid = False

        if not description:
            flash("お問い合わせ内容は必必須です")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        # メールを送る

        # contactエンドポイントへリダイレクトする
        return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
