import requests
import json

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def step1(url):
    step1_url = url + "/step1"
    req = requests.get(step1_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]

def step2(url, value, next_op):
    step2_url = url + next_op
    print(step2_url)
    headers = {'Content-type': 'application/json'}
    payload = {"value": value}
    req = requests.post(step2_url, json=payload, headers=headers)
    print(req.status_code)
    print(req.text)
    
def main():
    print("What is your DNI (Do not put your last letter)")
    dni = "70360133" #input()
    main_url = MAIN_URL.format(dni=dni)
    stp1_value, stp1_next_op = step1(main_url)
    step2(main_url, stp1_value, stp1_next_op)
    
if __name__ == "__main__":
    main()
main()
