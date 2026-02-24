from flask import Flask, render_template, request
from datetime import datetime, timezone
import csv
import os
import socket
import uuid
import time

app = Flask(__name__)

BASE_DIR = os.path.expanduser("~/iot_lab")
LOG_PATH = os.path.join(BASE_DIR, "logs", "actions.csv")

DEVICE_ID = "esp32_led_01"   # placeholder until serial is wired in
SOURCE_HOST = socket.gethostname()

HEADER = [
    "timestamp_utc",
    "event_id",
    "session_id",
    "username",
    "source_host",
    "device_id",
    "action",
    "target",
    "value",
    "result",
    "latency_ms",
    "error"
]

def init_log():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", newline="") as f:
            csv.writer(f).writerow(HEADER)

def log_event(session_id, username, action, target, value, result, latency_ms, error=""):
    init_log()
    ts = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    with open(LOG_PATH, "a", newline="") as f:
        csv.writer(f).writerow([
            ts,
            uuid.uuid4().hex[:8],
            session_id,
            username,
            SOURCE_HOST,
            DEVICE_ID,
            action,
            target,
            value,
            result,
            latency_ms,
            error
        ])

def send_command(cmd: str):
    """
    Placeholder until ESP32 serial is wired in.
    Returns (response_text, latency_ms, success_bool, error_text)
    """
    start = time.time()
    time.sleep(0.05)  # simulate a device round-trip
    latency = int((time.time() - start) * 1000)

    if cmd in ("ON", "OFF", "STATUS"):
        return "OK", latency, True, ""
    return "INVALID", latency, False, "invalid command"

@app.route("/", methods=["GET", "POST"])
def dashboard():
    message = None

    if request.method == "POST":
        cmd = request.form.get("command", "").upper().strip()
        session_id = request.form.get("session_id", "session1").strip() or "session1"
        username = request.form.get("username", "USER_A").strip() or "USER_A"

        resp, latency, ok, err = send_command(cmd)
        result = "SUCCESS" if ok else "BLOCKED"

        log_event(
            session_id=session_id,
            username=username,
            action="COMMAND",
            target="LED",
            value=cmd,
            result=result,
            latency_ms=latency,
            error=err
        )

        message = f"{cmd} → {resp} ({latency} ms)"

    return render_template("dashboard.html", message=message)

if __name__ == "__main__":
    # 0.0.0.0 allows other devices on the network (your Mac) to access it
    app.run(host="0.0.0.0", port=5000)
