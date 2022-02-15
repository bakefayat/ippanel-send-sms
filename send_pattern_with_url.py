import os
import requests
from read_from_file import add_to_set
from decouple import config

# rename the .env-sample to .env and fill it with your own API_KEY and pid.
api_key = config("API_KEY")
# pattern id -> unique id of pattern. ask sms panel provider.
pid = config("PID")
sender = '3000505'
receiver = "9371304458"
# first key.
p1 = 'name'
# first value.
v1 = 'some random name'
# second key.
p2 = 'price'
# second value
v2 = 'some random price'


# read from excel file and load the set with names and price.
user_set = add_to_set()

url = f'http://ippanel.com:8080/?apikey={api_key}&pid={pid}&fnum={sender}&tnum={receiver}&p1={p1}&p2={p2}&v1={v1}&v2={v2}'
get_url = requests.get(url)
