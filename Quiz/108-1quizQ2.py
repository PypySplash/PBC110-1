n = int(input())
x_list = input().split(',')
Sp = 0
Sn = 0

for i in range(n):
    x = int(x_list[i])
    if x > 0:
        Sp += x
    if x < 0:
        Sn += x

if Sp + Sn == 0:
    print(1, Sp, -Sn, sep=',')
if Sp + Sn != 0:
    print(0, Sp, -Sn, sep=',')
