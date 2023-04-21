nB_list = input().split(',')
num_item = int(nB_list[0])
limit_weight = int(nB_list[1])

w_list = input().split(',')
u_list = input().split(',')

num_sol = int(input())

best_weight = 0
best_utility = 0
best_sol = float("inf")

item = []

for i in range(num_sol):
    item.append(input().split(','))
    for j in range(num_item + 1):
        item[i][j] = int(item[i][j])

for i in range(num_sol):
    recommend_weight = 0
    recommend_utility = 0
    for j in range(num_item):
        portable_num = int(item[i][j+1])
        weight_num = int(w_list[j])
        utility_num = int(u_list[j])
        if portable_num == 1:
            recommend_weight += weight_num
            recommend_utility += utility_num
    if recommend_utility > best_utility and recommend_weight <= limit_weight:
        best_sol = item[i][0]
        best_weight = recommend_weight
        best_utility = recommend_utility
    elif recommend_utility == best_utility and recommend_weight <= limit_weight and best_sol > item[i][0]:
        best_sol = item[i][0]
        best_weight = recommend_weight

print(best_sol, best_weight, best_utility, sep=',')
