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

def insert_value_in_options(main_url, endpoint, value):
    result_url = main_url + endpoint
    json_info = {"value": value}
    headers = {"Content-Type": "application/json"}
    req = put_request(result_url, json_info, headers)

def check_options_value(main_url, endpoint, value):
    result_url = main_url + endpoint
    get_request(result_url)

def final_step(main_url, endpoint):
    result_url = main_url + endpoint
    get_request(result_url)
    
    
def make_step4(main_url, endpoint):
    print("\n\n/////////\nSTEP 4\n/////////")
    next_uri, uri = get_options_url(main_url, endpoint)
    value = check_options(main_url, uri)
    print("The value is {}".format(value))
    insert_value_in_options(main_url, uri, value)
    final_step(main_url, next_uri)
    check_options_value(main_url, uri, value)
    
