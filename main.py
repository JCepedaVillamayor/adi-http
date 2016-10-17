import requests
import json

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def catch_first_operand(url):
    op1_url = url + "/step1"
    req = requests.get(op1_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]

def catch_second_operand(url, next_op):
    step2_url = url + next_op
    req = requests.get(step2_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]

def catch_operator(url, next_op):
    step3_url = url + next_op
    req = requests.get(step3_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"], req.json()["uri"]

def calc_result(op1, op2, operator):
    op1 = int(op1)
    op2 = int(op2)
    res = 0
    if operator == '+':
        res = op1 + op2
    elif operator == '/':
        res = op1 / op2
    elif operator == '-':
        res = op1 - op2
    elif operator == '*':
        res = op1 * op2
    return res

def send_result(main_url, result_uri, result):
    result_url = main_url + result_uri
    json_info = {"value": result}
    headers = {"Content-Type": "application/json"}
    req = requests.post(result_url, headers=headers, json=json_info)
    print(req.json())
    return req.status_code

def make_step1(main_url):
    first_op, op2_endpoint = catch_first_operand(main_url)
    second_op, operator_endpoint = catch_second_operand(main_url, op2_endpoint)
    operator, step2_endpoint, result_uri = catch_operator(main_url, operator_endpoint)
    result = calc_result(first_op, second_op, operator)
    status_code = send_result(main_url, result_uri, result)
    return step2_endpoint


def main():
    print("What is your DNI (Do not put your last letter)")
    dni = input()
    main_url = MAIN_URL.format(dni=dni)
    make_step1(main_url)
    
if __name__ == "__main__":
    main()
