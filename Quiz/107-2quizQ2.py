n = int(input())
p_list = input().split(',')
q_list = input().split(',')
c_list = input().split(',')

max_profit_1 = 0

for i in range(n):
    p = int(p_list[i])
    q = int(q_list[i])
    c = int(c_list[i])
    profit = (p - c) * q
    if profit > max_profit_1:
        max_profit_1 = profit

max_profit_2 = 0

for i in range(n):
    p = int(p_list[i])
    q = int(q_list[i])
    c = int(c_list[i])
    profit = (p - c) * q
    if profit > 0:
        max_profit_2 += profit

print(max_profit_1, max_profit_2)
