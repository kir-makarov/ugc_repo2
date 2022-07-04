import motor.motor_asyncio
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

from api.v1.ugc import ugc_route
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url='/ugc/docs',
    openapi_url='/ugc/openapi.json',
)
app.include_router(ugc_route, prefix="/api/v1")


@app.on_event("startup")
async def startup_event():
    app.mongo = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_CONNECT_URI)[settings.MONGO_DB_NAME]

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
