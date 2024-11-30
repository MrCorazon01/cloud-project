from fastapi import FastAPI
from app.routers import health

app = FastAPI()

# Include routers
app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my Python Lab API!"}