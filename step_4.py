import requests
from requests import Request
from network_utilities import get_request, post_request, put_request

def get_options_url(main_url, endpoint):
    result_url = main_url + endpoint
    return get_request(result_url, 'next', 'uri')

def check_options(main_url, endpoint):
    result_url = main_url + endpoint
    req = requests.options(result_url)
    return req.headers['Allow']

def insert_value_options(main_url, endpoint, value):
    result_url = main_url + endpoint
    json_info = {"value": value}
    headers = {"Content-Type": "application/json"}
    req = put_request(result_url, headers, json_info)

def make_step4(main_url, endpoint):
    print("\n\n/////////\nSTEP 4\n/////////")
    next_uri, uri = get_options_url(main_url, endpoint)
    value, *rest = check_options(main_url, uri)
    insert_value_options(main_url, next_uri, value)
