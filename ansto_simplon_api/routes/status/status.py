from fastapi import APIRouter

from ...schemas.status import detector_state

import logging

router = APIRouter(prefix="/detector/api/1.8.0/status", tags=["Detector Status"])


@router.get("/state")
def get_detector_state():
    logging.info(f"Returning status: {detector_state.state}")
    return {"value": detector_state.state}
