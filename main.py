from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.database import init_db
from app.routes.legend_routes import router as legend_router
from scripts.wait_for_db import wait_for_db

app = FastAPI()

# CORS configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    wait_for_db()
    init_db()


app.include_router(legend_router)