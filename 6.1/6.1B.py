import math
from sys import stdin


def gcdlisted(nums):
    gcd = nums.pop()
    while len(nums):
        gcd = math.gcd(nums.pop(), gcd)
    return gcd


def main():
    for line in stdin:
        print(gcdlisted((list(int(each) for each in line.split(' ')))))


if __name__ == "__main__":
    main()
    