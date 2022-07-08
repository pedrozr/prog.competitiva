from math import  sqrt, pow
ent = input('')
ent2 = input('')

x1 = float(ent.split(' ')[0])
x2 = float(ent.split(' ')[1])
y1 = float(ent2.split(' ')[0])
y2 = float(ent2.split(' ')[1])

print(sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)))
