from network_utilities import post_request, get_request, delete_request

def check_next_steps_to_procced(main_url, endpoint):
    result_url = main_url + endpoint
    return get_request(result_url, 'uri', 'value', 'next')

def remove_element(main_url, endpoint, elements):
    head, *tail = elements
    result_url = "{}{}/{}".format(main_url, endpoint, head)
    delete_request(result_url)

def check_removed_element(main_url, next_uri):
    result_url = main_url + next_uri
    return get_request(result_url, 'next')

    
def make_step3(main_url, endpoint):
    print("\n\n/////////\nSTEP 3\n/////////")
    uri, value, next_uri = check_next_steps_to_procced(main_url, endpoint)
    remove_element(main_url, uri, value)
    step4 = check_removed_element(main_url, next_uri)[0]
    get_request(main_url + uri)
    return step4
    
