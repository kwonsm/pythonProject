class Rectangle:
    def __init__(self, w, l):
        self.set_dimension(w, l)

    def set_dimension(self, w, l):
        self.width = w
        self.length = l

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return (self.width+self.length)*2

    def print(self):
        print("Length = {}, Width = {}, Area = {}, Perimeter = {}".format(self.length, self.width, self.area(), self.perimeter()))


class Box(Rectangle):
    def __init__(self, w, l, h):
        self.set_dimension(w, l, h)

    def set_dimension(self, w, l, h):
        Rectangle.set_dimension(self, w, l)
        self.height = h

    def get_height(self):
        return self.height

    def area(self):
        return 2*(Rectangle.area(self) + self.height*self.length + self.height*self.width)

    def volume(self):
        return Rectangle.area(self)*self.height

    def print(self):
        print("Length = {}, Width = {}, Height = {}, Area = {}, Volume = {}".format(self.length, self.width, self.height, self.area(), self.volume()))


if __name__ == "__main__":
    r = Rectangle(10, 20)
    r.print()

    b = Box(10, 20, 10)
    b.print()
