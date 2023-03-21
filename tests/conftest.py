import pytest
from healthjoy_cc import create_app

@pytest.fixture()
def app():
    app = create_app({
        "CLIENT_ID": 'Iv1.745a221eb3703043',
        "CLIENT_SECRET": 'fa10e91de679e4d25db3f21d785839cfc8142060',
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()