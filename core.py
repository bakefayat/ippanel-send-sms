import requests
import json


class RestUrl:
    def __init__(self, address, api_key):
        self.address = address
        self.api_key = api_key
        self.response = None

    def get_request_to_url(self):
        self.response = requests.get(url=self.address,
                                     headers={"Authorization": f"AccessKey {self.api_key}"})
        return self.response

    def post_request_to_url(self, data):
        self.response = requests.post(url=self.address,
                                      headers={"Authorization": f"AccessKey {self.api_key}"},
                                      data=data)
        return self.response

    def response_content_to_json(self):
        message = json.loads(self.response.content)
        return message
