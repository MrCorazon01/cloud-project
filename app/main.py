from fastapi import FastAPI
from app.routers import health, items
from app.database import init_db

app = FastAPI()

# Initialize the database when the app starts
@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(health.router)
app.include_router(items.router)

# Root endpoint
# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my Python Lab API!"}