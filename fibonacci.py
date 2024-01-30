def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value <= 0:
        return [0] if max_value == 0 else [] #Use this because the condition of max value is 0 the answer will show as [0]
    #but if the max value is negative number, the answer will be [] 

    # Initialize the Fibonacci sequence with the first two numbers
    fib_sequence = [0, 1] #We need to start with the first two sequence because it have to start the loop

    # Generate Fibonacci sequence using a while loop
    while fib_sequence[-1] + fib_sequence[-2] <= max_value: #If the value is less than the max value so we need to add more as the next_fib to meet the amount
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib) #Add to the sequence

    return fib_sequence

# Test cases
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))   # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))   # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected output: []
