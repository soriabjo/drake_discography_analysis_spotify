from flask import Flask, request, redirect, jsonify
import requests
import uuid
import base64
import os

app = Flask(__name__)

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = 'http://localhost:8888/callback'


@app.route('/login')
def login():
    print('starting login method')
    state = str(uuid.uuid4())
    print('state: ', state)
    auth_url = f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope=user-read-private%20user-read-email&redirect_uri={redirect_uri}&state={state}'
    print('auth url: ', auth_url)
    print('end of login method')
    response = redirect(auth_url)
    response.set_cookie('spotify_auth_state', state)
    return response


@app.route('/callback')
def callback():
    print('starting callback method')
    code = request.args.get('code')
    state = request.args.get('state')
    stored_state = request.cookies.get('spotify_auth_state')
    print('code: ', code)
    print('state: ', state)
    print('stored_state: ', stored_state)

    if state is None or state != stored_state:
        return redirect('/#error=state_mismatch')

    auth_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }
    headers = {
        'Authorization': f'Basic {base64.b64encode((f"{client_id}:{client_secret}").encode()).decode()}'
    }
    response = requests.post(auth_url, data=data, headers=headers)
    print(response)
    print('end of callback method')
    if response.status_code == 200:
        access_token = response.json()['access_token']
        refresh_token = response.json()['refresh_token']
        print('access token: ', access_token, ' || ', 'refresh token: ', refresh_token)
        return redirect(f"/#access_token={access_token}&refresh_token={refresh_token}")
    else:
        return redirect('/#error=invalid_token')


@app.route('/refresh_token')
def refresh_token():
    print('start of refresh token method')
    refresh_token = request.args.get('refresh_token')
    auth_url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'refresh_token', 'refresh_token': refresh_token}
    headers = {
        'Authorization': f'Basic {base64.b64encode((f"{client_id}:{client_secret}").encode()).decode()}'
    }
    response = requests.post(auth_url, data=data, headers=headers)
    print('end of refresh token method')
    if response.status_code == 200:
        access_token = response.json()['access_token']
        return jsonify({'access_token': access_token})
    else:
        return jsonify({'error': 'invalid_token'}), 400


if __name__ == '__main__':
    print('starting script!')
    app.run(port=8888, debug=True)
    print('testing')
