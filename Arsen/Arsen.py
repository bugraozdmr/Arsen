import requests
import json
import sites

class Arsen:
    def __init__(self):
        pass

    def CheckUser(self,username):
        json_path = "Resources/sites.json"

        with open(json_path, 'r', encoding='utf-8') as json_dosyasi:
            data = json.load(json_dosyasi)

            for site,info in data.items():
                s = sites.sites
                url = info.get("url")

                full_url = s.CreateString(username=username,url=url)

                response = requests.get(full_url)

                if(response.status_code == 200):
                    if (info.get("error") not in response.text):
                        print(f"[{site}] {full_url}")


def main():
    main = Arsen()

    print("Type the username that you want to search >>> ")
    username = input()

    main.CheckUser(username)