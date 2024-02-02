import numpy as np


def multiplication_matrix(N):
    linear = np.arange(1, N + 1)
    linear.resize(N, 1)
    return linear * linear.transpose()


def main():
    print(multiplication_matrix(int(input())))


if __name__ == "__main__":
    main()
    