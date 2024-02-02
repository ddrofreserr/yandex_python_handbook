import math


def func(x):
    return (math.log(math.pow(x, 3 / 16), 32) + 
            math.pow(x, math.cos((math.pi * x) / (math.e * 2))) - 
            math.pow(math.sin(x / math.pi), 2))


def main():
    print(func(float(input())))


if __name__ == "__main__":
    main()
    