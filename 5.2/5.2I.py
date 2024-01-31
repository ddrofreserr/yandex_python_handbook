def gcd(first, second):
    first, second = max(first, second), min(first, second) 
    while (first % second != 0) and 0 < second < first:
        first, second = second, first % second
    return second


class Fraction:

    def __init__(self, fr, sc=1):

        if isinstance(fr, str):
            if '/' in fr:
                fr, sc = int(fr.split('/')[0]), int(fr.split('/')[1])
            else:
                fr = int(fr)

        self.numer = fr
        self.denum = sc
        self.__sign__()

        if gcd(abs(self.numer), self.denum) != 1:
            self._reduce()
            
    def __sign__(self):
        if self.denum / self.numer < 0:
            self.numer = -abs(self.numer)
            self.denum = abs(self.denum)
        elif self.denum < 0:
            self.numer = abs(self.numer)
            self.denum = abs(self.denum)
    
    def numerator(self, new_num=None):

        if new_num:
            if self.numer < 0:
                self.numer = -new_num
            else:
                self.numer = new_num

            if gcd(abs(self.numer), self.denum) != 1:
                self._reduce()

        return abs(self.numer)
    
    def denominator(self, new_num=None):

        if new_num:
            self.denum = new_num
            self.__sign__()

            if gcd(abs(self.numer), self.denum) != 1:
                self._reduce()

        return abs(self.denum)
    
    def _reduce(self):

        div = gcd(abs(self.numer), self.denum)
        self.numer //= div
        self.denum //= div

    def __str__(self):
        return f'{self.numer}/{self.denum}'
    
    def __repr__(self):
        return f'Fraction(\'{self.numer}/{self.denum}\')'
    
    def __neg__(self):
        return Fraction(-self.numer, self.denum)
    
    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numer * other.denum + other.numer * self.denum, self.denum * other.denum)
    
    def __radd__(other, self):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numer * other.denum + other.numer * self.denum, self.denum * other.denum)
    
    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.numer = self.numer * other.denum + other.numer * self.denum
        self.denum *= other.denum
        if gcd(abs(self.numer), self.denum) != 1:
            self._reduce()
        return self
    
    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numer * other.denum - other.numer * self.denum, self.denum * other.denum)

    def __isub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.numer = self.numer * other.denum - other.numer * self.denum
        self.denum *= other.denum
        if gcd(abs(self.numer), self.denum) != 1:
            self._reduce()
        return self
    
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numer * other.numer, self.denum * other.denum)
    
    def __imul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.numer *= other.numer
        self.denum *= other.denum
        if gcd(abs(self.numer), self.denum) != 1:
            self._reduce()
        self.__sign__()
        return self
    
    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return Fraction(self.numer * other.denum, self.denum * other.numer)
    
    def __itruediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        self.numer *= other.denum
        self.denum *= other.numer
        if gcd(abs(self.numer), self.denum) != 1:
            self._reduce()
        self.__sign__()
        return self
    
    def reverse(self):
        return Fraction(self.denum, self.numer)
    
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer * other.denum < other.numer * self.denum
    
    def __le__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer * other.denum <= other.numer * self.denum
    
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer * other.denum > other.numer * self.denum
    
    def __ge__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer * other.denum >= other.numer * self.denum

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer == other.numer and self.denum == other.denum
    
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other, 1)
        return self.numer != other.numer and self.denum != other.denum
