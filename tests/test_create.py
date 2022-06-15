import os

cur_path = os.getcwd()

files = [("files_list", (f"{i}.jpg", open(cur_path + f'/tests/images/{i}.jpg', 'rb'), 'image/jpeg')) for i in range(1, 16)]
files.append(("files_list", ("16.png", open(cur_path + '/tests/images/16.png', 'rb'), 'image/png')))


def test_no_image_post(test_client):
    response = test_client.post("/frames/", files=[files[-1]])
    assert response.status_code == 200
    assert response.json() == []


def test_wrong_number_of_images(test_client):
    response = test_client.post("/frames/", files=files)
    assert response.status_code == 400


def test_create_inbox(test_client):
    response = test_client.post("/frames/", files=files[:3])
    assert response.status_code == 200
    assert len(response.json()) == 3
    assert response.json()[0]["request_code"] == response.json()[1]["request_code"] == response.json()[2]["request_code"] == 1
    assert type(response.json()[0]["datetime"]) is not None
    assert type(response.json()[1]["datetime"]) is not None
    assert type(response.json()[2]["datetime"]) is not None
    assert response.json()[0]["file_name"] is not None
    assert response.json()[1]["file_name"] is not None
    assert response.json()[2]["file_name"] is not None
