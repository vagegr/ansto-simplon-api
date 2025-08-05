from fastapi import APIRouter

from ...schemas.status import stream_status

router = APIRouter(prefix="/stream/api/1.8.0/status", tags=["Stream Status"])

@router.get("/dropped")
async def get_stream_dropped():
    return {"value": stream_status.dropped}


@router.get("/state")
async def get_stream_state():
    return {"value": stream_status.state}


### Stream subsystem status
# dropped
# state
