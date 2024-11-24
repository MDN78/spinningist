import os
import requests


def get_auth_cookie():
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = os.getenv('API_URL')
    username = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    response = requests.post(url=url, headers=user_agent,
                                 data={'modlink': 'members', 'username': username, 'password': password},
                                 allow_redirects=False)
    cookie = response.cookies.get('session_')
    return cookie
