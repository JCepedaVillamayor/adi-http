from network_utilities import *

def get_dni_endpoint(main_url, endpoint):
    result_url = main_url + endpoint
    return get_request(result_url, 'next', 'uri', 'value')

def post_dni(main_url, dni_uri, dni):
    result_url = main_url + dni_uri
    json_info = {"value": dni}
    headers = {"Content-Type": "application/json"}
    return put_request(result_url, json_info, headers)

def check_dni(main_url, check_dni_uri):
    result_url = main_url + check_dni_uri
    get_request(result_url)
    
def make_step2(main_url, endpoint):
    print("\n\n/////////\nSTEP 2\n/////////")
    check_dni_uri, dni_uri , dni = get_dni_endpoint(main_url, endpoint)
    status_code = post_dni(main_url, dni_uri, dni)
    if status_code != 200:
        print("Exiting. Step 2 failed")
    check_dni(main_url, check_dni_uri)
