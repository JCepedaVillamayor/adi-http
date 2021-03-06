import requests
from requests import Request
from network_utilities import get_request, post_request, put_request

def get_options_url(main_url, endpoint):
    ''' get the url to send the OPTIONS request '''
    result_url = main_url + endpoint
    return get_request(result_url, 'next', 'uri')

def check_options(main_url, endpoint):
    ''' do a options requests and gets the allow value '''
    result_url = main_url + endpoint
    req = requests.options(result_url)
    return req.headers['Allow']

def insert_value_in_options(main_url, endpoint, value):
    '''
    insert the value in the endpoint
    '''
    result_url = main_url + endpoint
    json_info = {"value": value}
    headers = {"Content-Type": "application/json"}
    put_request(result_url, json_info, headers)

def check_options_value(main_url, endpoint, value):
    ''' Check that the value has been inserted '''
    result_url = main_url + endpoint
    obtained_value = get_request(result_url, 'value')[0]
    print("Initial value:{}".format(value))
    print("Obtained value:{}".format(obtained_value))
    
def final_step(main_url, endpoint):
    ''' final request '''
    result_url = main_url + endpoint
    get_request(result_url)
    
    
def make_step4(main_url, endpoint):
    ''' 
    The fourth step is focused on dealing with OPTIONS request
    Task: obtain the allow functions given and enpoint and put the result
    in the endpoint
    '''
    print("\n\n/////////\nSTEP 4\n/////////")
    next_uri, uri = get_options_url(main_url, endpoint)
    value = check_options(main_url, uri)
    print("The value is {}".format(value))
    insert_value_in_options(main_url, uri, value)
    final_step(main_url, next_uri)
    check_options_value(main_url, uri, value)
    
