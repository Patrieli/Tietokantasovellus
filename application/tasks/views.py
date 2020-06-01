from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager

from application import app, db
from application.tasks.models import Task
from application.tasks.forms import TaskForm
from application.label.models import Label

@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.filter_by(user_id = current_user.id),
    completed=Task.list_all_completed_tasks(current_user.id),
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
        t.labels.append(Label(l))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/delete/<task_id>/", methods=["POST"])
@login_required
def delete_task(task_id):

    t = Task.query.get(task_id)
    
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

