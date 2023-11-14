class Checkers:

    def __init__(self):
        self.alpha_stroke = 'ABCDEFGH'
        self.desk = [[Cell('W') if (i + j) % 2 == 0 else Cell('X') for i in range(8)] for j in range(3)]
        self.desk += [[Cell('X') for i in range(8)] for j in range(2)]
        self.desk += [[Cell('B') if (i + j) % 2 == 1 else Cell('X') for i in range(8)] for j in range(3)]

    def get_cell(self, coor):
        return self.desk[int(coor[1]) - 1][self.alpha_stroke.index(coor[0])]

    def move(self, f, t):
        self.get_cell(t).change_status(self.get_cell(f).status())
        self.get_cell(f).change_status()


class Cell:

    def __init__(self, stat):
        self.stat = stat

    def status(self):
        return self.stat
    
    def change_status(self, stat='X'):
        self.stat = stat
