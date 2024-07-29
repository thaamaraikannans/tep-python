val1 = int(input("Enter Number 1: "))
val2 = int(input("Enter Number 2: "))

# print(type(int(val1)))

opp = input("which operation would you like to perform ? eg: +, -, *, / :- ")

if opp == "+":
    print(val1+val2)
elif opp == "-":
    pass
elif opp == "*":
    print(val1*val2)
elif opp == "/":
    print(val1/val2)
else:
    print("not valid operation")