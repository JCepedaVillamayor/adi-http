import requests

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def step1(url):
    step1_url = url + "/step1"
    req = requests.get(step1_url)
    if req.status_code == 200:
        print(req.json())
        return req.json()["value"], req.json()["next"]
    
def main():
    print("What is your DNI (Do not put your last letter)")
    dni = input()
    main_url = MAIN_URL.format(dni=dni)
    stp1_value, stp1_next_op = step1(main_url)

if __name__ == "__main__":
    main()
