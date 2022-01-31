class Parking_Garage():
    def __init__(self, spaces_available=list(range(1, 21)), tickets_available=list(range(1, 21)), leavegarage={}, taken_spots=[]):

        self.tickets = tickets_available
        self.spaces = spaces_available
        self.leavegarage = leavegarage
        self.taken_spots = taken_spots
        # self.current_ticket = False
        # self.running = True
        # insert logic here


# define functions below

# ---- take ticket function.


    def take_ticket(self):
        # decrease the amount of tickets available by 1
        # As long as there are tickets available, one is distributed.
        if (len(self.tickets)) > 0:
            (print(f"\nTake a ticket"))
            # assign the last ticket number to a variable which is given to the customer as their space number.
            space_number = self.tickets.pop()
            print(f"Please make your way to space number {space_number}. Don't lose your ticket!")
            self.taken_spots.append(space_number)
            # add the newly distributed space to an empty list which stores the taken spots.
            self.leavegarage[space_number] = "unpaid"  # set the value in leavegarage dict to unpaid
        else:
            (len(self.tickets)) == 0
            print("This lot is full. Please come back later.")
            return

    # decrease the amount of space available by 1
        # if (len(self.spaces)) > 0:
        #     self.spaces.pop()
        #     print("Spaces remaining: ")
        #     print(f"{len(self.spaces)}")

    # pay for parking function

    def pay_for_parking(self):
        running = True
        while True:
            # - Display an input that waits for an amount from the user and store it in a variable

            space_number = int(input("\nWhat space number are you parked in? "))
            if space_number not in self.spaces:
                print("\nWe do not have that number in our garage. Please try again! ")
                running = True
            elif space_number in self.taken_spots:
                print("\nGot it! Please note that this garage only takes card payments. ")
                self.leavegarage[space_number] = "paid"
                print(f"Thanks for staying, please make your way to the exit. Leave us a great review on Yelp!")
                break
            elif space_number not in self.taken_spots:
                input("\nWe believe this is the wrong space number. Press any key to continue. ")
                running = True

                # running = False

    def leave_garage(self):
        print("\nThanks for staying at Jiffy Park! Whatever rumors you have heard about us are not true and we hope to see you soon!")
        ticket = int(input("Please input your space number. "))
        if ticket not in self.spaces:
            int(input("That number is not in our parking garage. Please enter a valid space number! "))
        elif self.leavegarage[ticket] == "paid":
            self.tickets.append(ticket)
            del self.leavegarage[ticket]
            print("\nThank you, have a nice day!")
        else:
            warning =input("\nOur records show you have not paid your ticket! If you would like to pay press Y, if not press N. ").lower()
            if warning == "n":
                print("Please return to your assigned space number, or else!")
            elif warning == "y":
                self.pay_for_parking()

    def our_garage(self): #final function run all our code together
            while True:
                question = input(
                    "\nWelcome to Jiffy Park! Would you like to park (P), pay (Pay), or leave garage (L)? ").lower()
                if question == 'p':
                    self.take_ticket()
                elif question == 'pay':
                    self.pay_for_parking()
                elif question == 'l':
                    self.leave_garage()

 
            #original our_garage function was longer, made it more concise by combining all 3 functions into one question.
            #     print("Have a nice day! Come again soon!")
            #     return
            # running = True
            # while running:
            #     follow_up = input(
            #         "Would you like to pay for ticket (P) or leave garage (L)? ").lower()
            #     if follow_up == 'p':
            #         self.pay_for_parking()
            #         break
            #     elif follow_up == 'l':
            #         print("You have not paid yet! ")
            #         running = False


p = Parking_Garage()
# p.take_ticket()
# p.pay_for_parking()
# p.leave_garage()

p.our_garage()

