from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="API/static"), name="static")

@app.get("/")
async def root():
    return "Hola mundo desde FastAPI"

@app.get("/url")
async def url():
    return {"url": "https://www.emmanuel.dev"}