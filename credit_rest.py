from config import api_key
from core import RestUrl

url = RestUrl('http://rest.ippanel.com/v1/credit', api_key)
url.get_request_to_url()
response = url.response_content_to_json()

try:
    credit = int(response['data']['credit'])
    print(f"your credit is: {credit} rials.")

except KeyError:
    message = {
        "status": response['status'],
        "error": response['data']['error']
    }
    print(message['status'], message['error'])
