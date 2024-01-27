def is_leap_year(year):

    if year % 4 == 0 and year % 100 != 0: #If the year can divided by 4 and no remainder, also the year that is century = able to divided by 100
        return True
    elif year % 400 == 0: #those year should be divided by 400 with no remiander. 
        return True
    else:
        return False

print(is_leap_year(2020))  
print(is_leap_year(1900))  
print(is_leap_year(2000))  
print(is_leap_year(2019))  