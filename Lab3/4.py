from cmath import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, z, t):
        print(sqrt((z - self.x)**2 + (t - self.y)**2))
s = Point(4, 3)
s.show()
s.move(5, 6)
s.show()
s.dist(7, 8)