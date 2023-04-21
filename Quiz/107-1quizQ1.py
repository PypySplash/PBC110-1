x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

area = (x2 - x1) * (y2 - y1)

if x2 - x1 == y2 - y1:
    print(1, area)
else:
    print(0, area)
