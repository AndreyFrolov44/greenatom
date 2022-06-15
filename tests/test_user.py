def test_user_create(test_client):
    response1 = test_client.post("/user/", json={
        "username": "test",
        "password": "123",
        "password2": "123"
    })
    response2 = test_client.post("/user/", json={
        "username": "test2",
        "password": "123",
        "password2": "123"
    })
    assert response1.status_code == 200
    assert response1.json()["username"] == "test"
    assert response1.json()["id"] is not None
    assert response2.status_code == 200
    assert response2.json()["username"] == "test2"
    assert response2.json()["id"] is not None


def test_login(test_client):
    response = test_client.post("/login/", data={
        "username": "user",
        "password": "123"
    })
    assert response.status_code == 200


def test_login_bad(test_client):
    response = test_client.post("/login/", data={
        "username": "123",
        "password": "123"
    })
    assert response.status_code == 401
