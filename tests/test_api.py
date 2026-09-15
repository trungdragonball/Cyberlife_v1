from fastapi.testclient import TestClient
from apps.cyberlife.main import app

c=TestClient(app)

def test_health():
    r=c.get("/health")
    assert r.status_code==200
    assert r.json()["system"]=="CyberLife V1"

def test_chat():
    r=c.post("/api/v1/chat",json={"owner_id":"owner","message":"hello"})
    assert r.status_code==200
