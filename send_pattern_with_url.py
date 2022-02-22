import requests
from config import api_key, pid, sender

receiver = "989111111111"
# first key.
p1 = 'name'
# first value.
v1 = 'some random name'
# second key.
p2 = 'price'
# second value
v2 = 'some random price'


url = f'http://ippanel.com:8080/?apikey={api_key}&pid={pid}&fnum={sender}&tnum={receiver}&p1={p1}&p2={p2}&v1={v1}&v2={v2}'
get_url = requests.get(url)
print(get_url)
