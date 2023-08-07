year = int(input("Enter the Year: "))
if (year % 400 == 0):
    print("Leap year")
else:
    if (year % 100 == 0):
        print("Not a Leap Year")
    elif (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
