

def max_of_2(x, y):
    # if x > y:
    #     return x
    # else:
    #     return y
    return x if x > y else y


def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)


a = 4
b = 5
c = 3
wieksza = maximum_of(a, b, c)
print("Moja wieksza liczba to: ", wieksza)
