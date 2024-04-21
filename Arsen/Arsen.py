import time
import Main
import requests
import json
import sites
from colorama import Fore, Style
import Result
import argparse

import warnings
warnings.filterwarnings("ignore")



def parse_arguments():
    parser = argparse.ArgumentParser(description=f'{Main.module_description}')
    parser.add_argument('-t', '--timeout', type=int, help='Operation ends after n seconds. ** arsen.py -t 30 => this operation ends after 30 seconds ')
    parser.add_argument('-u', '--username', type=str, help='After this parameter type username that you want to search')
    parser.add_argument('-o', '--output', type=str, help='After this parameter type filename only .Output will be in the same folder. ** arsen.py -u grant -o out.txt')


    return parser.parse_args()


class Arsen:
    def __init__(self):
        pass

    def CheckUser(self,username):
        # flag value for output
        flag = 0

        # args
        args = parse_arguments()

        if (args.output is not None):
            if (".txt" not in args.output):
                print("Filename must have .txt in it")
                return

            text = ""
            flag = 1

        json_path = "Resources/sites.json"

        count = 0

        opTime = 0

        print(
            f'\n{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}]{Fore.RESET} {Style.NORMAL} Checking username : {Style.BRIGHT}{Fore.CYAN}{Fore.YELLOW}{username}{Fore.YELLOW}{Fore.RESET} {Style.NORMAL}')

        with open(json_path, 'r', encoding='utf-8') as json_dosyasi:
            data = json.load(json_dosyasi)

            site_count = len(list(data.items()))

            opTime = 0

            # output start
            if(flag == 1):
                text += f"Searching for : {username}\n\n"

            for site,info in data.items():
                opStart = time.time()

                s = sites.sites
                url = info.get("url")

                full_url = s.CreateString(username=username,url=url)

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Accept-Language": "en-US"
                }

                response = requests.get(full_url,headers=headers)

                # check
                if(response.status_code == 200):
                    if (info.get("error") not in response.text):
                        if(site == "tiktok") : print(response.text)
                        print(f"{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}{site}{Fore.CYAN}]{Fore.RESET} {Style.NORMAL}{Fore.WHITE}{full_url}{Style.RESET_ALL}")
                        count+=1

                        if(flag == 1):
                            text += f"{site} : {full_url}\n"



                opEnd = time.time()


                opTime += opEnd-opStart

                if(args.timeout is not None):
                    if (opTime >= args.timeout):
                        break


        print(f"\n{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}]{Fore.RESET} {Style.NORMAL}Found {count}/{site_count} profiles")
        print(f"{Style.BRIGHT}{Fore.CYAN}[{Fore.GREEN}*{Fore.CYAN}]{Fore.RESET} {Style.NORMAL}Operation took {round(opTime)} seconds")


        if(flag == 1):
            text += f"\nFound {count}/{site_count} in {round(opTime)} seconds"

        if (args.output is not None):
            r = Result.Result
            r.WriteOut(text=text, filename=args.output)



if __name__ == "__main__":
    main = Arsen()

    args = parse_arguments()

    if (args.username is not None):
        main.CheckUser(args.username)
    else:
        Main.info()