import math
from fractions import Fraction


def main():
    NM = input().split(' ')
    all = math.comb(int(NM[0]), int(NM[1]))
    pos = all * Fraction(int(NM[1]), int(NM[0]))
    print(pos, all)


if __name__ == "__main__":
    main()
    