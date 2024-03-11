from fastapi import FastAPI
from pydantic import BaseModel
from routers import depos

app = FastAPI()

app.include_router(depos.router)

@app.get("/")
async def root():
    return {"message": "Cool Stuff!!"}