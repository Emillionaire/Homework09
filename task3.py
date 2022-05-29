import datetime
from pprint import pprint

import requests
import time

tag = 'Python'
url = "https://api.stackexchange.com/2.3/questions?"


class Reddit:

    def search(self):
        try:
            time_now = int(time.time())
            time_stop = int(time_now - 86400 * 2)
            page = 1
            line = 0
            full_url = f'{url}page={page}&pagesize=100&fromdate={time_stop}&todate={time_now}&order=desc&sort=creation&tagget={tag}&site=stackoverflow'
            responce = requests.get(full_url).json()
            for i in responce['items']:
                print(responce['items'][line]['title'])
                line += 1
            while responce['has_more']:
                page += 1
                print(page)
                responce = requests.get(
                    f'{url}page={page}&pagesize=100&fromdate={time_stop}&todate={time_now}&order=desc&sort=creation&tagget={tag}&site=stackoverflow').json()
                line = 0
                for i in responce['items']:
                    print(responce['items'][line]['title'])
                    line += 1
        except KeyError:
            print('End of list')


reddit_search = Reddit()
reddit_search.search()
