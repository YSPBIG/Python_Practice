def is_prime(number):
    if number < 2: #To check the number less than two 
        return False
    
    for i in range(2, number):
        if number % i == 0: #To show that the number is able to divided by some numbers which show as remainder is 0.
            return False
    else:
        return True #True when the number that not able to divided by any number in the range

print(is_prime(11))  
print(is_prime(4))  
print(is_prime(2))  
print(is_prime(1))
    