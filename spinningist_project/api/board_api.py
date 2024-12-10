import os
import requests


class BoardApi:

    def get_auth_cookie(self):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = os.getenv('API_URL')
        username = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        response = requests.post(url=url, headers=user_agent,
                                 data={'modlink': 'members', 'username': username, 'password': password},
                                 allow_redirects=False)
        cookie = response.cookies.get('session_')
        return cookie

    def add_item_to_cart(self, my_token):
        url = "https://spinningist.ru/"
        payload = {
            'modlink': 'buy/2Fspinningi/2Fmaximus/2Fwinner-x/2Fudilische-spin-maximus-winner-x-27866',
            'itemId': '27866',
            'offset': 0,
            'catoffset': 0,
            'action': 'add',
            'qty': 1,
            'eshop_cart_simple': 1
        }
        headers = {
            'cookie': f'vid=710aaba106794f1efde881f6e45f59fe; is_logged_in=1; session_={my_token}'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text


board_api = BoardApi()
