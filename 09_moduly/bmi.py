def get_status(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif 18.5 <= bmi < 25:
        return 'normal'
    elif 25 <= bmi < 30:
        return 'overweight'
    else:
        return 'obesity'

def bmi_calculator(weight, height):
    bmi = round(weight / (height * height), 2)
    return get_status(bmi)

if __name__ == "__main__":
    print ('Run as main code')
    print('Your BMI:', bmi_calculator(53, 1.59))
else:
    print ('Run as module')
