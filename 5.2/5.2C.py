class Point:

    def __init__(self, x=0, y=0):
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
    
    
class PatchedPoint(Point):

    def __init__(self, *args):
        if len(args) == 2:
            super().__init__(x=args[0], y=args[1])
        elif len(args) == 1:
            super().__init__(x=args[0][0], y=args[0][1])
        else:
            super().__init__()

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'PatchedPoint{self.__str__()}'
    
    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])
    
    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self
