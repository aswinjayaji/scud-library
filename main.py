from fastapi import FastAPI
app = FastAPI()

from routes import router as BookRouter
app.include_router(BookRouter, tags=["book"], prefix="/book")

@app.get('/')
async def Home():
    return "welcome home"
