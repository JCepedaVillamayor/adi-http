from network_utilities import post_request, get_request, delete_request

def obtain_the_value_from_the_endpoint(main_url, endpoint):
    '''
    Checks the endpoint and gets the list and the following endpoints
    '''
    result_url = main_url + endpoint
    return get_request(result_url, 'uri', 'value', 'next')

def remove_element(main_url, endpoint, elements):
    '''
    Extract the first element from the list given and endpoint
    '''
    head, *tail = elements
    result_url = "{}{}/{}".format(main_url, endpoint, head)
    delete_request(result_url)

def request_the_next_step(main_url, next_uri):
    '''
    Obtain the next step
    '''
    result_url = main_url + next_uri
    return get_request(result_url, 'next')

def check_that_the_value_has_been_removed(main_url, uri, value):
    ''' the function title '''
    result_url = main_url + uri
    obtained_list = get_request(result_url, 'value')[0]
    print("Initial value:{}".format(value))
    print("Obtained value:{}".format(obtained_list))
    
def make_step3(main_url, endpoint):
    ''' 
    The third step is focused on dealing with DELETE request
    Task: delete the first element of a list obtained in an endpoint
    '''
    print("\n\n/////////\nSTEP 3\n/////////")
    uri, value, next_uri = obtain_the_value_from_the_endpoint(main_url, endpoint)
    remove_element(main_url, uri, value)
    step4 = request_the_next_step(main_url, next_uri)[0]
    check_that_the_value_has_been_removed(main_url, uri, value)
    return step4
    
