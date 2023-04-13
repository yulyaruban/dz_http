
import requests

import json 
from pprint import pprint
url = "https://akabab.github.io/superhero-api/api/all.json"

    
response = requests.get(url)

data = response.json()


heroes_list = ['Hulk', 'Captain America', 'Thanos']
d = {}
for i in data:
    for m in heroes_list:
      if i['name'] == m and m not in list(d.keys()):
        d[m] = i['powerstats']['intelligence']
        
# print(d)
max_intelligence = max(d, key = d.get)

print(f'Самый умный из трех супергероев (Hulk, Capitan America, Thanos) - {max_intelligence}')