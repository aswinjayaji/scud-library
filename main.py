from fastapi import FastAPI
app = FastAPI()

from routes import router as BookRouter
app.include_router(BookRouter, tags=["lib"], prefix="/lib")

@app.get('/')
async def Home():
    return "welcome home"
