import math
a = float(input("Enter the number"))
b = float(input("Enter the number"))
c = float(input("Enter the number"))
if (((b*b)-(4*a*c)) < 0):
    print("Not possible")
else:
    x1 = (((-1.0)*b)+math.sqrt((b*b)-(4*a*c)))/(2.0*a)
    x2 = (((-1.0)*b)-math.sqrt((b*b)-(4*a*c)))/(2.0*a)
    print(x1)
    print(x2)
