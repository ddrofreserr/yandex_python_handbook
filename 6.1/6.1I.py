import numpy as np


def rotate(matr, ang):
    if ang <= 180:
        matr = np.rot90(matr, -1)
    if ang == 180:
        matr = np.rot90(matr, -1)
    if ang == 270:
        matr = np.rot90(matr)
    return matr


def main():
    print(rotate(np.arange(12).reshape(3, 4), 90))


if __name__ == "__main__":
    main()
