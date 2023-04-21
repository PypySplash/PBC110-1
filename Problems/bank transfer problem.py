acc1 = int(input())
acc2 = int(input())
rate = int(input())
tran = int(input())

if acc1 - tran >= 0:
    acc1new = acc1 - tran
    acc2new = acc2 + rate*tran
else:
    acc1new = 0
    acc2new = acc2+rate*acc1

print(str(acc1new)+","+str(acc2new))
