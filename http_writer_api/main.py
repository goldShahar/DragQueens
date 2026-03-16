from http_writer_api.routers import hazard, type
from config import HTTP_HOST, HTTP_PORT
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def start_server():
    uvicorn.run(app, host=HTTP_HOST, port=HTTP_PORT)


def include_routers():
    app.include_router(type.router)
    app.include_router(hazard.router)


if __name__ == "__main__":
    include_routers()
    start_server()
