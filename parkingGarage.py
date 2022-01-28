
class Parking_Garage():
    def __init__(self, spaces_available = list(range(1, 21)), tickets_available= list(range(1, 21)), leave_garage = {}):

        self.tickets = tickets_available
        self.spaces = spaces_available
        self.leave_garage = leave_garage
        self.current_ticket = False
        self.running = True
        #insert logic here



#define functions below

#---- take ticket function. 
    def take_ticket(self):
        self.running = False
        while not self.running:
# decrease the amount of tickets available by 1
            if (len(self.tickets)) > 0:
                (print(f"Take a ticket"))
                self.tickets.pop()
                print("Tickets remaining: ")
                print(f"{len(self.tickets)}")
                self.running = True  
            else:
                (len(self.tickets)) == 0
                print("This lot is full. ")
                return
    #decrease the amount of space available by 1
            if (len(self.spaces)) > 0:
                self.spaces.pop()
                print("Spaces remaining: ")
                print(f"{len(self.spaces)}")

    # pay for parking function
    def pay_for_parking(self):
    # - Display an input that waits for an amount from the user and store it in a variable
        payment =  (input("How are you paying today? Cash or Credit? ")).lower()
#    - If the payment variable is not empty then (meaning the ticket has been paid) ->  display a message to the user that their ticket has been paid and they have 15mins to leave
        if payment == "Cash":
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.current_ticket = True 
        elif payment == "Credit":
            print("Your ticket has been paid. You have 15 minutes to leave.")
            self.current_ticket = True 
        else:
            input("Plese enter a valid payment method. Press any key to continue. ")
#    - This should update the "currentTicket" dictionary key "paid" to True
                

    

p = Parking_Garage()
p.take_ticket()
p.take_ticket()
p.pay_for_parking()
