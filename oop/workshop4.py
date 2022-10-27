class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin 
        self.password = password
    def change_name(self, name): 
        self.name = name
        print("Your name has been changed to", self.name)
    def change_pin(self, pin):
        self.pin = pin
        print("Your pin has been changed to", self.pin)
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.00
        self.amt = 0.00
    def show_balance(self):
        print(self.name, "has an account balance of: $",self.balance) 
    def withdraw(self, withdraw_amt):
        self.balance -= withdraw_amt if withdraw_amt >= 0.00 else print("Cannot use negative numbers.")
    def deposit(self, deposit_amt):
        self.balance += deposit_amt if deposit_amt >= 0.00 else print("Cannot use negative numbers.")
    def transfer_money(from_acc, to_acc, amt):
        if amt <= 0.00: print("Cannot use negative numbers.")
        print(f"\nYou are transferring ${amt} to {to_acc.name}")
        print("Authentication Required")
        print(f"Enter your PIN: {from_acc.pin}")
        if from_acc.pin == from_acc.pin:
            print("Transfer authorized")
            from_acc.withdraw(amt)
            to_acc.deposit(amt)
            return True
        if from_acc.pin != from_acc.pin: print("Invalid PIN. Transaction cancelled.")  
        return False
    def request_money(from_acc, to_acc, amt):
        if amt <= 0.00: print("Cannot use negative numbers.")
        print(f"\nYou are requesting ${amt} from {to_acc.name}")
        print("User authentication is required...")
        print(f"Enter {to_acc.name}'s PIN: {to_acc.pin}")
        print(f"Enter your password: {from_acc.password}")
        if to_acc.pin == to_acc.pin and from_acc.password == from_acc.password:
            print("Request Authorized")
            from_acc.deposit(amt)
            to_acc.withdraw(amt)
            print(f"{to_acc.name} sent ${amt}")
            return True
        if to_acc.pin != to_acc.pin: print("Invalid PIN. Transaction cancelled")
        if from_acc.password != from_acc.password: print("Invalid password. Transaction cancelled")
        if from_acc.password != from_acc.password and to_acc.pin != to_acc.pin: print("Invalid password and PIN. Transaction cancelled")
        return False


"""Driver Test code for task 1"""
# test_code = User("Gerardo", 1234, "bestpw")
# print(test_code.name, test_code.pin, test_code.password)

"""Driver Test code for task 2"""
# joe = User("Joe", 4321, "Betterpassword1")
# print(joe.name, joe.pin, joe.password)
# joe.change_name = "Joey"
# joe.change_pin = 1324
# joe.change_password = "Supr3mePW#"
# print(joe.change_name, joe.change_pin, joe.change_password)

""" Driver Code for Task 3"""
# bob = BankUser("Bob", 1993, "P@ssw0rd666!$")
# print(bob.name, bob.pin, bob.password, bob.balance)
# print(dir(bob))
# print(help(bob))

"""Driver code for Task 4"""
# bob = BankUser("Bob", 1993, "P@ssw0rd666!$")
# bob.show_balance()
# bob.deposit(1000.00)
# bob.show_balance()
# bob.withdraw(200.00)
# bob.show_balance()

"""Driver code for Task 5"""
bob = BankUser("Bob", 1993, "P@ssw0rd666!$")
alice = BankUser("Alice", 4321, "Betterpassword1") #second user
alice.deposit(5000)
alice.show_balance()
bob.show_balance()
successful = alice.transfer_money(bob, 500)
alice.show_balance()
bob.show_balance()
if successful:
    alice.request_money(bob, 250)
alice.show_balance()
bob.show_balance()
