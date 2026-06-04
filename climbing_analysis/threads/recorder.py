import threading
import time

from config import RECORDER_INTERVAL, IDLE_POLL


class RecorderThread(threading.Thread):
    def __init__(self, recording_event: threading.Event, shutdown_event: threading.Event):
        super().__init__(name="Recorder", daemon=True)
        self._recording = recording_event
        self._shutdown = shutdown_event

    def run(self):
        frame = 0
        while not self._shutdown.is_set():
            if self._recording.is_set():
                frame += 1
                print(f"[recorder] frame {frame}", flush=True)
                time.sleep(RECORDER_INTERVAL)
            else:
                frame = 0
                time.sleep(IDLE_POLL)
