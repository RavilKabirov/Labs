class streng():
    def getString(self, integ):
        self.integ = integ
    def printString(self):
        print(self.integ.upper())
s = streng()
s.getString("вао")
s.printString()