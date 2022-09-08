from datetime import datetime


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "environment": "dev",
        "ping": "pong",
        "testing": True,
        "timestamp": datetime.strftime(datetime.utcnow(), "%s"),
    }
