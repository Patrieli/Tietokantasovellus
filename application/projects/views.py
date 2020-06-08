from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm

@app.route("/projects", methods=["GET"])
@login_required
def projects_index():
    return render_template("projects/list.html", projects = Project.query.filter_by(user_id = current_user.id))

@app.route("/projects/create/")
@login_required
def projects_form():
    return render_template("projects/create.html", form = ProjectForm())

@app.route("/projects/", methods=["POST"])
@login_required
def create_project():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/create.html", form = form)

    t = Project(form.name.data)
    t.user_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("projects_index"))

@app.route("/projects/<project_id>", methods=["GET"])
@login_required
def open_project(project_id):
    return render_template("projects/project.html", project = Project.query.get(project_id))