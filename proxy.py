import requests
import pyfiglet
import time
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor
import sys
import os
from colorama import Fore

osystem = sys.platform
if osystem == "linux":
    os.system("clear")
else:
    os.system("cls")

print(f"""{Fore.RED}
██████╗ ██╗████████╗    ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
██╔══██╗██║╚══██╔══╝    ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
██████╔╝██║   ██║       ███████╗██╔██╗ ██║███████║█████╔╝ █████╗
██╔══██╗██║   ██║       ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝
██████╔╝██║   ██║       ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
╚═════╝ ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
""")

def download_proxies_list(choice):
    if choice == 1:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=http&timeout=15000&proxy_format=ipport&format=text'
    elif choice == 2:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks4&timeout=15000&proxy_format=ipport&format=text'
    elif choice == 3:
        proxy_list_url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&protocol=socks5&timeout=15000&proxy_format=ipport&format=text'
    elif choice == 4:
        osystem = sys.platform
        if osystem == "linux":
            os.system("clear")
        else:
            os.system("cls")

        print(f"""{Fore.RED}
██████╗ ██╗████████╗    ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
██╔══██╗██║╚══██╔══╝    ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
██████╔╝██║   ██║       ███████╗██╔██╗ ██║███████║█████╔╝ █████╗
██╔══██╗██║   ██║       ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝
██████╔╝██║   ██║       ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
╚═════╝ ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
            """)
        print(f"{Fore.CYAN}# Coding by {Fore.YELLOW}: {Fore.RED}BitSnake\n{Fore.CYAN}# GitHub {Fore.YELLOW}: {Fore.RED}https://github.com/bitsnakee\n{Fore.CYAN}# Version {Fore.YELLOW}: {Fore.RED}1.1\n")
        print(f"{Fore.RED}[{Fore.YELLOW}All{Fore.RED}] {Fore.YELLOW}All\n{Fore.RED}[{Fore.YELLOW}Us{Fore.RED}] {Fore.YELLOW}United States\n{Fore.RED}[{Fore.YELLOW}Ru{Fore.RED}] {Fore.YELLOW}Russia\n{Fore.RED}[{Fore.YELLOW}FR{Fore.RED}] {Fore.YELLOW}France\n{Fore.RED}[{Fore.YELLOW}De{Fore.RED}] {Fore.YELLOW}Germany\n{Fore.RED}[{Fore.YELLOW}Pl{Fore.RED}] {Fore.YELLOW}Poland\n{Fore.RED}[{Fore.YELLOW}Cn{Fore.RED}] {Fore.YELLOW}China\n{Fore.RED}[{Fore.YELLOW}Ir{Fore.RED}] {Fore.YELLOW}Iran\n")

        country_code = input(f"{Fore.RESET}Enter the country code >> ")
        proxy_list_url = f'https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country={country_code}&timeout=15000&proxy_format=ipport&format=text'
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
    file_path = "Proxy.txt"
    osystem = sys.platform
    if osystem == "linux":
        os.system("clear")
    else:
        os.system("cls")
    print(f"""{Fore.RED}
██████╗ ██╗████████╗    ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
██╔══██╗██║╚══██╔══╝    ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
██████╔╝██║   ██║       ███████╗██╔██╗ ██║███████║█████╔╝ █████╗
██╔══██╗██║   ██║       ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝
██████╔╝██║   ██║       ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
╚═════╝ ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
        """)
    print(f"{Fore.CYAN}# Coding by {Fore.YELLOW}: {Fore.RED}BitSnake\n{Fore.CYAN}# GitHub {Fore.YELLOW}: {Fore.RED}https://github.com/bitsnakee\n{Fore.CYAN}# Version {Fore.YELLOW}: {Fore.RED}1.1\n")
    file_paths = ["Proxy.txt", "proxyCheck.txt"]
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                if file_path == "Proxy.txt":
                    number_of_proxies = max(len(lines) - 1, 0)
                else:
                    number_of_proxies = len(lines)
                print(f"{Fore.RESET}{file_path}: {number_of_proxies}")
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error reading {file_path} file: {e}")

user_input = int(input(f"{Fore.CYAN}# Coding by {Fore.YELLOW}: {Fore.RED}BitSnake\n{Fore.CYAN}# GitHub {Fore.YELLOW}: {Fore.RED}https://github.com/bitsnakee\n{Fore.CYAN}# Version {Fore.YELLOW}: {Fore.RED}1.1\n\n{Fore.RED}[{Fore.YELLOW}1{Fore.RED}]{Fore.YELLOW} Http/s\n{Fore.RED}[{Fore.YELLOW}2{Fore.RED}]{Fore.YELLOW} Socks4\n{Fore.RED}[{Fore.YELLOW}3{Fore.RED}]{Fore.YELLOW} Socks5\n{Fore.RED}[{Fore.YELLOW}4{Fore.RED}]{Fore.YELLOW} Country\n\n{Fore.RESET}Select Option >> "))

if ask_user_for_proxy_check():
    proxies_list = download_proxies_list(user_input)
    if proxies_list is not None:
        active_proxies_list = check_proxies(proxies_list)
        save_active_proxies(active_proxies_list)
else:
    print("Proxy check skipped.")

