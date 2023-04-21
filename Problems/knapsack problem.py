nB_list = input().split(',')  # 輸入n,B
num_item = int(nB_list[0])  # 清單內第一個數字為物品數量
limit_weight = int(nB_list[1])  # 第二個數字為限制重量

wi_list = input().split(',')  # 輸入各物品之重量
ui_list = input().split(',')  # 輸入各物品所能帶來之效用
xi_list = input().split(',')  # 1表示帶，0表示不帶

recommend_weight = 0
recommend_utility = 0

for i in range(num_item):  # 跑迴圈，要帶的物品重量與效用分別相加
    weight_num = int(wi_list[i])  # 先把清單內的數字格式全部轉為int
    utility_num = int(ui_list[i])
    portable_num = int(xi_list[i])
    if portable_num == 1:  # 要帶的物品重量與效用分別相加
        recommend_weight += weight_num
        recommend_utility += utility_num

if recommend_weight <= limit_weight:  # 若總重<=限制重，印出總重及總效用
    print(recommend_weight, recommend_utility, sep=',')
else:  # 若總重大於限制重量，則印出-1
    print(-1)
