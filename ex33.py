i = 0
numbers = []

var_1 = 4
var_2 = 1

def kid(input_a, input_b):
    i = 0
    numbers = []

    for i in range(0, input_a):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + var_2
        print("Numbers now ", numbers)
        print(f"At the bottom i is {i}")

kid(var_1, var_2)
