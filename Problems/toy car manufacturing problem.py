n = int(input())
t = int(input())
q1 = int(input())
q2 = int(input())
left1 = 480
left2 = 480
tot_rev = 0
lst = [-1]

for i in range(1, n+1):
    x = int(input())
    p = int(input())
    if p // x >= t and left1 - q1 * x >= 0 and left2 - q2 * x >= 0:
        tot_rev += p
        left1 = left1 - q1 * x
        left2 = left2 - q2 * x
        lst.append(i)

if len(lst) > 1:
    lst.remove(-1)
    print(*lst, sep = ",")
    print(left1, left2, tot_rev, sep = ",")
else:
    print(*lst, sep = ",")
    print(left1, left2, tot_rev, sep = ",")
