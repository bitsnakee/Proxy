import requests
import random
import pyfiglet
import time
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor
import sys
import os

osystem = sys.platform
if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")

text = "Bit Snake"
font = "standard"
print(pyfiglet.figlet_format(text, font=font))

def download_proxies_list(choice):
    if choice == 1:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout=15000&proxy_format=ipport&format=text'
    elif choice == 2:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks4&timeout=15000&proxy_format=ipport&format=text'
    elif choice == 3:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks5&timeout=15000&proxy_format=ipport&format=text'
    else:
        print("Invalid choice.")
        return

    response = requests.get(proxy_list_url)

    proxies = response.text.split('\r\n')

    with open('Proxy.txt', 'w') as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")

    return proxies

def ask_user_for_proxy_check():
    return True

def check_proxy(proxy):
    proxy_dict = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
    try:
        response = requests.get("http://www.google.com", proxies=proxy_dict, timeout=5, verify='http://www.example.com')

        if response.status_code == 200:
            return proxy
    except requests.RequestException:
        pass

    return None


def check_proxies(proxies):
    active_proxies = []

    with alive_bar(len(proxies), bar="smooth", spinner="dots") as progress_bar:
        with ThreadPoolExecutor(max_workers=250) as executor:
            futures = [executor.submit(check_proxy, proxy) for proxy in proxies]

            for future in futures:
                result = future.result()
                if result:
                    active_proxies.append(result)

                progress_bar()
                time.sleep(0.1)

    return active_proxies

def save_active_proxies(active_proxies):
    with open('proxyCheck.txt', 'w') as file:
        for proxy in active_proxies:
            file.write(f"{proxy}\n")
    print(f"Active proxies saved in 'proxyCheck.txt'.")

user_input = int(input("[1] Http\n[2] Socks4\n[3] Socks5\n\nEnter: "))

if ask_user_for_proxy_check():
    proxies_list = download_proxies_list(user_input)
    active_proxies_list = check_proxies(proxies_list)
    save_active_proxies(active_proxies_list)
else:
    print("Proxy check skipped.")
