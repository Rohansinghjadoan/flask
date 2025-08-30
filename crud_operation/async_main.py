import asyncio
from fastapi import FastAPI
app=FastAPI()

@app.get('/wait')
async def wait():
    await asyncio.sleep(5) ## non blocking sleep
    return {"message":"waited for 5 seconds"}

