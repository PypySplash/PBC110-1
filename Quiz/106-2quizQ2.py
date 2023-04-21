n = int(input())
p_list = input().split(',')
q_list = input().split(',')
cK = input().split(',')
c = int(cK[0])
K = int(cK[1])

max_profit = 0

for i in range(n):
    p = int(p_list[i])
    q = int(q_list[i])
    if q > K:
        q = K
    profit = (p - c) * q
    if profit > max_profit:
        max_profit = profit
        best_price = p
        method = i+1
        best_q = q
    if profit == max_profit and q > best_q:
        method = i+1
        best_price = p

print(best_price, max_profit)
