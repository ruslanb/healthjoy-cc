# healthjoy-cc
HealthJoy Coding Challenge

## Overview
This project forks its own repo on GitHub into the user's GitHub account.
It is a Flask application that requires to be run inside a Flask server.
It is also a GitHub app, meaning that the user needs to install the app into his GitHub account first to trigger the fork.

### Installation Setup
This project uses Python 3. To install on Linux
1. Open a terminal. Navigate to the top level directory of the project.

2. Issue the following commands:

`python3 -m venv venv`

`. venv/bin/activate`

`pip install .`

As a result, a virtual environment is created in `venv` directory with all the necessary libraries to run and test the project.

### Usage
Start Flask server by running the following command in the top level directory of the project.

`flask --app healthjoy_cc/app run`

Open your browser.