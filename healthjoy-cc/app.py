from flask import Flask, request, url_for, abort
import re
import requests

app = Flask(__name__)

client_id = 'Iv1.745a221eb3703043'
client_secret = 'fa10e91de679e4d25db3f21d785839cfc8142060'

installation_confirm_html = '<!DOCTYPE html>' \
                            '<head><title>healthjoy-fork Installed</title></head>' \
                            '<body><p>Github app <b>healthjoy-fork</b> was successfully installed. ' \
                            'Click the button below to fork <b>healthjoy-cc</b> repo to your account.</p> ' \
                            '<button onclick="window.location.href=\'{}\';">Click Here</button> ' \
                            '</body>'
fork_confirm_html = '<!DOCTYPE html>' \
                    '<head><title>healthjoy-fork Installed</title></head>' \
                    '<body><p><b>healthjoy-cc</b> repo was successfully forked.</p></body>'


@app.route('/fork-request')
def fork_request():
    code = request.args.get('code', '')
    access_token = get_access_token(code)

    # Check access_token is not null
    if not access_token:
        abort(500, description='Could not get access token from GitHub')

    target_url = url_for('fork_repo', access_token=access_token)
    return installation_confirm_html.format(target_url)


@app.route('/fork-repo')
def fork_repo():
    access_token = request.args.get('access_token', '')
    response_status = fork_health_joy_cc_repo(access_token)
    if response_status != 200:
        abort(response_status, description='Could not fork healthjoy-cc repo')
    return fork_confirm_html


def get_access_token(code):
    url = 'https://github.com/login/oauth/access_token'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
    }
    access_token = ''
    res = requests.post(url, data=data).text

    res_strs = re.split(r'=|&', res)
    for i in range(len(res_strs)):
        if res_strs[i] == 'access_token':
            access_token = res_strs[i+1]

    return access_token


def fork_health_joy_cc_repo(access_token):
    url = 'https://api.github.com/repos/ruslanb/healthjoy-cc/forks'
    headers = {"Authorization": "BEARER {}".format(access_token)}
    return requests.post(url, headers=headers).status_code


if __name__ == '__main__':
    app.run()