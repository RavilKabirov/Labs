class bankaccount:
    def __init__(self, owner):
        self.owner = owner
        self.mone = 0
    def deposit(self, z):
        self.mone += z
    def withdraw(self, x):
        if(x > self.mone):
            print("No mone!")
        else:
            self.mone -= x
            print("Ostalos", self.mone)
s = bankaccount("Boba")
s.withdraw(5000)
s.deposit(10000)
s.withdraw(9999)
