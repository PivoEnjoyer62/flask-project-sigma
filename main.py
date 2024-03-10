from flask import Flask, render_template, request, redirect, url_for
from sqlmanager import SQLManager

app = Flask(__name__)
db = SQLManager("krutoj")
db.create_tables()


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        nickname = request.form["nickname-input"]
        email = request.form["email-input"]
        password = request.form["password-input"]
        print(f"Nickname: {nickname};\nE-mail: {email};\nPassword: {password}.\n")
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
