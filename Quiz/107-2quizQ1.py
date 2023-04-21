x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

TF = 0

if y2 >= y1:
    m1 = (y2 - y1) / (x2 - x1)
else:
    m1 = (y1 - y2) / (x2 - x1)

if y3 >= y2:
    m2 = (y3 - y2) / (x3 - x2)
else:
    m2 = (y2 - y3) / (x3 - x2)

if m1 == m2:
    TF = 1

if y2 > y1 and y2 > y3:
    print(TF, 2)
if y1 > y2 and y1 > y3:
    print(TF, 1)
if y3 > y1 and y3 > y2:
    print(TF, 3)
