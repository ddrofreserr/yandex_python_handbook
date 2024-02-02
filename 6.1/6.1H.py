import numpy as np


def snake(M, N, direction='H'):

    if direction == 'H':
        snake = np.zeros((N, M), dtype='int8')
        for i in range(N):
            if i % 2:
                snake[i] = np.arange((i + 1) * M, i * M, -1)
            else:
                snake[i] = np.arange(i * M + 1, (i + 1) * M + 1)

    else:
        snake = np.zeros((M, N), dtype='int8')
        for i in range(M):
            if i % 2:
                snake[i] = np.arange(i * N + 1, (i + 1) * N + 1)
            else:
                snake[i] = np.arange((i + 1) * N, i * N, -1)
        snake = np.rot90(snake)
    
    return snake


def main():
    print(snake(5, 3))


if __name__ == "__main__":
    main()
