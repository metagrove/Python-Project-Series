from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks =[]

class Task(BaseModel):
    id : int
    title :str
    is_done :bool = False

@app.post("/tasks/", status_code=201)
def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created successfully", "task": task}

@app.get("/tasks/", status_code=200)
def get_task():
    return{"message": "Task retrieved successfully", "tasks": tasks}

@app.get("/tasks/{task_id}", status_code=200)
def get_task(task_id:int):
    for task in tasks:
        if task.id == task_id:
            return {"message": "Task retrieved successfully", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", status_code=200)
def update_task(task_id:int,update_task:Task):
    for i,task in enumerate(tasks):
        if task.id == task_id:
            tasks[i]=update_task
            return {"message": "Task updated successfully", "task": update_task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id:int):
    for i,task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"} 
    raise HTTPException(status_code=404, detail="Task not found")