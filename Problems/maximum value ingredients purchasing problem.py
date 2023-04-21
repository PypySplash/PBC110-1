nm = input().split(',')
n = int(nm[0])
m = int(nm[1])
pList = input().split(',')
xList = input().split(',')
qList = input().split(',')

q = []

for i in range(len(qList)):
    q.append(int(qList[i]))

earnings = 0

for i in range(n):
    p = int(pList[i])
    x = int(xList[i])
    earnings += p * x

maxSpend = 0
from itertools import combinations

for i in range(1, len(q)+1):
    listQ = list(combinations(q, i))
    for j in range(len(listQ)):
        spendMoney = 0
        for k in range(len(listQ[j])):
            spendMoney += int(listQ[j][k])
        if spendMoney > maxSpend and spendMoney <= earnings:
            maxSpend = spendMoney

print(earnings - maxSpend)
