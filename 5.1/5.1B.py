class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

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
            super().__init__(0, 0)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __repr__(self):
        return f'PatchedPoint{self.__str__()}'
    
    def __add__(self, coords):
        return (self.x + coords[0], self.y + coords[1])
    
    def __iadd__(self, coords):
        self.x += coords[0]
        self.y += coords[1]
        return self

point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)


first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
