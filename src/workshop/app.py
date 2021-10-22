from fastapi import FastAPI
from workshop.api.operations import router


app = FastAPI()
app.include_router(router)
