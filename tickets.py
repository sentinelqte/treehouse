TICKET_PRICE = 10

tickets_remaining = 100  

#run until tics gone
while tickets_remaining >=1:
    print("There are {} tickets remaining." .format(tickets_remaining))
    name = input("What is your name?    ")
    num_tickets = input("How many tickets would you like, {} ?   ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There is only {} tickets ramining".format(tickets_remaining))
    except ValueError as err:  
        print("We ran into an issue. {}. Pleae try again".format(err))  
    else:    
        amount_due = num_tickets * TICKET_PRICE
        print("The total due is {}".format(amount_due))
        should_proceed = input("Do you want to proceed?   Y?N  ")
        if should_proceed.lower() == "y":
            print("SOlD!")
            tickets_remaining -= num_tickets    
        else: 
            print("Thank you anyways, {}!".format(name))

#notify a sold out if sold out    
print("Sorry sold out!")