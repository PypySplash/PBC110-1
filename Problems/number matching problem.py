x = int(input())
y = int(input())

a = x // 100
b = (x-a*100) // 10
c = x % 10

d = y // 100
e = (y-d*100) // 10
f = y % 10

A = int()
B = int()

if a == d:
    A += 1
if a == e:
    B += 1
if a == f:
    B += 1
if b == d:
    B += 1
if b == e:
    A += 1
if b == f:
    B += 1
if c == d:
    B += 1
if c == e:
    B += 1
if c == f:
    A += 1

print(str(A) + "A" + str(B) + "B")



"""
if a == d and b == e and c == f:
    print("3A0B")
    
if a != d and b != e and c != f:
    print("0A0B")
"""
