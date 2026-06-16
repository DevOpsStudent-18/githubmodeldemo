from flask import Flask, request, jsonify
from tasks import TaskManager

app = Flask(__name__)

task_manager = TaskManager()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(task_manager.tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json

    title = data["title"]

    task_manager.add_task(title)

    return jsonify({"message": "Task created"}), 201

if __name__ == "__main__":
    app.run(debug=True)
