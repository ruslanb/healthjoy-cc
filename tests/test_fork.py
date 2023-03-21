
access_token = 'ghu_e1DnhS4T5GfLtFSYvAUVAkhSHpFjUE0aNmti'
code = 'd663cf29690cbc5beed8'

def test_fork(client):
    response = client.get("/fork-repo?access_token={}".format(access_token))
    assert response.status_code == 200
    assert b'successfully forked' in response.data