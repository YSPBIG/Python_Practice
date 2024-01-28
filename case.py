def case_counter(text):

    upper_case = 0
    lower_case = 0
    
    for character in text:
        if character.isalpha:
            if character.isupper():
                upper_case += 1
            elif character.islower():
                lower_case += 1
            else:
                pass

    return(f"Uppercase letters : {upper_case}, Lowercase letters: {lower_case}")

# Test cases
print(case_counter("Hello Wo)rld!"))  # Expected: Uppercase letters: 2, Lowercase letters: 8
print(case_counter("PYTHON"))  # Expected: Uppercase letters: 6, Lowercase letters: 0
print(case_counter("python"))  # Expected: Uppercase letters: 0, Lowercase letters: 6
print(case_counter("1234!@#$)"))  # Expected: Uppercase letters: 0, Lowercase letters: 0

