import os

from config import HTTP_PORT, OUTPUT_DIR
from state import make_events
from threads.recorder import RecorderThread
from threads.preview import PreviewThread
from threads.depth import DepthThread
from threads.http_server import HttpServerThread
# from threads.inference import InferenceThread  # Phase 2


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    recording_event, shutdown_event = make_events()

    threads = [
        RecorderThread(recording_event, shutdown_event),
        PreviewThread(recording_event, shutdown_event),
        DepthThread(recording_event, shutdown_event),
        HttpServerThread(recording_event, shutdown_event),
        # InferenceThread(recording_event, shutdown_event),  # Phase 2
    ]

    for t in threads:
        t.start()

    print(f"System ready, HTTP on :{HTTP_PORT}", flush=True)

    try:
        shutdown_event.wait()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
