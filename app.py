"""
Flask Git Practice App
A simple task tracker to practice Git workflows and CI/CD.
"""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory task store (replace with DB later as practice)
tasks = [
    {"id": 1, "title": "Learn git init & clone", "status": "done", "created": "2026-03-14"},
    {"id": 2, "title": "Practice git add & commit", "status": "in-progress", "created": "2026-03-14"},
    {"id": 3, "title": "Learn branching & merging", "status": "todo", "created": "2026-03-14"},
    {"id": 4, "title": "testing", "status": "added", "created": "2026-03-15"},
]
next_id = 4


@app.route("/")
def index():
    """Home page - shows all tasks."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    """Add a new task."""
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "status": "todo",
            "created": datetime.now().strftime("%Y-%m-%d"),
        })
        next_id += 1
    return redirect(url_for("index"))


@app.route("/update/<int:task_id>", methods=["POST"])
def update_status(task_id):
    """Cycle task status: todo -> in-progress -> done -> todo."""
    cycle = {"todo": "in-progress", "in-progress": "done", "done": "todo"}
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = cycle.get(task["status"], "todo")
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Delete a task."""
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/health")
def health():
    """Health check endpoint for CI/CD pipeline."""
    return jsonify({"status": "healthy", "version": "1.0.1", "tasks_count": len(tasks)})


@app.route("/api/tasks")
def api_tasks():
    """REST API endpoint - useful for testing."""
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
