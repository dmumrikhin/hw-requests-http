from pprint import pprint
import requests

heroes_list = ['Hulk', 'Captain America', 'Thanos']
heroes_intelligence = {}

url = "https://akabab.github.io/superhero-api/api/all.json" # id/1.json"
response = requests.get(url)

for hero in response.json():
    if hero['name'] in heroes_list:
        heroes_intelligence[hero['name']] = hero['powerstats']['intelligence']


print(f'Самый умный из героев {max(heroes_intelligence, key=heroes_intelligence.get)}')