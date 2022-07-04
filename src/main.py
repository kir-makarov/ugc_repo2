import motor.motor_asyncio
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from src.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/ugc/docs',
    openapi_url='/ugc/openapi.json',
)


@app.on_event("startup")
async def startup_event():
    app.mongo = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_CONNECT_URI)[settings.MONGO_DB_NAME]



