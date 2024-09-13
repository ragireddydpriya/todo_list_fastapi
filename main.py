from fastapi import FastAPI
from models import Task

app = FastAPI()

tasks = []

@app.get("/tasks/")
def get_tasks():
    return tasks
    # return 'This is task'

@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task created successfully"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks[i] = task.dict()
            return {"message": "Task updated successfully"}
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}