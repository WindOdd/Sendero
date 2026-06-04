import threading


def make_events():
    """Return (recording_event, shutdown_event)."""
    return threading.Event(), threading.Event()
