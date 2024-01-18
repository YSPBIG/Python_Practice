# is for Single Line comment 
print("Hello,World")

"""
This is use for multiple comments
which not be only in the one line same as the first one
"""
print("Hello,World")

"""
To create the variable or assign the value will use the = symbol
Lower and Upper case can be different variables
Variable name cannot be start with numbers
"""
age = 26
name = "Yossapol1997"
print(age)
print(name)

#To assign multiple variable and use , for each name
a,b,c = "Gender","Birthdate","Status"
print(a,b,c)

#Best practice to create naming convention is using the lower_case_with_underscore

#Combine two strings
greeting = "Hello"
message = greeting + "," + name + "!" 
print(message)

#Repeating String
laugh = "ha"
repeat_laugh = laugh * 4
print(repeat_laugh)

#Accessing the character in the string
letter = name[5] #Index start at 0
print(letter)

#Slicing string
sub_word = name[8:12] #Slicing for index 8 to 11
print(sub_word)

