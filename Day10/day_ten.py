from Day_10.art import logo

def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
def calculator():
    print(logo)
    a = float(input("what's the first number :"))
    continue_operation = True
    while continue_operation:
        total = 0


        for i in operations:
            print(i)
        operation = input("Enter an operation :")
        b = float(input("what's the second number :"))
        total = operations[operation](a, b)
        print(f"{a}{operation}{b}={total}")
        continue_calculating = input(f"Type 'y' for contnuie calculating with  {total} Type n for restart ").lower()
        if continue_calculating == 'y':
            a = total
        else:
            continue_operation = False
            print("\n"*20)
            calculator()
calculator()