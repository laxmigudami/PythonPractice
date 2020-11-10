


class Bank:
    B_Name = "SBI"
    ROI = "12"
    MBL = "DELHI"

    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.phone = args[1]
        self.email = args[2]
        self.bal = kwargs.get('bal', 0)
        
    def display(self,):
        print("name is", self.name)
        print("phone is", self.phone)
        print("email is", self.email)
        print("balance is", self.bal)

    def deposit(self, amt=0):
        if amt == 0:
            amt = self.get_amt()
        self.bal = self.add(self.bal + amt)
        print("depositted successfully")

    def withdrow(self, amt):
        if amt > self.bal:
            print("insufficient balance")
            return self.bal
        self.bal = self.sub(self.bal, amt)
        print("withdrawal is successful")
        print("remaining balance is", self.bal)

    @classmethod
    def modify_bank_name(cls, newname):
        cls.B_Name = newname
        print("bank name has changed successfully")

    @staticmethod
    def get_amt():
        amt = int(input("enter the amount:"))

    @staticmethod
    def add(a,b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


Preksha = Bank("preksha", "9108780649","pre@gmail.com", bal=2000)
Laxmi = Bank("laxmi", "9743692132", "laxmi@gmail.com")

print(Bank.ROI)
print(Preksha.ROI)
print(Preksha.modify_bank_name('sbm'))
print(Preksha.B_Name)
print(Preksha.display())

