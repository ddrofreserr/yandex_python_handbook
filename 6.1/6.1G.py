import numpy as np


def make_board(dim):
    board = np.ones(dim ** 2, dtype='int8')
    for i in range(1, (dim ** 2)):
        if bool((i // dim) % 2) is not bool((i % dim) % 2):
            board[i] = 0
    return board.reshape(dim, dim)


def main():
    print(make_board(int(input())))


if __name__ == "__main__":
    main()
