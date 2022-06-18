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
                "type": "Misc",
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
                "type": "Misc",
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


# Joke filtering tests
def test_get_jokes_filters(test_app_with_db):
    # Add a joke
    response = test_app_with_db.post(
        "/jokes/",
        data=json.dumps(
            {
                "setup": "I told my psychiatrist I got suicidal tendencies.",
                "punchline": "He said from now on I have to pay in advance.",
                "type": "Dark",
            }
        ),
    )
    response = test_app_with_db.get("/jokes/?type=Dark&count=1&contains=psychiatrist")
    assert response.status_code == 200
    response_dict = response.json()
    # test the ?count filter
    assert len(response_dict) == 1
    # test out the ?type filter
    assert response_dict[0]["type"] == "Dark"
    # test out the ?contains filter
    assert (
        response_dict[0]["setup"] == "I told my psychiatrist I got suicidal tendencies."
    )


def test_get_jokes_filtering_invalid_count(test_app_with_db):
    response = test_app_with_db.get("/jokes/?count=0")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "count"],
                "msg": "ensure this value is greater than 0",
                "type": "value_error.number.not_gt",
                "ctx": {"limit_value": 0},
            }
        ]
    }
