max = int(input())
N = int(input())
news = []
for i in range(N): 
    stroke = input()
    news.append(stroke)


for stroke in news:
    if len(stroke) < (max - 3):
        print(stroke)
        max -= len(stroke)
    else:
        print(stroke[:max - 3] + '...')
        break
