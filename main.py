from flask import Flask, render_template, request, redirect, url_for, session
from sqlmanager import SQLManager

app = Flask(__name__)
app.secret_key = "SIGMAKRUTOJ34567890987654"


@app.route('/')
def main():
    return render_template("main.html", is_logged_in=session.get("is_logged_in", False))


@app.route('/articles')
def articles():
    db = SQLManager("krutoj")
    articles = db.select_articles()
    return render_template("articles.html", articles=articles, is_logged_in=session.get("is_logged_in", False))


@app.route('/create-article', methods=["GET", "POST"])
def create_articles():
    if request.method == "GET":
        return render_template("create_article.html", is_logged_in=session.get("is_logged_in", False))
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
        if data is None:
            return render_template("login.html")
        if data[0] == email and data[1] == password:
            session["is_logged_in"] = True
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
        session['id'] = None
        return render_template("register.html")


@app.route('/profile')
def profile():

    return render_template("profile.html", is_logged_in=session.get("is_logged_in", False))


if __name__ == "__main__":
    app.run(debug=True)
