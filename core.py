import requests
import json
from config import api_key, base_endpoint


def response_content_to_json(bytes_response):
    json_response = json.loads(bytes_response.content)
    return json_response


class RestUrl:
    def get_credit(self):
        address = base_endpoint + 'v1/credit'
        try:
            bytes_response = requests.get(url=address,
                                          headers={"Authorization": f"AccessKey {api_key}"})
            json_response = response_content_to_json(bytes_response)
            response = json_response['data']['credit']
            return response

        except KeyError:
            res = {
                "status": json_response['status'],
                "error": json_response['data']['error']
            }
            return res

        except requests.exceptions.ConnectionError:
            response = "connection refused."

    def get_user_detail(self):
        address = self.endpoint + 'v1/user'
        response = requests.get(url=address,
                                headers={"Authorization": f"AccessKey {api_key}"})
        return response

    def post_request_to_url(self, data):
        response = requests.post(url=self.address,
                                 headers={"Authorization": f"AccessKey {api_key}"},
                                 data=data)
        return response
