from fastapi import FastAPI
from routers.approuter import app_router
from routers.realstaterouter import real_state_router

app = FastAPI()
app.include_router(app_router)
app.include_router(real_state_router)
