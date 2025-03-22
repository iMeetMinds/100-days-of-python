from art import logo

print(logo)

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

result_num = 0
y_num_one = float(input("What's first number? "))

want_continue = True
while want_continue:
    operations = {
        "+" : addition,
        "-" : subtraction,
        "*" : multiplication,
        "/" : division,
    }
    # operations = ["+","-","*","/"]
    for i in operations:
        print(f"{i}")
    operator = input("Pick an operation : ")
    y_num_two = float(input("What's next number? "))

    if result_num != 0:
        y_num_one = result_num

    if operator in operations:
        result_num = operations[operator](y_num_one, y_num_two)
        # if operator == "+":
        #     result_num = addition(y_num_one, y_num_two)
        # elif operator == "-":
        #     result_num = subtraction(y_num_one, y_num_two)
        # elif operator == "*":
        #     result_num = multiplication(y_num_one, y_num_two)
        # elif operator == "/":
        #     result_num = division(y_num_one, y_num_two)
    else:
        print("Enter valid operation.")
        continue

    print(f"{y_num_one} {operator} {y_num_two} = {result_num}")

    choice = input(f"Type 'Y' to continue calculating with {result_num} or type 'N' to start new calculations : ").lower()

    if choice == "n":
        want_continue = False