import task2

class Rectangle(task2.Shape):
    def __init__(self, l, w):
        task2.Shape.__init__(self)
        self.l = l
        self.w = w
    def area(self):
        return self.l*self.w

r = Rectangle(4, 5)
# print(r.area())
