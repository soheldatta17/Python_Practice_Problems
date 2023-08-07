a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
if (a > b):
    if (a > c):
        print("Greatest: ", a)
    else:
        print("Greatest", c)
else:
    if (b > c):
        print("Greatest: ", b)
    else:
        print("Greatest", c)
