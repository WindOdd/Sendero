import threading

from flask import Flask, jsonify

from config import HTTP_HOST, HTTP_PORT

app = Flask(__name__)

_recording_event: threading.Event = None


def _state():
    return "recording" if _recording_event.is_set() else "idle"


@app.route("/start", methods=["POST"])
def start():
    _recording_event.set()
    return jsonify(status=_state())


@app.route("/stop", methods=["POST"])
def stop():
    _recording_event.clear()
    return jsonify(status=_state())


@app.route("/status", methods=["GET"])
def status():
    return jsonify(status=_state())


class HttpServerThread(threading.Thread):
    def __init__(self, recording_event: threading.Event, shutdown_event: threading.Event):
        super().__init__(name="HttpServer", daemon=True)
        global _recording_event
        _recording_event = recording_event

    def run(self):
        app.run(host=HTTP_HOST, port=HTTP_PORT, threaded=True)
