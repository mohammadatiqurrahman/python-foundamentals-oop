class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width*self.height)

rctgl_1 = Rectangle(5,5)
rctgl_2 = Rectangle(10,20)
rctgl_1.area()
rctgl_2.area()
    