from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.router import task_routes
from src.user.router import user_routes

# from src.tasks.models import TaskModel

Base.metadata.create_all(engine)


app= FastAPI(title="Task_Management_Application")
app.include_router(task_routes)
app.include_router(user_routes)