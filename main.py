from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="DADA-Forest API")

@app.get("/health")
async def health():
    now = datetime.now()

    return {
        "msg": "ok",
        "data": now,
    }