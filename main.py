import sys
import logging
from logging.handlers import RotatingFileHandler
import uvicorn
from fastapi import FastAPI
from routers.tasks import router as task_router


def log_configuration():
    logging.basicConfig(
        handlers=[
            RotatingFileHandler(
                "{log_dir}.log".format(log_dir="/Users/kathirmalan/Projects/log/todoApp/todoapp"),
                maxBytes=500000,
                backupCount=30,
            )
        ],
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    )


def include_app_routes(application):
    application.include_router(task_router)


def create_app():
    application = FastAPI(
        title="Simple Todo App",
        description="Simple Todo App by Kathirmalan",
        version="0.1"
    )
    try:
        log_configuration()
    except FileNotFoundError:
        print("Logger file configuration failed")
        sys.exit()

    @application.get('/')
    async def root_route():
        return {"message": "Hello world"}

    include_app_routes(application)

    return application


# Initialize FastApi App
application = create_app()

if __name__ == "__main__":
    logging.info("Application started on port 5001")
    uvicorn.run("main:application", host="0.0.0.0", port=5001, reload=True)

