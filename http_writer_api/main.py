from routers import hazard, type
from config import HOST, PORT
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def start_server():
    uvicorn.run(app, host=HOST, port=PORT)


def include_routers():
    app.include_router(type.router)
    app.include_router(hazard.router)


if __name__ == "__main__":
    include_routers()
    start_server()
