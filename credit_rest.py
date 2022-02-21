import requests
import json
from config import api_key


bytes_response = requests.get(url="http://rest.ippanel.com/v1/credit",
                              headers={"Authorization": f"AccessKey {api_key}"})
response = json.loads(bytes_response.content)

try:
    credit = int(response['data']['credit'])
    print(f"your credit is: {credit} rials.")

except KeyError:
    message = {
        "status": response['status'],
        "error": response['data']['error']
    }
    print(message['status'], message['error'])
