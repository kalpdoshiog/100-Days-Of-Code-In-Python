from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {"+": add,
               "-":  sub,
               "*": mul,
               "/": div,
               }

# print(operations["*"](4, 8))

def first_num():
    first_number = float(input("What's the first number?: "))
    return first_number

def which_operations(first_number):

    for operation in operations:
        print(operation)
    which_operation = input("Which operation you want to perform? Pick any one: ")
    second_number = float(input("What's the next number?: "))

    output = f"{operations[which_operation](first_number, second_number)}"
    print(f"{first_number} {which_operation} {second_number} = {output}")
    return output

output = which_operations(first_num())

should_continue = True
while should_continue:
    will_continue = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ").lower()

    if will_continue == "y":
        output = which_operations(float(output))
    else:
        first_number = None
        print("\n" * 100)
        print(logo)
        output = which_operations(first_num())




