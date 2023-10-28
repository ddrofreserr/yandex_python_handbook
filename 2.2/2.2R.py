a = int(input())
b = int(input())
c = int(input())
alfa = (c * c + b * b - a * a) / (2 * c * b) 
beta = (a * a + c * c - b * b) / (2 * a * c) 
gamma = (a * a + b * b - c * c) / (2 * a * b) 
if alfa == 0 or beta == 0 or gamma == 0:
    print('100%')
elif alfa < 0 or beta < 0 or gamma < 0:
    print('велика')
else:
    print('крайне мала')
