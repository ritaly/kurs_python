import bmi

def show_tip(status):
    with open(status + '.txt', 'r') as fopen:
        return fopen.read()
        

def check_bmi(w, h):
    return bmi.bmi_calculator(w, h)

def main():
    weight = float(input('Your weight (kg): '))
    height = float(input('Your height (m): '))

    status = check_bmi(weight, height)

    print(show_tip(status))

if __name__ == "__main__":
    main()
