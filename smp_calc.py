def calculator():
    num1 = int(input("Enter the no1?:"))
    num2 = int(input("Enter the no2?:"))



    


    op= input("enter the operations?: ")
        # op = ' + , -, /, * '
    if(op=='+'):
        sum = num1 + num2
        print(f"the sum+ of two number's is{sum}\n")

    elif(op == '-'):
        subtract = num1 - num2
        print(f"the subtraction- of two number's is{subtract}\n")

    elif(op == '*'):
            multip =  num1 * num2 
            print(f"the multiplication* of two number's is{multip}\n")
    elif(op == '/'):
        div = num1 /num2
        print(f"the division/ of two number's is{div}\n")
    else:
        print("wrong operations")

calculator()