nB_list = input().split(',')
n = int(nB_list[0])  # 物品數量
B = int(nB_list[1])  # 箱子最大限重

w_list = input().split(',')

weight = []  # 物品重量清單

for i in range(n):
    w = float(w_list[i])
    weight.append(float(w))

weight.sort()  # 排序
weight.reverse()  # 重量由大到小

remain_cap = [B]  # 紀錄剩餘容量，起始清單表預設一個空箱子

for i in range(n):
    put = False  # 物品是否已經被放進已經打開的箱子，False表還沒
    for j in range(len(remain_cap)):
        if weight[i] <= remain_cap[j]:  # 判斷是否放得下
            put = True
            remain_cap[j] -= weight[i]
            break
    if not put:  # 表需開一個新箱子裝此物品
        remain_cap.append(B - weight[i])  # 新箱子剩餘容量 = 最大容量 - 此物品容量

print(len(remain_cap))
