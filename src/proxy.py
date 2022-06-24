from itertools import cycle

# read proxies from text file
def read_proxies(file_path):
    with open(file_path) as txt_file:
        proxies = txt_file.read().splitlines()
    return proxies

# parse proxy
def proxy_parse(proxy):
    proxy_parts = proxy.split(':')

    if len(proxy_parts) == 2:
        ip, port = proxy_parts
        formatted_proxy = {
            'http': f'http://{ip}:{port}/',
            'https': f'https://{ip}:{port}/'
        }

    elif len(proxy_parts) == 4:
        ip, port, user, password = proxy_parts
        formatted_proxy = {
            'http': f'http://{user}:{password}@{ip}:{port}/',
            'https': f'https://{user}:{password}@{ip}:{port}/'
        }

    # formatted_proxy = formatted_proxy['http']
    return formatted_proxy