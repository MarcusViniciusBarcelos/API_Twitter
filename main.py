# main.py
import uvicorn
from fastapi import FastAPI

from src.services import TwitterService

app = FastAPI()
twitter_service = TwitterService()


@app.on_event("startup")
def startup_event():
    twitter_service.save_global_trends_to_mongo()


@app.get("/trends")
def get_trends_route():
    global_trends = twitter_service.get_global_trends()
    return {"trends": global_trends}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
