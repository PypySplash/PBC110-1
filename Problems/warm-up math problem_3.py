n = int(input())
x_list = input().split(',')
w_list = input().split(',')

y = 0
num = 0

for i in range(n):
    x = int(x_list[i])
    w = int(w_list[i])
    y += x*w

a = y // 100000
b = (y - a * 100000) // 10000 
c = (y - a * 100000 - b * 10000) // 1000
d = (y - a * 100000 - b * 10000 - c * 1000) // 100
e = (y - a * 100000 - b * 10000 - c * 1000 - d * 100) // 10
f = y % 10

if a == 1:
    num += 1
if b == 1:
    num += 1
if c == 1:
    num += 1
if d == 1:
    num += 1
if e == 1:
    num += 1
if f == 1:
    num += 1

print(y, num, sep=',')
