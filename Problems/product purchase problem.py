money = int(input())
jua = int(input())
gtea = int(input())

if money - jua >= 0:
    left1 = money - jua
else:
    left1 = money

if left1 - gtea >= 0:
    left2 = left1 - gtea
else:
    left2 = left1

print(left2)
