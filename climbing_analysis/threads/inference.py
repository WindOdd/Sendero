import threading

# Phase 2: load TensorRT engine, consume frames from Queue, emit JSON skeleton.
# NOT started in Phase 1.


class InferenceThread(threading.Thread):
    def __init__(self, recording_event: threading.Event, shutdown_event: threading.Event):
        super().__init__(name="Inference", daemon=True)
        self._recording = recording_event
        self._shutdown = shutdown_event

    def run(self):
        pass
