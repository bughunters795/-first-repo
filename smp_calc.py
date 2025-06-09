def calculator():
    num1 = int(input("Enter the no1?:"))
    num2 = int(input("Enter the no2?:"))

    sum = num1 + num2

    subtract = num1 - num2

    multip =  num1 * num2 
    
    div = num1 /num2


    op= input("enter the operations?: ")
        # op = ' + , -, /, * '
    if(op=='+'):
        print(f"the sum+ of two number's is{sum}\n")

    elif(op == '-'):
        print(f"the subtraction- of two number's is{subtract}\n")

    elif(op == '*'):
        print(f"the multiplication* of two number's is{multip}\n")
    elif(op == '/'):
        print(f"the division/ of two number's is{div}\n")
    else:
        print("wrong operations")

calculator()