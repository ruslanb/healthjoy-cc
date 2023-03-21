import pytest

access_token = 'ghu_HqoMCnKGbNcqyGL11QGOFKDFAgg04J3niT6v'
code = '0f6ce141db3195343ced'


@pytest.mark.skip(reason="no way of currently testing this. code value can be used only once to get access_token")
def test_create_request(client):
    response = client.get("/fork-request?code={}".format(code))
    assert response.status_code == 200
    assert b'Click the button below to fork' in response.data
    assert b'access_token=' in response.data


def test_fork(client):
    response = client.get("/fork-repo?access_token={}".format(access_token))
    assert response.status_code == 200
    assert b'successfully forked' in response.data