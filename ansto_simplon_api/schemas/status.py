from typing import Literal

from pydantic import BaseModel


class DetectorState(BaseModel):
    state: Literal[
        "ready", "initialize", "configure", "acquire", "idle", "test", "error", "na"
    ] = "idle"


detector_state = DetectorState()

class StreamStatus(BaseModel):
    dropped: int = 0
    state: Literal[ "disabled", "ready", "acquire", "error" ] = "ready"

stream_status = StreamStatus()
