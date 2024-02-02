import math


def convert(coords):
    r, phi = coords[0], coords[1]
    return r * math.cos(phi), r * math.sin(phi)


def main():
    dek = tuple(float(each) for each in input().split())
    pol = convert(list(float(each) for each in input().split()))
    print(math.dist(dek, pol))


if __name__ == "__main__":
    main()
    