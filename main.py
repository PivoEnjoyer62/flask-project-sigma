from flask import Flask, render_template, request, redirect, url_for
from sqlmanager import SQLManager

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/articles')
def articles():
    db = SQLManager("krutoj")
    articles = db.select_articles()
    return render_template("articles.html", articles=articles)


@app.route('/create-article', methods=["GET", "POST"])
def create_articles():
    if request.method == "GET":
        return render_template("create_article.html")
    if request.method == "POST":
        db = SQLManager('krutoj')
        db.create_articles_table()
        title = request.form["title-input"]
        text = request.form["text-input"]
        db.insert_articles(title, text)
        return redirect(url_for("create_articles"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        db = SQLManager("krutoj")
        email = request.form["email-input"]
        password = request.form["password-input"]
        data = db.login_selection(email, password)
        print(data)
        if data is None:
            return render_template("login.html")
        if data[0] == email and data[1] == password:
            return redirect(url_for("main"))

        return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        db = SQLManager("krutoj")
        nickname = request.form["nickname-input"]
        email = request.form["email-input"]
        password = request.form["password-input"]
        db.register_insertion(nickname, email, password)
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
