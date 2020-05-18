from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks= Task.query.all())

@app.route("/tasks/create/")
def tasks_form():
    return render_template("tasks/create.html", form = TaskForm())

@app.route("/tasks/<task_id>/", methods=["POST"])
def activate_task(task_id):

    t = Task.query.get(task_id)
    t.active = True
    t.state = "In progress"
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/complete/<task_id>/", methods=["POST"])
def complete_task(task_id):

    t = Task.query.get(task_id)
    t.active = False
    t.state = "Completed"
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
def create_tasks():
    form = TaskForm(request.form)

    t = Task(form.name.data, form.description.data)

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/delete/<task_id>/", methods=["POST"])
def delete_task(task_id):

    t = Task.query.get(task_id)
    
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))
