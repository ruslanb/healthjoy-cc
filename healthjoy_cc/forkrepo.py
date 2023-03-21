import flask
import re
import requests

blueprint = flask.Blueprint('forkrepo', __name__)

installation_confirm_html = '<!DOCTYPE html>' \
                            '<head><title>healthjoy-fork Installed</title></head>' \
                            '<body><p>Github app <b>healthjoy-fork</b> was successfully installed. ' \
                            'Click the button below to fork <b>healthjoy-cc</b> repo to your account.</p> ' \
                            '<button onclick="window.location.href=\'{}\';">Click Here</button> ' \
                            '</body>'
fork_confirm_html = '<!DOCTYPE html>' \
                    '<head><title>healthjoy-fork Installed</title></head>' \
                    '<body><p><b>healthjoy-cc</b> repo was successfully forked.</p></body>'


@blueprint.route('/fork-request')
def fork_request():
    code = flask.request.args.get('code', '')
    access_token = get_access_token(code)

    # Check access_token is not null
    if not access_token:
        flask.abort(500, description='Could not get access token from GitHub')

    target_url = flask.url_for('forkrepo.fork_repo', access_token=access_token)
    return installation_confirm_html.format(target_url)


@blueprint.route('/fork-repo')
def fork_repo():
    access_token = flask.request.args.get('access_token', '')
    response_status = fork_health_joy_cc_repo(access_token)
    if response_status >= 300:
        flask.abort(response_status, description='Could not fork healthjoy-cc repo')
    return fork_confirm_html


def get_access_token(code):
    url = 'https://github.com/login/oauth/access_token'
    data = {
        'client_id': flask.current_app.config['CLIENT_ID'],
        'client_secret': flask.current_app.config['CLIENT_SECRET'],
        'code': code,
    }
    access_token = ''
    response = requests.post(url, data=data).text

    # response body is in the form of key1=value1&key2=value2
    # split the response body into separate strings (i.e. [key1, value1, key2, value2])
    response_kvs = re.split(r'=|&', response)
    for i in range(len(response_kvs)):
        if response_kvs[i] == 'access_token':
            access_token = response_kvs[i+1]

    return access_token


def fork_health_joy_cc_repo(access_token):
    url = 'https://api.github.com/repos/ruslanb/healthjoy-cc/forks'
    headers = {"Authorization": "BEARER {}".format(access_token)}
    return requests.post(url, headers=headers).status_code
