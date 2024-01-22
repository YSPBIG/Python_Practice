def case_counter():

    upper_case = 0
    lower_case = 0
      
    user_input = input("Please enter the word here : ")
    for characters in user_input:
        if characters.isupper():
            upper_case += 1 
        elif characters.islower():
            lower_case += 1
        else:
            pass
    print("The number of uppercase is : ",upper_case , "lowercase is : ",lower_case )

case_counter()