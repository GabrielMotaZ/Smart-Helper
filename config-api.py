from fastapi import FastAPI
from pydantic import BaseModel
import datetime

class Configuration(BaseModel):
    alarm: datetime.time
    playlist: str

app = FastAPI

@app.post("/configure")
async def configurationEndPoint(configuration: Configuration):
    return {
        "alarm": configuration.alarm,
        "playlist": configuration.playlist
    }