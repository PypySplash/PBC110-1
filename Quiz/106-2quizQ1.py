a = int(input())
b = int(input())
c = int(input())

tri = 0

if c >= b and c >= a:
    if a + b > c:
        if a ** 2 + b ** 2 == c ** 2:
            tri = 2
        if a ** 2 + b ** 2 > c ** 2:
            tri = 1
        if a ** 2 + b ** 2 < c ** 2:
            tri = 3

if b >= a and b>= c:
    if a + c > b:
        if a ** 2 + c ** 2 == b ** 2:
            tri = 2
        if a ** 2 + c ** 2 > b ** 2:
            tri = 1
        if a ** 2 + c ** 2 < b ** 2:
            tri = 3

if a >= b and a >= c:
    if b + c > a:
        if b ** 2 + c ** 2 == a ** 2:
            tri = 2
        if b ** 2 + c ** 2 > a ** 2:
            tri = 1
        if b ** 2 + c ** 2 < a ** 2:
            tri = 3

tri_len = a + b + c

print(tri, tri_len)
