loop =1

choice = 0

while loop == 1:
    print("WELCOME TO CALCULATOR.PY")

    print("your options are")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")

    print("3) multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")

    choice =  input("choose your option:")
    if choice == 1:
        add1 = input("add this:")
        add2 = input("to this:")
        print(add1," + ", add2, " = ", add1 + add2)
    elif choice == 2:
        sub2 = input("subtract this:")
        sub1 = input("from this:")
        print(sub1," - ",sub2," = ",sub1 - sub2)
    elif choice == 3:
        mul1 = input("multiply this:")
        mul2 = input("to this:")
        print(mul1,"*",mul2,"=",mul1,mul2)
    elif choice == 4:
        div1 = input("divide this:")
        div2 = input("by this")
        print(div1,"/",div2,"=",div1/div2)
    elif choice == 5:
        loop = 0


    print("Thankyou for using calculator.py!")