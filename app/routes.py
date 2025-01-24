from app import app, db
from app.models import Todo
from flask import render_template, redirect, request, url_for

@app.route("/")
def home():
    todos = Todo.query.all()
    return render_template("index.html", todos = todos)

@app.route("/add", methods = ["POST"])
def add():
    title = request.form.get('title')
    if(title):
        new_todo = Todo(title = title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('home'))