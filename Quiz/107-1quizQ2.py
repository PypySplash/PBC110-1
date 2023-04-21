npq_list = input().split(',')
n = int(npq_list[0])
p = int(npq_list[1])
q = int(npq_list[2])

f_list = input().split(',')
r_list = input().split(',')

max_profit = 0
method = 0

for i in range(n):
    f = int(f_list[i])
    r = int(r_list[i])
    profit = (p - r) * q - f
    if profit > max_profit and profit > 0:
        max_profit = profit
        method = i+1
        fix_fee = f
    if profit == max_profit and f < fix_fee:
        method = i+1
        fix_fee = f

print(method, max_profit)
