def calculate_factorial(number):
    if number < 0: #To state that the number to calculate the factorial cannot be negative or zero.
        raise ValueError ("Factorial is not able to do with Negative number") 
    
    result = 1 #set the answer as 1 because every positive number that multiply will be start with 1.

    for i in range(1, number + 1): #Using for loop to calculate factorial 
        result *= i # *i is to multiply until x which in this case is multiply as i times 

    return result

#i is the loop variable that takes on the values in specific range
#range(1,number + 1) is to generate the sequence of the number start from 1 until number + 1 so the final answer will end at number that fill in.

print(calculate_factorial(5))  
print(calculate_factorial(0))  
print(calculate_factorial(3))  
print(calculate_factorial(-1))
    