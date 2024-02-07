import pandas as pd 


with open('data.csv') as file:
    board = pd.read_csv(file)
    x1, y2 = map(int, input().split())
    x2, y1 = map(int, input().split())
    print(board[(board['x'] >= x1) & (board['y'] >= y1) & (board['x'] <= x2) & (board['y'] <= y2)])
    