class Rectangle:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def get_area(self):
        area = self.height*self.width
        return area


rec1 = Rectangle(20, 10)
rec2 = Rectangle(10, 10)

print(rec1.get_area())
print(rec2.get_area())
