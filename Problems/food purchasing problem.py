nm_list = input().split(',')
n = int(nm_list[0])
m = int(nm_list[1])

p_list = input().split(',')
x_list = input().split(',')
q_list = input().split(',')

money = 0

for i in range(n):
    p = int(p_list[i])
    x = int(x_list[i])
    money += p * x

for j in range(m):
    q = int(q_list[j])
    if money >= q:
        money -= q

print(money)
