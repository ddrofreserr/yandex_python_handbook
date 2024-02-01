import math


def geometric(list):
    return math.pow(math.prod(list), 1 / len(list))


def main():
    print(geometric(list(float(each) for each in input().split())))


if __name__ == "__main__":
    main()
    