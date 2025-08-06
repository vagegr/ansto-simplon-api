from fastapi import APIRouter

from ...simulate_zmq_stream import zmq_stream

# Make the commands non-blocking
from threading import Thread

router = APIRouter(prefix="/detector/api/1.8.0/command", tags=["Detector Command"])
# List of running threads
threads_running = []

@router.put("/trigger")
def trigger():
    # zmq_stream.stream_frames(zmq_stream.frames)
    thread = Thread(target=zmq_stream.stream_frames, args=(zmq_stream.frames,))
    thread.start()
    # thread.join()
    threads_running.append(thread)


@router.put("/arm")
def arm():
    zmq_stream.sequence_id += 1
    # Reset the image number every time we arm the detector
    zmq_stream.image_number = 0
    zmq_stream.trigger_number = 0
    zmq_stream.frame_id = 0;
    zmq_stream.stream_start_message()
    return {"sequence id": zmq_stream.sequence_id}


@router.put("/disarm")
def disarm():
    # zmq_stream.stream_end_message()
    nthreads = len(threads_running)
    print("\nThreads running:", nthreads, "..")
    while len(threads_running) > 0:
        thread = threads_running[-1]
        thread.run = False
        thread.join()
        threads_running.pop()
    zmq_stream.stream_end_message()
    print("Disarm detector")

@router.put("/cancel")
def cancel():
    nthreads = len(threads_running)
    print("\nThreads running:", nthreads, "..")
    while len(threads_running) > 0:
        thread = threads_running[-1]
        thread.run = False
        thread.join()
        threads_running.pop()
    zmq_stream.cancel_stream()
    print("Cancel detector")

@router.put("/abort")
def abort():
    nthreads = len(threads_running)
    print("\nThreads running:", nthreads, "..")
    while len(threads_running) > 0:
        thread = threads_running[-1]
        thread.run = False
        thread.join()
        threads_running.pop()
    zmq_stream.abort_stream()
    print("Abort detector")
