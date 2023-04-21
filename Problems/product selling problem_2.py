nc_list = input().split(',')
n = int(nc_list[0])
c = int(nc_list[1])
pi_list = input().split(',')
qi_list = input().split(',')
max_profit = float("-inf")

for j in range(n):
    pi = int(pi_list[j])
    qi = int(qi_list[j])
    profit = (pi - c) * qi
    if profit > max_profit:
        max_profit = profit
        optimal_p = pi
        optimal_q = qi
    elif profit == max_profit and qi > optimal_q:
        optimal_q = qi
        optimal_p = pi

print(optimal_p, max_profit, sep=',')
