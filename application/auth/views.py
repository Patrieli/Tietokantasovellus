from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username = form.username.data).first()
    if user:
        validated = bcrypt.check_password_hash(user.password, form.password.data)
        if validated:
            login_user(user)
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Invalid username or password")
                               
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/signup", methods = ["GET", "POST"])    
def auth_sign_up():
    if request.method == "GET":
        return render_template("auth/new.html", form = UserForm())

    form = UserForm(request.form)
   
    new_user = User(form.username.data, form.password.data)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("index"))