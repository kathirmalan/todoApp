import logging

from fastapi import HTTPException, status
from sqlmodel import Session, select
from db import engine
from models.tasks import Task


async def create_task(task: Task):
    try:
        print(task)
        with Session(engine) as session:
            session.add(task)
            session.commit()
            session.refresh(task)
        return task
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error")


async def read_tasks():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks


async def read_task_by_id(id: int) -> Task:
    with Session(engine) as session:
        statement = select(Task).where(Task.id == id)
        task = session.exec(statement).one()
        return task
