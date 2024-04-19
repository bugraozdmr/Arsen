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

                s.CreateString(username=username,url=url)






def main():
    main = Arsen()

    main.CheckUser()