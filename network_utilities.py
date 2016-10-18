import requests
import json

def post_request(url, json_content={}, headers={}):
    req = requests.post(url, headers=headers, json=json_content)
    print("JSON: \n{}\nStatus code: {}".format(req.json(), req.status_code))
    return req.status_code

def put_request(url, json_content={}, headers={}):
    req = requests.put(url, headers=headers, json=json_content)
    print("JSON: \n{}\nStatus code: {}".format(req.json(), req.status_code))
    return req.status_code

def get_request(url, *args):
    req = requests.get(url)
    print("JSON: \n{}\nStatus code: {}".format(req.json(), req.status_code))
    return [req.json()[val] for val in args]
