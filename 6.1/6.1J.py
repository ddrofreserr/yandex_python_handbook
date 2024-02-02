import numpy as np


def stairs(vect):
    size = len(vect)
    stair = np.zeros((size, size), dtype=vect.dtype)
    for i in range(size):
        stair[i] = np.hstack((vect[-i:], vect[:-i]))
    return stair


def main():
    print(stairs(np.arange(3)))


if __name__ == "__main__":
    main()
