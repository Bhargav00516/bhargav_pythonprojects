class RailwayTicketSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.booked_tickets = 0
    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Invalid number of tickets.")
        elif number_of_tickets > self.available_seats:
            print("Not enough seats available.")
        else:
            self.available_seats -= number_of_tickets
            self.booked_tickets += number_of_tickets
            print("Successfully booked {number_of_tickets} ticket(s).")
    def cancel_ticket(self, number_of_tickets):
        if number_of_tickets <= 0:
            print("Invalid number of tickets.")
        elif number_of_tickets > self.booked_tickets:
            print("Cannot cancel more tickets than booked.")
        else:
            self.available_seats += number_of_tickets
            self.booked_tickets -= number_of_tickets
            print("Successfully cancelled {number_of_tickets} ticket(s).")
    
    def check_availability(self):
        print("Available seats: {self.available_seats}")
        print("Booked tickets: {self.booked_tickets}")

# Example usage
if __name__ == "__main__":
    # Initialize system with 100 seats
    system = RailwayTicketSystem(100)
    
    while True:
        print("\nRailway Ticket System")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Check Availability")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            num_tickets = int(input("Enter number of tickets to book: "))
            system.book_ticket(num_tickets)
        elif choice == '2':
            num_tickets = int(input("Enter number of tickets to cancel: "))
            system.cancel_ticket(num_tickets)
        elif choice == '3':
            system.check_availability()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
