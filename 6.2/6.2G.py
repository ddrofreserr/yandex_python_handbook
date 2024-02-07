import pandas as pd 


with open('data.csv', encoding='UTF8') as file:
    data = pd.read_csv(file)
    left = input().split()
    right = input().split() 
    data = data[left[0] <= data['x']][right[1] <= data['y']] 
    data = data[right[0] >= data['x']][left[1] >= data['y']]
    print(data)
