def add(num1,num2):
    return(num1 + num2)

def subtract(num1,num2):
    return(num1 - num2)

def multiply(num1,num2):
    return(num1*num2)

def divide(num1,num2):
    try:
        return(num1/num2)
    except ZeroDivisionError:
        return("Error : Division cannot be zero")
    
def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter Choice (1,2,3,4) : ")

        if choice in ("1","2","3","4"):
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))

            if choice == "1":
                result = add(num1,num2)
            elif choice =="2":
                result = subtract(num1,num2)
            elif choice == "3":
                result = multiply(num1,num2)
            elif choice == "4":
                result = divide(num1,num2)
            print(f"Result: {result}")

        elif choice == "5":
            break
        else:
            print("Invalid inout. Please try again")

calculator()