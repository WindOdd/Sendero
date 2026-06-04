import threading
import time

from config import DEPTH_INTERVAL, IDLE_POLL


class DepthThread(threading.Thread):
    def __init__(self, recording_event: threading.Event, shutdown_event: threading.Event):
        super().__init__(name="Depth", daemon=True)
        self._recording = recording_event
        self._shutdown = shutdown_event

    def run(self):
        frame = 0
        while not self._shutdown.is_set():
            if self._recording.is_set():
                frame += 1
                print(f"[depth] frame {frame}", flush=True)
                time.sleep(DEPTH_INTERVAL)
            else:
                frame = 0
                time.sleep(IDLE_POLL)
