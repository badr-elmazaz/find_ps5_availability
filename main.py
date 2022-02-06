import os
import json

from fastapi import FastAPI, Depends
import uvicorn
from config import *

config_path=os.path.join(os.getcwd(), "config.json")
with open(config_path) as f:
    config = json.loads(f)

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)