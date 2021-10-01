import requests
import threading
import time as t
import proxy as p
import random
from user_generator import User
from bs4 import BeautifulSoup
from itertools import cycle

##### EDIT #####
use_catchall = False
catchall = ''
proxy_txt = 'proxies.txt'
num_threads = 10

# use for emails
user_txt = 'emails.txt'

##### DO NOT EDIT #####

def random_entry(proxy, user):
    try:
        s = requests.Session()
        s.proxies=proxy

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
        }

        url = 'https://nba75comp.com/au'

        r = s.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')

        # get random team
        teams = soup.find_all('option')
        team = random.choice(teams)['value']

        data = {
            'email_address': user.email,
            'favorite_nba_team': team,
            'first_name': user.fname,
            'last_name': user.lname,
            'phone_number': "",
            'agree_rules': "yes"
        }

        post_url = 'https://nba75comp.com/app/entry_action/134'
        r = s.post(url=post_url, data=data, headers=headers)
        print(r.text)

        if r.json()['status'] != 'OK':
            return Exception(f'{r.status_code} | {r.text}')

        print(f'\033[92m Entry submitted'+ ' '+ user.email)

    except Exception as e:
            print(f'\033[91m Exception {e}')


def main():
    proxies = p.read_proxies(proxy_txt)
    proxies = cycle(proxies)

    if use_catchall == False:
        with open(user_txt) as txt_file:
            users = txt_file.read().splitlines()
        users = cycle(users)

    num_entries = 1

    while True:
        threads = []
        for i in range(num_threads):
            proxy = next(proxies)
            proxy = p.proxy_parse(proxy)
            user = User()

            if use_catchall == False:
                user_text = next(users)
                user.email_user(user_text)
            else:
                user.fake_user(catchall)

            print(f'Entry #{num_entries}, entering with {user.email}')
            print('Using ' + proxy['https'] + ' for raffle entries')

            thread = threading.Thread(target=random_entry, args=(proxy,user))
            num_entries += 1

            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    main()