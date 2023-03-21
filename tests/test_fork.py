
access_token = 'ghu_7JIPTgYCcKfiBuZXWBscTzRdxuZK2w1bSO9p'
code = '0f6ce141db3195343ced'


def test_create_request(client):
    response = client.get("/fork-request?code={}".format(code))
    assert response.status_code == 200
    assert b'Click the button below to fork' in response.data
    assert b'access_token=' in response.data


def test_fork(client):
    response = client.get("/fork-repo?access_token={}".format(access_token))
    assert response.status_code == 200
    assert b'successfully forked' in response.data