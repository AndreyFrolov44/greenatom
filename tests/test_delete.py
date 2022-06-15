from .test_create import files
from .conftest import create_user, get_user_token


def test_delete_unauthorised(test_client):
    create_user(test_client, "user")
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    code = test_client.post("/frames/",
                            files=files[:5],
                            headers={"Authorization": f"Bearer {token}"}
                            ).json()[0]["request_code"]
    response = test_client.delete(f"/frames/{code}")
    assert response.status_code == 401


def test_delete_non_own_code(test_client):
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
    response = test_client.delete(f"/frames/{code}", headers={"Authorization": f"Bearer {token2}"})
    assert response.status_code == 403


def test_delete_success(test_client):
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    code = test_client.post(
        "/frames/",
        files=files[:5],
        headers={"Authorization": f"Bearer {token}"}
    ).json()[0]["request_code"]

    response = test_client.delete(f"/frames/{code}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 204


def test_delete_with_bad_code(test_client):
    token = get_user_token(test_client, {
        "username": "user",
        "password": "123"
    })
    response = test_client.delete("/frames/999", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 400
