from app import app, db
from app.models import Todo
from flask import render_template, redirect, request, url_for, jsonify

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

@app.route("/check/<id>", methods=["PUT"])
def check(id):
    todo = Todo.query.get(id)
    if(todo):
        todo.done = not todo.done
        db.session.commit()
        return jsonify({"success": True, "id": id, "done": todo.done}), 200
    return jsonify({"success": False, "message": "Todo not found"}), 404

@app.route("/delete/<id>", methods = ["DELETE"])
def erase(id):
    todo = Todo.query.get(id)
    if(todo):
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("home"))
    return "Todo not found", 404