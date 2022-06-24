import requests
import threading
import time as t
import src.proxy as p
import random
from src.user_generator import User
from bs4 import BeautifulSoup
from itertools import cycle

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