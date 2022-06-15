from .test_create import files


def test_delete_success(test_client):
    test_client.post("/frames/", files=files[:3])
    response = test_client.delete("/frames/2")
    assert response.status_code == 204


def test_delete_with_bad_code(test_client):
    response = test_client.delete("/frames/5")
    assert response.status_code == 400
