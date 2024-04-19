import time

import requests
import json
import sites
from colorama import Fore, Style

import warnings
warnings.filterwarnings("ignore")


class Arsen:
    def __init__(self):
        pass

    def CheckUser(self,username):
        json_path = "Resources/sites.json"

        count = 0

        startTime = time.time()

        with open(json_path, 'r', encoding='utf-8') as json_dosyasi:
            data = json.load(json_dosyasi)

            for site,info in data.items():
                s = sites.sites
                url = info.get("url")

                full_url = s.CreateString(username=username,url=url)

                response = requests.get(full_url)

                if(response.status_code == 200):
                    if (info.get("error") not in response.text):
                        print(f"{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}{site}{Fore.CYAN}]{Fore.RESET} {Style.NORMAL}{Fore.WHITE}{full_url}{Style.RESET_ALL}")
                        count+=1

        endTime = time.time()

        print(f"\nFound {count} profiles.")
        print(f"Operation took {round(endTime-startTime)} seconds.")

        # X doesnt working

def main():
    main = Arsen()

    username = input("Type the username that you want to search >>> ")
    print()

    main.CheckUser(username)