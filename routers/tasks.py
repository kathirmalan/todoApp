from fastapi import APIRouter
from crud.tasks import create_task, read_tasks, read_task_by_id
from models.tasks import Task

router = APIRouter(
    tags=['Task']
)


@router.post("/tasks")
async def r_create_task(task: Task):
    add_task_operation = await create_task(task=task)
    print(add_task_operation)
    return add_task_operation


@router.get("/tasks", response_model=list[Task])
async def r_read_tasks():
    return await read_tasks()


@router.get("/tasks/{id}", response_model=Task)
async def r_read_tasks(id: int):
    return await read_task_by_id(id=id)
