from fastapi import FastAPI
from logic_ai import start
app = FastAPI()

@app.get("/")
async def root():
    return{"Hello":"world"}
@app.get("/device")
async def device():
    result = start()
    return result
