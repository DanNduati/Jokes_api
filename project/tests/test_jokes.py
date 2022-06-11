import json

import pytest


def test_add_joke(test_app_with_db):
    """Test adding a joke"""
    response = test_app_with_db.post(
        "/jokes/",
        data=json.dumps(
            {
                "setup": "Why do cows wear bells?",
                "punchline": "Because their horns don't work!",
                "type": "misc",
            }
        ),
    )
    assert response.status_code == 201
    assert response.json()["punchline"] == "Because their horns don't work!"


def test_add_joke_invalid_json(test_app_with_db):
    """Test adding a joke with invalid json request field"""
    response = test_app_with_db.post("/jokes/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "setup"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "punchline"],
                "msg": "field required",
                "type": "value_error.missing",
            },
            {
                "loc": ["body", "type"],
                "msg": "field required",
                "type": "value_error.missing",
            },
        ]
    }


def test_get_joke(test_app_with_db):
    """Test getting a single joke"""
    response = test_app_with_db.post(
        "/jokes/",
        data=json.dumps(
            {
                "setup": "Why do cows wear bells?",
                "punchline": "Because their horns don't work!",
                "type": "misc",
            }
        ),
    )
    joke_id = response.json()["id"]
    response = test_app_with_db.get(f"/jokes/{joke_id}/")
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict["id"] == joke_id
    assert response_dict["setup"] == "Why do cows wear bells?"
    assert response_dict["punchline"]
    assert response_dict["type"]


def test_get_joke_invalid_id(test_app_with_db):
    response = test_app_with_db.get("/jokes/9999/")
    assert response.status_code == 404


def test_get_all_jokes(test_app_with_db):
    response = test_app_with_db.post(
        "/jokes/",
        data=json.dumps(
            {
                "setup": "Why do cows wear bells?",
                "punchline": "Because their horns don't work!",
                "type": "misc",
            }
        ),
    )
    joke_id = response.json()["id"]
    response = test_app_with_db.get("/jokes/")
    assert response.status_code == 200
    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == joke_id, response_list))) == 1
