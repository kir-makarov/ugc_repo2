import logging

import motor.motor_asyncio
import uvicorn
from fastapi import FastAPI
from logstash_async.handler import AsynchronousLogstashHandler

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
    app.db = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_CONNECT_URI)[settings.MONGO_DB_NAME]

    uvicorn_logger = logging.getLogger()
    handler = AsynchronousLogstashHandler(
        settings.LOGSTASH_HOST,
        settings.LOGSTASH_PORT,
        transport="logstash_async.transport.UdpTransport",
        database_path="logstash.db",
    )
    uvicorn_logger.addHandler(handler)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
