import requests
import json

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def step1(url):
    step1_url = url + "/step1"
    req = requests.get(step1_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]

def step2(url, next_op):
    step2_url = url + next_op
    req = requests.get(step2_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]

def step3(url, next_op):
    step3_url = url + next_op
    req = requests.get(step3_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"], req.json()["uri"]

def main():
    print("What is your DNI (Do not put your last letter)")
    dni = input()
    main_url = MAIN_URL.format(dni=dni)
    op1, op2_endpoint = step1(main_url)
    op2, operator_endpoint = step2(main_url, op2_endpoint)
    operator, next_endpoint, uri = step3(main_url, operator_endpoint)
    
if __name__ == "__main__":
    main()
