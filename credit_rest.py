import requests.exceptions

from core import RestUrl

url = RestUrl()
response = url.get_credit()
print(response)
