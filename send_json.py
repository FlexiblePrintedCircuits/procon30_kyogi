import json
import requests

class SendJson():
    def send(match_id, action):
        url = "http://localhost:8081/matches/{0}/action".format(match_id)
        token = { "Authorization": "procon30_example_token" }
        res = requests.post(url, headers=token, json=action).json()
        return res