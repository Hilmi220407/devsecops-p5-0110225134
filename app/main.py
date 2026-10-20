from flask import Flask, jsonify, request
from app.models import Task
from app.utils import validate_title

app = Flask(__name__)
tasks = []


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify([t.to_dict() for t in tasks])


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json() or {}
    title = data.get("title", "")
    if not validate_title(title):
        return jsonify({"error": "Judul tidak valid"}), 400
    task = Task(len(tasks) + 1, title.strip())
    tasks.append(task)
    return jsonify(task.to_dict()), 201


@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def finish_task(task_id):
    for t in tasks:
        if t.task_id == task_id:
            t.mark_done()
            return jsonify(t.to_dict())
    return jsonify({"error": "Task tidak ditemukan"}), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)