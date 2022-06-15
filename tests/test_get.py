from .conftest import get_user_token, create_user
from .test_create import files


def test_get_success(test_client):
    create_user(test_client, "user")
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    code = test_client.post(
        "/frames/",
        files=files[:3],
        headers={"Authorization": f"Bearer {token}"}
    ).json()[0]["request_code"]

    response = test_client.get(f"/frames/{code}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["request_code"] == response.json()[1]["request_code"] == response.json()[2]["request_code"] == code
    assert type(response.json()[0]["datetime"]) is not None
    assert type(response.json()[1]["datetime"]) is not None
    assert type(response.json()[2]["datetime"]) is not None
    assert response.json()[0]["file_name"] is not None
    assert response.json()[1]["file_name"] is not None
    assert response.json()[2]["file_name"] is not None


def test_get_with_bad_code(test_client):
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    response = test_client.get("/frames/999", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 400


def test_get_unauthorised(test_client):
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    code = test_client.post(
        "/frames/",
        files=files[:3],
        headers={"Authorization": f"Bearer {token}"}
    ).json()[0]["request_code"]
    response = test_client.get(f"/frames/{code}")
    assert response.status_code == 401


def test_get_non_own(test_client):
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    code = test_client.post(
        "/frames/",
        files=files[:5],
        headers={"Authorization": f"Bearer {token}"}
    ).json()[0]["request_code"]

    create_user(test_client, "user2")
    token2 = get_user_token(test_client, {
        "username": "user2",
        "password": "123"
    })
    response = test_client.get(f"/frames/{code}", headers={"Authorization": f"Bearer {token2}"})
    assert response.status_code == 403
