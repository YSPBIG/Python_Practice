def get_month_number(month): #To list down the month as the number because we cannot compare the string as the date 
    months = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    return months #Make this as the number of each month to compare the amount with each other as value integer.

def convert_to_comparable_date(date):
    day, month = date.split() #Split the date and month separately, this will help to compare the month first that if it is same so we will see the date
    day = int(day[:-2])  # Remove 'th' and convert to integer as -2 is to cut the last two characters which will remain only the amount of number
    month = get_month_number(month)
    return day, month

def date_passed(todays_date, scheduled_date):
    # Convert date strings to a comparable format, Make each definition of today and schedule date.
    today_day, today_month = convert_to_comparable_date(todays_date) 
    scheduled_day, scheduled_month = convert_to_comparable_date(scheduled_date)

    # Compare dates
    if (scheduled_month, scheduled_day) < (today_month, today_day): #In case that today case is already pass which has greater value
        print("Scheduled date has passed.")
    elif (scheduled_month, scheduled_day) == (today_month, today_day): #In case that it has the same value
        print("Scheduled date is today.")
    else: #For others scenarios, it will fall into the date that already pass.
        print("Scheduled date is yet to pass.")
    

print(date_passed("26th March", "25th March"))  
print(date_passed("26th March", "26th March")) 
print(date_passed("26th March", "27th March")) 