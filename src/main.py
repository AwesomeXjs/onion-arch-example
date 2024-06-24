from fastapi import FastAPI

from infra.controllers.api_v1 import router as v1_router

app = FastAPI(title="Onion architecture")

app.include_router(v1_router)
