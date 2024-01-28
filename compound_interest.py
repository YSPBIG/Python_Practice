def compound_interest_calculator(P, r, n, t): #The factors given in the question that need to have 4 factors 
    # Validate input parameters
    if not all(isinstance(arg, (int, float)) for arg in [P, r, n, t]): #To validate that all of the factors in each parameter should be the numbers as integer and float
        raise ValueError("All parameters must be numeric") #raise is to show the error message 
    elif r < 0 or n <= 0 or t < 0:  #To make condition in each of the component as interest rate is not be negative and n,t should be a value which is more than 1
        raise ValueError("Invalid input. Make sure interest rate is non-negative, and n and t are positive")

    # Calculate compound interest using the formula A = P(1 + r/n)^(nt)
    A = P * (1 + r/n)**(n*t)
    
    return A

#isinstance(arg,(int,float)) is to check the given objective as 'arg' which is the instance of int or float
#It will return as True if the data is correct in that condition. 
#all() is to return the outcomes as true if all elements in there is True.


# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Expected: Amount after 7 years