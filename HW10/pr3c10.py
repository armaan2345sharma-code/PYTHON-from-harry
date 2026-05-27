class train:
    @staticmethod
    def print_welcome():
        print("WELCOME TO INDIAN RAILWAY ")
    def __init__(self,name,fair,seat):
        self.name=name
        self.fair=fair
        self.seat=seat
    def get_details(self):
        print(f"train is {self.name}")
        print(f"Train is {self.fair}")
        print(f"Seats left {self.seat}")
    def book_ticket(self):
        if self.seat>0:
            print("Ticket Booked")
            self.seat-=1
        else:
            print("Nothing left")
intrancity= train("Rajdhani Express", 1500, 100)
intrancity.print_welcome()
intrancity.get_details()
intrancity.book_ticket()
intrancity.get_details()