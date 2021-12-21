class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()


image_one = ImageArea(10, 10)
image_two = ImageArea(10, 10)
print(image_one < image_two)
print(image_one <= image_two)
print(image_one > image_two)
print(image_one >= image_two)
print(image_one == image_two)
print(image_one != image_two)

