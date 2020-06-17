from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, bcrypt, login_required
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

@app.route("/auth/signup/", methods = ["GET", "POST"])
def signup_form():
    if request.method == "GET":
        return render_template("auth/new.html", form = UserForm())

    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    found_user = User.query.filter_by(username = form.username.data).first()
    if found_user:
        return render_template("auth/new.html", form = form,
                               error = "Username already exists")

    if form.password.data != form.repassword.data:
        return render_template("auth/new.html", form = form,
                               error = "Passwords doesn't match")

    new_user = User(form.username.data, form.password.data)
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(url_for("index"))

@app.route("/users", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    return render_template("auth/list.html", users = User.query.all())

@app.route("/profile/<user_id>", methods=["GET", "POST"])
@login_required
def user_profile(user_id):
    if request.method == "GET":
        return render_template("auth/profile.html", user = User.query.get(current_user.id),
        count = User.task_count(user_id))