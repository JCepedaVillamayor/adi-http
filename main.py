from step_1 import make_step1
from step_2 import make_step2
from step_3 import make_step3
from step_4 import make_step4

MAIN_URL = "http://httptask-142719.appspot.com/{dni}"

def main():
    print("What is your DNI (Do not put your last letter)")
    dni = input()
    main_url = MAIN_URL.format(dni=dni)
    step2_endpoint = make_step1(main_url)
    step3_endpoint = make_step2(main_url, step2_endpoint, dni)
    step4_endpoint = make_step3(main_url, step3_endpoint)
    make_step4(main_url, step4_endpoint)
    
if __name__ == "__main__":
    main()
