import requests

from config.keys import settings


def start_session():
    try:
        response = requests.post(f"{settings.FASTAPI_URL}/session/start")
        return response.json().get("session_id")
    except Exception:
        return None

def reset_session(session_id):
    try:
        requests.post(f"{settings.FASTAPI_URL}/session/reset/{session_id}")
    except Exception:
        pass
