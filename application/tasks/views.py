from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager
from datetime import datetime

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm, TaskEditForm
from application.label.models import Label

@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.filter_by(user_id = current_user.id),
    current_date=datetime.now(),
    count=Task.count_all_tasks(current_user.id))

@app.route("/tasks/create/")
@login_required
def tasks_form():
    return render_template("tasks/create.html", form = TaskForm())

@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def activate_task(task_id):

    t = Task.query.get(task_id)
    t.active = True
    t.state = "In progress"
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/complete/<task_id>/", methods=["POST"])
@login_required
def complete_task(task_id):

    t = Task.query.get(task_id)
    t.active = False
    t.state = "Completed"
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required
def create_tasks():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("tasks/create.html", form = form)

    t = Task(form.name.data, form.description.data, form.deadline.data)
    t.user_id = current_user.id

    labels = form.labels.data.split(",")
    for l in labels:
        t.labels.append(Label(l.strip()))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/delete/<task_id>/", methods=["GET", "POST"])
@login_required
def delete_task(task_id):

    t = Task.query.get(task_id)
    
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/archive/<task_id>/", methods=["POST"])
@login_required
def archive_task(task_id):

    t = Task.query.get(task_id)
    t.archived = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/archived", methods=["GET"])
@login_required
def tasks_archived():
    return render_template("tasks/archived.html", tasks = Task.query.filter_by(user_id = current_user.id).filter(Task.archived == True),
    count=Task.count_all_tasks(current_user.id))

@app.route("/tasks/edit/<task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):
    if request.method == "GET":
        return render_template("tasks/edit.html", form = TaskEditForm(),
        task = Task.query.get(task_id))

    form = TaskEditForm(request.form)

    if not form.validate():
        return render_template("tasks/edit.html", form = form,
        task = Task.query.get(task_id))

    task = Task.query.get(task_id)

    task.name = form.name.data
    task.description = form.description.data
    task.deadline = form.deadline.data
    task.status = form.status.data

    labels = form.labels.data.split(",")
    task.labels = []
    for l in labels:
        task.labels.append(Label(l.strip()))

    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/list", methods=["GET"])
@login_required
def list_tasks():
    return render_template("tasks/users_tasks.html",
    current_date=datetime.now(),
    users_tasks=Task.users_tasks(current_user.id))