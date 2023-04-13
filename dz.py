
import requests

import json 
from pprint import pprint
url_task1 = "https://akabab.github.io/superhero-api/api/all.json"

    
response1 = requests.get(url_task1)

data = response1.json()


heroes_list = ['Hulk', 'Captain America', 'Thanos']
d = {}
for i in data:
    for m in heroes_list:
      if i['name'] == m and m not in list(d.keys()):
        d[m] = i['powerstats']['intelligence']
        
# print(d)
max_intelligence = max(d, key = d.get)

print(f'Самый умный из трех супергероев (Hulk, Capitan America, Thanos) - {max_intelligence}')







class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(url = files_url, headers = headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url = upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path = disk_file_path).get("href", "")
        response = requests.put(href, data = open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

TOKEN = "y0_AgAAAAA0Fa5UAADLWwAAAADg1gteBrYmb7mbQUuqKjPjaxcerAdhaDA"

if __name__ == '__main__':
  ya = YandexDisk(token=TOKEN)
  data_disk = ya.get_files_list()
  ya.upload_file_to_disk('testfoto_for_dzhttp.jpg', 'testfoto.jpg')