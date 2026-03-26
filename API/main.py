from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola mundo desde FastAPI"

@app.get("/url")
async def url():
    return {"url": "https://www.emmanuel.dev"}