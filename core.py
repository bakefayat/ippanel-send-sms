import requests
import json
from config import api_key, base_endpoint


def response_content_to_json(bytes_response):
    json_response = json.loads(bytes_response.content)
    return json_response


class RestUrl:
    def get_credit(self):
        address = base_endpoint + 'credit'
        try:
            bytes_response = requests.get(url=address,
                                          headers={"Authorization": f"AccessKey {api_key}"})
            json_response = response_content_to_json(bytes_response)
            response = json_response['data']['credit']
            return response

        except KeyError:
            error = {
                "status": json_response['status'],
                "error": json_response['data']['error']
            }
            return error

        except requests.exceptions.ConnectionError:
            response = "connection refused."
            return response

    def get_user_detail(self):
        address = base_endpoint + 'user'
        try:
            bytes_response = requests.get(url=address,
                                          headers={"Authorization": f"AccessKey {api_key}"})
            json_response = response_content_to_json(bytes_response)
            response = json_response['data']['user']
            return response

        except KeyError:
            error = {
                "status": json_response['status'],
                "error": json_response['data']['error']
            }
            return error

        except requests.exceptions.ConnectionError:
            response = "connection refused."
            return response

    def post_request_to_url(self, sender, receivers, message_text):
        address = base_endpoint + 'messages/'
        data = {
            "originator": sender,
            "recipients": receivers,
            "message": message_text,
        }
        try:
            bytes_response = requests.post(url=address,
                                     headers={"Authorization": f"AccessKey {api_key}"},
                                     data=data)
            json_response = response_content_to_json(bytes_response)
            response = json_response['data']['bulk_id']
            return response

        except KeyError:
            error = {
                "status": json_response['status'],
                "error": json_response['data']['error']
            }
            return error

        except requests.exceptions.ConnectionError:
            response = "connection refused."
            return response
