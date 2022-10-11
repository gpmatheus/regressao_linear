import random

indexess = []

for i in range(50) :
    x = float(i) + random.random() * 5
    y = x + random.random() * 6
    indexess.append('{index}  {a}  {b}'.format(index=i, a=x, b=y))

with open('data.txt', 'a') as f :
    for i in indexess :
        f.write(i + '\n')
