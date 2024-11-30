import os
from fastapi import FastAPI
from app.server.routers import health, items
from app.server.database import init_db
import uvicorn

app = FastAPI()

# Initialize the database when the app starts
@app.on_event("startup")
async def startup():
    await init_db()

# Include routers
app.include_router(health.router)
app.include_router(items.router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my Python Lab API!"}

if __name__ == "__main__":
    # Get the port from environment variable, defaulting to 8080
    port = int(os.getenv("PORT", 8080))  # Cloud Run définit automatiquement le port
    uvicorn.run(app, host="0.0.0.0", port=port)
