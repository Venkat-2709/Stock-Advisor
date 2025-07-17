from fastapi import APIRouter, Depends, HTTPException
import redis
import uuid
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter()

# Connect to Redis (hostname should match docker-compose service name)
redis_client = redis.Redis(host="stock_redis", port=6379, decode_responses=True)

SESSION_TTL_SECONDS = 60 * 60 * 24  # 1 day

def verify_session(session_id: str):
    key = f"session:{session_id}"
    if not redis_client.exists(key):
        raise HTTPException(status_code=404, detail="Session not found")
    return session_id
# ------------------ Routes ------------------

@router.post("/session/start")
def start_session():
    session_id = str(uuid.uuid4())
    session_key = f"session:{session_id}"

    redis_client.hset(session_key, mapping={
        "status": "active",
        "created_at": datetime.utcnow().isoformat()
    })
    logger.info(f"New session started: {session_id}")
    redis_client.expire(session_key, SESSION_TTL_SECONDS)

    return {"session_id": session_id}


@router.post("/session/reset/{session_id}")
def reset_session(session_id: str = Depends(verify_session)):
    session_key = f"session:{session_id}"
    redis_client.delete(session_key)
    logger.info(f"Session reset: {session_id}")
    return {"status": "session deleted", "session_id": session_id}


@router.get("/session/exists/{session_id}")
def session_exists(session_id: str = Depends(verify_session)):
    session_key = f"session:{session_id}"
    exists = redis_client.exists(session_key)
    logger.info(f"Session exists check for {session_id}: {exists}")
    return {"session_id": session_id, "exists": bool(exists)}
