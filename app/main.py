from fastapi import FastAPI
from app.routers import health, items

app = FastAPI()

# Ajouter les routeurs
app.include_router(health.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Bienvenue dans mon API FastAPI !"}
