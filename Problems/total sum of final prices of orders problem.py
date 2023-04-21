mnQD_list = input().split(',')
m = int(mnQD_list[0])
n = int(mnQD_list[1])
Q = int(mnQD_list[2])
D = int(mnQD_list[3])
p_list = input().split(',')

x_list = []

for i in range(n):
    x_list.append(input().split(','))
    for j in range(m):
        x_list[i][j] = int(x_list[i][j])

total_price = 0

for i in range(n):
    pricei = 0
    for j in range(m):
        p = int(p_list[j])
        pricei += p * x_list[i][j]
    if pricei > Q and pricei - D >= Q:
        pricei -= D
    elif pricei > Q and pricei - D < Q:
        pricei = Q
    total_price += pricei
    
print(total_price)
