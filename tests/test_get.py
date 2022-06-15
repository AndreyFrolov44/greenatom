def test_get_success(test_client):
    response = test_client.get("/frames/1")
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["request_code"] == response.json()[1]["request_code"] == response.json()[2]["request_code"] == 1
    assert type(response.json()[0]["datetime"]) is not None
    assert type(response.json()[1]["datetime"]) is not None
    assert type(response.json()[2]["datetime"]) is not None
    assert response.json()[0]["file_name"] is not None
    assert response.json()[1]["file_name"] is not None
    assert response.json()[2]["file_name"] is not None


def test_get_with_bad_code(test_client):
    response = test_client.get("/frames/2")
    assert response.status_code == 200
    assert response.json() == []
    test_client.delete("/frames/1")
