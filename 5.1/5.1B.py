class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def get_coordinats(self):
        return (self.x, self.y)

    def length(self, second_point):
        compare = second_point.get_coordinats()
        return round(((self.x - compare[0]) ** 2 + (self.y - compare[1]) ** 2) ** 0.5, 2)
    