import requests
import json
from config import api_key
url_address = "http://rest.ippanel.com/v1/messages/"
sender = "+983000505"
receiver = ["+989111111111", ]
message_text = "متن تست"

bytes_response = requests.post(url=url_address,
                               headers={"Authorization": f"AccessKey {api_key}"},
                               data={"originator": sender,
                                     "recipients": receiver,
                                     "message": message_text})
response = json.loads(bytes_response.content)
try:
    bulk_id = response['data']['bulk_id']
    print(f"message sent. bulk id is: {bulk_id}")

except KeyError:
    message = {
        "status": response['status'],
        "error": response['data']['error']
    }
    print(message['status'], message['error'])
