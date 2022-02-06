from fastapi import FastAPI, Depends
import uvicorn
from config import *


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)