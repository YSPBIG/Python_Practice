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

text = "Practice"

#Convert to Uppercase
upper_text = text.upper()
print(upper_text)

#Convert to Lowercase
lower_text = text.lower()
print(lower_text)

#Remove the whitespace in the sentence
whitespace_string = "    Example,  the space in sentences        "

stripped_string = whitespace_string.strip()
print(stripped_string)

#Finding the substring
sentence = "This is the example for the subsentence"
index = sentence.find("the")
print(index) #Output is 8

#Replace the substring
new_sentence = sentence.replace ("example" , "intances")
print(new_sentence)

#Split the string
data_set = "Apple,Banana,Orange,Pineapple"
fruits = data_set.split(",")
print(fruits) #Output is ['Apple', 'Banana', 'Orange', 'Pineapple']

#Joining a list of strings
new_data_set = "/".join(fruits)
print(new_data_set) #Output is Apple/Banana/Orange/Pineapple

strformat_msg = "Hello, {} . This is an example of format. Your age is {}".format(name, age)
print(strformat_msg)

format_msg = f"Hello, {name}. Your age is {age} years old "
print(format_msg)

# \n is to insert new line within a string
new_line_sentence = "This will test\n create new line"
print(new_line_sentence)

# \t is to add a tab is the sentences
new_space_sentence = "This will test\t create new line"
print(new_space_sentence)

# use r to ignore the escape character
example_to_ignore = r"This is to test\the escape character"
print(example_to_ignore)

#Integer = int
#Number with decimal point = float

#Symbol for operations 
# + , - , * , / the answer will be always float, 
# // = divides and returns the largest whole number
# % will return the remainder of the division
# ** will be power of another

print(5 / 2) #2.5
print(5//2) #2
print(5%2) #1
print(5**2) #25

#billion = 1_000_000

rounded_number = round(3.14159, 2) 
integer_number = int(5.7)
float_number = float(7)
absolute_value = abs(-5.5) 

print(rounded_number) #Rounds to 3.14
print(integer_number) #Covert to 5
print(float_number) #Covert to 7.0
print(absolute_value)  #Returns 5.5

#Calculate the square root of a number
import math
square_root = math.sqrt(16)
print(square_root)

import random
random_integer = random.randint(1,10)
print(random_integer)

x = 100
print("The value of x is" , x )
print(f"{name} is {age} years old")

#Use end and following string to have the same sentences
print("Hello", "World" , sep="-", end="!")
print(" This is on the same line.")

print("Hello", end = "!")
print("World")

#Input function
username = input("Enter your name: ")
print("Hello,", username)

age_new = input("Enter your age : ")
age_new = int(age_new) #To convert to integer
print("You are", age, "years old.")

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print("Your full name is ", first_name, last_name)

number = 42 
converted_to_string = str(number)
print(f"Number {converted_to_string} is now a string.")
print(type(converted_to_string))

float_number = 3.6
coverted_to_int = int(float_number)
print(f"Float {float_number} is coverted to integer {coverted_to_int}.")
print(type(coverted_to_int))

string_number = "9.6"
coverted_to_float = float(string_number)
print(f"String {string_number} is coverted to float {coverted_to_float}.")
print(type(coverted_to_float))

#Booleans is the things that result turns into two answer as True and False
#If the answer contains the value or something will show as True
#If it not contain anything like 0,None or empty list will show as False.

print(bool(0)) #False

# == will be equal
# != will be not equal to

#Logical operators 
#and : must be true in both conditions
#or : can be true in one condition
#not : inverted of the result

#Membership test
#in : True if it can found in the sequence 
#not in : True if the values not in the sequence 

print("Apple" in fruits)
print("Durian" not in fruits)

if number > 40:
    print("The number is greater than 40")
elif number > 30:
    print("The number is greater than 30 but not greater than 40")
else:
    print("The number is 30 or less.")

if age >= 25:
    print("You are older than or equals to 25 years old")
else:
    print("You are younger than 25 years old")

score = 55

if score >= 70:
    grade = 'Distinction'
elif score >= 60:
    grade = "Merit"
elif score >= 50:
    grade = "Pass"
else:
    grade = "Fail"
print(f"Your grade is {grade}.")

# While Loop is the loop that allows code to run repeatly based on given condition
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

#Infinite Loops 
#while True:
    #print("This will never end!")

#Exit Loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("Loop ended.")

count = 3
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)

for fruit in fruits:
    print(fruit)
    print("Fruit is delicious!")

print("All fruits have been printed") #This line is not a part of loop

my_list = [1, "Hello", 3.14]
print(my_list)

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

print(my_list[0]) #Output: 1 (first item)
print(my_list[1]) #Output: "Hello" (second item)

print(my_list[-1]) #Output: "3.14" (last item)
print(my_list[-2]) #Output: "Hello" (second last item)

print(nested_list[0]) # Output : [1,2,3]
print(nested_list[0][0]) #Output : 1

print(fruit[2])
number_list = [10,20,30]
sum = number_list[0] + number_list[1] #Add 10 and 20

list_length = len(fruits)
print(list_length) 

#Add element into list
fruits.append("mango")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

other_fruits = ["grape", "cherry"]
fruits.extend(other_fruits)
print(fruits)

#Remove element in the list
fruits.remove("kiwi")
print(fruits)

removed_fruits = fruits.pop(1)
print(removed_fruits) #Output = second fruits 

fruits.clear()
print(fruits) #Output : []

print(number)

numbers = [3,1,4,1,5,9,2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers) #List has change to sorted order
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)

numbers.reverse()
print(numbers)

fruits = ["apple","kiwi","orange","Cherry","Mango","grape","pineapple","banana"]
fruits.sort(key=len)
print(fruits)

#Range
for i in range(5):
    print(i) #Output : 0,1,2,3,4

for i in range (2,6):
    print(i) #Output : 2,3,4,5

for i in range (0,10,2): #Range(start, stop, step)
    print(i) #Output : 0,2,4,6,8

numbers = range(5)
print(numbers)
#Output: range(0,5)

numbers = list(range(5))
print(numbers)
#Output : [0,1,2,3,4]

numbers = [1,2,3,4,5]
smallest_number = min(numbers)
largest_number = max(numbers)
print(smallest_number)
print(largest_number)

squared_numbers = [x**2 for x in numbers]
print(squared_numbers) #Output = [1, 4, 9, 16, 25]

even_numbers = [x for x in numbers if x%2 == 0]
print(even_numbers)

parity = ["even" if x%2 == 0 else "odd" for x in numbers]
print (parity)

first_three = numbers[:3]
last_three = numbers[-3:]
print(first_three)
print(last_three)

numbers = [0,1,2,3,4,5,6,7,8,9]
every_second = numbers[::2]
print(every_second)

reversed_numbers = numbers[::-1]
print(reversed_numbers)











