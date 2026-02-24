from fastapi import FastAPI
from app.routes.automation import router as automation_router
from app.routes.insights import router as insights_router

app = FastAPI(title="GHUSUN AI Server")

app.include_router(automation_router)
app.include_router(insights_router)