class App:
    def __init__(self):
        print("Please Fill The Following Parameters:")
        self.name = input("Company Name: ")
        self.role = input("Role: ")
        self.portal = input("Portal Name: ")
        self.location = input("Location: ")
        self.ref = input("Referrals: ")
        self.dt = input("Date in MM-DD-YY: ")
        line = self.name + "," + self.role+ "," + self.portal+ "," + self.location+ "," + self.ref+ "," + self.dt + "\n"

        with open('db.txt', 'a') as f:
            f.write(line)

        print("Form Filled Successfully!")

        

    def get_details_by_cname(self):
        cname = input("Please Enter Company Name To Find Details: ")
        
        with open("db.txt", "r") as f:
            print(f.readline())

application = App()

application.get_details_by_cname()
