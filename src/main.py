import motor.motor_asyncio
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from api.v1.ugc import ugc_route
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/ugc/docs',
    openapi_url='/ugc/openapi.json',
)
app.include_router(ugc_route, prefix="api/v1/")


@app.on_event("startup")
async def startup_event():
    app.mongo = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_CONNECT_URI)[settings.MONGO_DB_NAME]
