class Rectangle:

    def __init__(self, first, second):
        self.first_coor = first
        self.second_coor = second
        self.horizontal_line = round(abs(first[0] - second[0]), 2)
        self.vertical_line = round(abs(first[1] - second[1]), 2)

    def perimeter(self):
        return round((self.horizontal_line + self.vertical_line) * 2, 2) 

    def area(self):
        return round(self.horizontal_line * self.vertical_line, 2) 
    
    def get_pos(self):
        return (round(min(self.first_coor[0], self.second_coor[0]), 2), 
                round(max(self.first_coor[1], self.second_coor[1]), 2))
    
    def get_size(self):
        return (round(self.horizontal_line, 2), 
                round(self.vertical_line, 2))
    
    def move(self, dx, dy):
        self.first_coor = (round(self.first_coor[0] + dx, 2), round(self.first_coor[1] + dy, 2))
        self.second_coor = (round(self.second_coor[0] + dx, 2), round(self.second_coor[1] + dy, 2))
    
    def resize(self, width, height):
        if self.first_coor[0] > self.second_coor[0]:
            self.first_coor = (width + self.second_coor[0], self.first_coor[1])
        else:
            self.second_coor = (width + self.first_coor[0], self.second_coor[1])
        if self.first_coor[1] < self.second_coor[1]:
            self.first_coor = (self.first_coor[0], self.second_coor[1] - height)
        else:
            self.second_coor = (self.second_coor[0], self.first_coor[1] - height)
        self.horizontal_line = width
        self.vertical_line = height

    def turn(self):
        self.first_coor = (self.first_coor[1], self.first_coor[0])
        self.second_coor = (self.second_coor[1], self.second_coor[0])
        self.horizontal_line, self.vertical_line = self.vertical_line, self.horizontal_line

    def scale(self, factor):
        self.horizontal_line *= factor
        self.vertical_line *= factor
        self.first_coor = (round(self.first_coor[0] - self.first_coor[0] * factor / 2, 2), 
                           round(self.first_coor[1] + self.first_coor[1] * factor / 2, 2))
        self.second_coor = (round(self.second_coor[0] + self.second_coor[0] * factor / 2, 2),
                            round(self.second_coor[1] - self.second_coor[1] * factor / 2, 2))
    