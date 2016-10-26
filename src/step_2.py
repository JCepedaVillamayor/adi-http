from network_utilities import get_request, put_request

def get_dni_endpoint(main_url, endpoint):
    ''' 
    make a petition to the endpoint and return the dni endpoint
    to insert your dni_uri
    '''
    result_url = main_url + endpoint
    return get_request(result_url, 'next', 'uri', 'value')

def post_dni(main_url, dni_uri, dni):
    '''
    make a PUT request to /dni endpoint
    '''
    result_url = main_url + dni_uri
    json_info = {"value": dni}
    headers = {"Content-Type": "application/json"}
    return put_request(result_url, json_info, headers)

def check_dni(main_url, check_dni_uri, dni_uri, dni):
    ''' 
    Check that the value inserted it's the dni 
    and return the next endpoint
    '''
    result_url = main_url + check_dni_uri
    next_endpoint = get_request(result_url, 'next')[0]
    result_url = main_url + dni_uri
    dni_val = get_request(result_url, 'value')[0]
    print("Original DNI:{} \nDNI in the backend:{}".format(dni, dni_val))
    return next_endpoint

def make_step2(main_url, endpoint, dni):
    '''
    The second step is focused on dealing with PUT request
    Task: obtain the dni endpoint and pass your dni to the backend
    given a valid endpoint
    '''
    print("\n\n/////////\nSTEP 2\n/////////")
    check_dni_uri, dni_uri, _ = get_dni_endpoint(main_url, endpoint)
    post_dni(main_url, dni_uri, dni)
    next_endpoint = check_dni(main_url, check_dni_uri, dni_uri, dni)
    return next_endpoint
