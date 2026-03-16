from observer.observer import get_message_by_id
from check_status.config import HOST, PORT
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/message_status")
def get_message_status(message_id: str):
    return get_message_by_id(message_id)


def start_server():
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    print("start")
    start_server()
