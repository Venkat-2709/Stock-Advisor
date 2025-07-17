import requests

from config.keys import settings

def save_profile(session_id, risk, goal, sectors):
    payload = {
        "session_id": session_id,
        "risk_level": risk,
        "goal": goal,
        "preferred_sectors": sectors
    }
    res = requests.post(f"{settings.FASTAPI_URL}/profile", json=payload)
    return res.status_code == 200

def get_profile(session_id):
    try:
        res = requests.get(f"{settings.FASTAPI_URL}/profile/{session_id}")
        if res.status_code == 200:
            return res.json()
    except Exception:
        return None