from fastapi import APIRouter

real_state_router = APIRouter()


@real_state_router.get("/units")
async def get_units():
    return []
