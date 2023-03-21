# healthjoy-cc
HealthJoy Coding Challenge

## Overview
This project forks its own repo on GitHub into the user's GitHub account.
It is a Flask application that requires to be run inside a Flask server.
It is also a GitHub app, meaning that the user needs to install the app into his GitHub account first to trigger the fork (see **Usage** instruction below).

### Installation Setup
This project uses Python 3. To install on Linux
1. Open a terminal. Navigate to the top level directory of the project.

2. Issue the following commands:

`python3 -m venv venv`

`. venv/bin/activate`

`pip install .`

As a result, a virtual environment is created in `venv` directory with all the necessary libraries to run and test the project.

### Usage
1. Start Flask server by running the following command in the top level directory of the project.

`flask --app healthjoy_cc run`

As a result the following message is displayed:

```
 * Serving Flask app 'healthjoy_cc'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

2. Open your browser and point it to [https://github.com/apps/healthjoy-fork](). You should see a green `Install` button. If you installed this app previously, there will be a grey `Configure` button instead. You will need to uninstall the app first. Click on `Configure`, scroll down and click on red button `Uninstall`. Follow instructions to uninstall the app and go back to the app [URL](https://github.com/apps/healthjoy-fork).

3. Click on the green `Install` button. This will get you to GitHub's `Install and Authorize healthjoy-fork` screen.

4. Click on the green `Install and Authorize` button. This will get you to the app's page with the following message:
```
Github app healthjoy-fork was successfully installed. Click the button below to fork healthjoy-cc repo to your account.
```

5. Click on the grey `Click Here` button. You should get `healthjoy-cc repo was successfully forked.` message.

6. Go to your profile GitHub page and navigate to `Repositories` tab. You should see `healthjoy-cc` repository there.

### Running Tests
1. The page from step 5 above should have the following URL: http://localhost:5000/fork-repo?access_token=ghu_HqoMCnKGbNcqyGL11QGOFKDFAgg04J3niT6v Copy the value of `access_token` query string param and paste it as a string value of the `access_token` variable in the file `tests/test_fork.py`.

2. In your terminal go the top level directory of the project and issue the following commands:

`. venv/bin/activate`

`pytest`

This should produce the following output:
```
============================================= test session starts =============================================
platform darwin -- Python 3.7.9, pytest-7.2.2, pluggy-1.0.0
rootdir: /Users/ruslan/Projects/healthjoy-cc
collected 2 items

tests/test_fork.py s.
```

Note: I could not find a way to generate an access token without `code` value that is being passed as a query param to the callback URL. Moreover, once one access token is issued, `code` value becomes invalid. Therefore, I had to skip one of the tests and require a valid access token to run the second test. Possible ways around are:

a) Find a different way to generate access tokens (possibly, by `installation_id` that is passed to the callback URL as well)

b) Get access token along with a refresh token. Store the refresh token in the test and use it to get an access token before running tests.