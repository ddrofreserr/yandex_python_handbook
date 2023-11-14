class Programmer:

    def __init__(self, name, post):
        self.name = name
        self.hours = 0
        self.post = post
        self.total_wage = 0
        if post == 'Junior':
            self.wage_ph = 10
        elif post == 'Middle':
            self.wage_ph = 15
        else:
            self.wage_ph = 20

    def work(self, time):
        self.hours += time
        self.total_wage += self.wage_ph * time

    def rise(self):
        if self.post == 'Junior':
            self.post = 'Middle'
            self.wage_ph += 5
        elif self.post == 'Middle':
            self.post = 'Senior'
            self.wage_ph += 5
        else:
            self.wage_ph += 1

    def info(self):
        return f'{self.name} {self.hours}ч. {self.total_wage}тгр.'
