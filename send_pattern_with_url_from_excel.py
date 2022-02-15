import requests
import read_from_file
from config import api_key, pid, sender
# read from excel file and load the set with names and price.
user_set = read_from_file.add_to_set()

# first key.
p1 = 'name'
# second key.
p2 = 'price'

# value of first and second key is different for every user.
for i in user_set:
    v1 = i[0]
    v2 = i[1]
    tnum = i[2]
    url = f'http://ippanel.com:8080/?apikey={api_key}&pid={pid}&fnum={sender}&tnum={tnum}&p1={p1}&p2={p2}&v1={v1}&v2={v2}'
    a = requests.get(url)
    print(a)
