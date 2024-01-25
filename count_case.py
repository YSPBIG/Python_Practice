def case_counter():

    upper_case = 0
    lower_case = 0
      
    user_input = input("Please enter the word here : ") # To add the word that want the app to run
    for characters in user_input:
        if characters.isupper(): #To add the uppercase since is .isupper is to capture the uppercase alphabet
            upper_case += 1 
        elif characters.islower(): #To add the lowercase since is .islower is to capture the uppercase alphabet
            lower_case += 1
        else:
            pass
    print("The number of uppercase is : ",upper_case , "lowercase is : ",lower_case )

case_counter()
