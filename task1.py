import requests
import operator

URL = 'https://superheroapi.com/api/'
TOKEN = '2619421814940190'
COMMAND = ['search', 'powerstats']
superhero_list = ['Hulk', 'Captain America', 'Thanos', 'Star-Lord', 'Iron Man', 'Groot', 'Thor']


class HeroAPI:

    def __init__(self, token):
        self.token = token

    def search_hero_id(self, superhero):
        full_url = f'{URL}{TOKEN}/{COMMAND[0]}/{superhero}/'
        response = requests.get(full_url, timeout=5)
        superhero_id = response.json()['results'][0]['id']
        return superhero_id

    def get_hero_intelligence(self, superhero):
        superhero_dict = {}
        full_url = f'{URL}{TOKEN}/{HeroAPI.search_hero_id(self, superhero)}/{COMMAND[1]}'
        responce = requests.get(full_url, timeout=5)
        superhero_dict[superhero] = int(responce.json()['intelligence'])
        return superhero_dict


def superhero_comparison_intelligence(TOKEN, superhero_list):
    comparison_dict = {}
    for i in superhero_list:
        k = HeroAPI.get_hero_intelligence(TOKEN, i)
        comparison_dict.update(k)
    result = dict(sorted(comparison_dict.items(), key=operator.itemgetter(1), reverse=True))
    print(f'Запущен процесс сравнения интеллекта героев: {", ".join(superhero_list)}\n'
          f'Герои в порядке снижения интеллекта, от самого умного к самому не умному:')
    for i in result:
        print(f'{i} со значением интеллекта {result.get(i)}')


superhero_comparison_intelligence(TOKEN, superhero_list)
