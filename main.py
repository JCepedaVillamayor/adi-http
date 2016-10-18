from step_1 import make_step1
from step_2 import make_step2

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def main():
    print("What is your DNI (Do not put your last letter)")
    dni = input()
    main_url = MAIN_URL.format(dni=dni)
    endpoint = make_step1(main_url)
    make_step2(main_url, endpoint, dni)
    
if __name__ == "__main__":
    main()
