def speeding_ticket(speed, is_birthday):

    #the boundaries of charging in each speed
    no_charged_ticket = 60
    small_max_ticket = 80

    #In case of the birthday, the maximum will increase the limit around 5
    if is_birthday:
        no_charged_ticket += 5 #For No Ticket case
        small_max_ticket += 5 # For Small Ticket case

    if speed <= no_charged_ticket: #For the less than 60 and 65 max will have no ticket
        return("No Ticket")
    elif no_charged_ticket <= speed <= small_max_ticket: #For the range within the ceiling speed for each one
        return("Small Ticket") 
    else: #For all leftover case will be charge as Big Ticket
        return("Big Ticket") 

print(speeding_ticket(60, False))
print(speeding_ticket(75, False))  
print(speeding_ticket(85, False))
print(speeding_ticket(65, True))  
print(speeding_ticket(85, True))