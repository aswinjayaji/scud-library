from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app = FastAPI()

from routes import router as BookRouter
app.include_router(BookRouter, tags=["lib"], prefix="/lib")

@app.get('/')
async def Home():
    return RedirectResponse("https://scud-library.herokuapp.com/docs")
