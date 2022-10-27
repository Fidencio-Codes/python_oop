class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to", self.password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
    def check_balance(self):
        print(self.name, "has account a balance of: $",self.balance)

bankuser1 = BankUser("Mary", "mary@nucamp.co", "bestpassword")

BankUser.change_password = 123
print(BankUser.change_password)
# remember this is the constructor method when using __ini__
# defining an instance method on a class