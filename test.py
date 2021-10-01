import requests
import threading
import time as t
import random
import proxy as p
from random import randint
from faker import Faker
from bs4 import BeautifulSoup
from itertools import cycle

try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    }

    url = 'https://nba75comp.com/au'
    s = requests.Session()
    r = s.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    email_domain = '@gmail.com'
    fname = 'john'
    lname = 'doe'
    email = fname+lname+email_domain

    data = {
        'email_address': email,
        'favorite_nba_team': "",
        'first_name': fname,
        'last_name': lname,
        'phone_number': "",
        'agree_rules': "yes"
    }

    post_url = 'https://nba75comp.com/app/entry_action/134'
    r = s.post(url=post_url, data=data, headers=headers)
    print(r.text)
    # t.sleep(10)
    if r.json()['status'] != 'OK':
        print(Exception(f'{r.status_code} | {r.text}'))

    print(f'\033[92m Entry submitted'+ ' '+ email)

except Exception as e:
        print(f'\033[91m Exception {e}')