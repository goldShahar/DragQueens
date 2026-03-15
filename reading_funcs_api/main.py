from routers import postgers_reading
from reading_funcs_api.config import host, port
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def start_server():
    uvicorn.run(app, host=host, port=port)


def include_routers():
    app.include_router(postgers_reading.router)


if __name__ == "__main__":
    include_routers()
    start_server()
