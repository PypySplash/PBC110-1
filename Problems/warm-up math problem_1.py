x = int(input())
y = int(input())

a = x + y
b = abs(x-y)

num = 0

if a % 2 != 0:
    num += 1
if b % 2 != 0:
    num += 1

print(num)
