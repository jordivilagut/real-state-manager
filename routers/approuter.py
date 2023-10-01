from fastapi import APIRouter

app_router = APIRouter()


@app_router.get("/health")
async def health():
    return {
        "name": "real-state-manager",
        "version": "1.0.0"
    }
