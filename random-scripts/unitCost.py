import sys

print('')
print("Type 'quit' to leave.")

while True:
    print('')
    num1 = input("Price: ")
    if num1.lower() == 'quit':
        sys.exit()
    num2 = input("# of units: ")
    if num2.lower() == 'quit':
        sys.exit()
    num3 = float(num1) / float(num2)
    food = 0
    while food < 10:
        print('')
        food = food + 1
    print(str(num3))
    print("Expression: "+num1+" / "+num2)
    print('')
