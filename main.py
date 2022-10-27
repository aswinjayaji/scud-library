from fastapi import FastAPI
app = FastAPI()

from routes import router as StudentRouter
@app.get('/')
async def Home():
    return "welcome home"
