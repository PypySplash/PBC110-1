x1 = int(input())
x2 = int(input())
x3 = int(input())

if x3 == x1 + x2 or x2 == x1 + x3 or x1 == x2 + x3:
    print(1)
else:
    print(0)
