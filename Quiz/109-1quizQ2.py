p1p2dn_list = input().split(',')
p1 = int(p1p2dn_list[0])
p2 = int(p1p2dn_list[1])
d = int(p1p2dn_list[2])
n = int(p1p2dn_list[3])
xi_list = input().split(',')

total = 0
q1 = 0
q2 = 0

for i in range(n):
    xi = int(xi_list[i])
    if xi == 1:
        total += p1
        q1 += 1
    if xi == 2:
        total += p2
        q2 += 1
    if xi == 3 and p1 + p2 - d >=0 :
        total += p1 + p2 -d
        q1 += 1
        q2 += 1
    if xi == 3 and p1 + p2 - d < 0:
        q1 += 1
        q2 += 1

print(q1, q2, total, sep=',')
