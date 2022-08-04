# solve for x

# x will always be the first variable recieved
# and this function will only deal with addition and subtraction operations

def solve_eq(equation):

    # recive the string and split the string into variables
    x, operator, num1, equal, num2 = equation.split()

    # type casting the number variable to integer
    num1, num2 = int(num1), int(num2)

    if operator == '+':
        return "x = " + str(num2 - num1)

    elif operator == '-':
        return "x = " + str(num2 + num1)


print (solve_eq("x - 5 = 9"))


