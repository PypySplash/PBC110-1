# import numpy as np

color = input().split(',')
given = input().split(',')
# print(f"5張牌花色：{color}")
# print(f"手牌為：{given}")

# for i in range(5):
#     print(given[i])

"""規則a: 一張A得5分"""

point = 0
for i in range(5):
    if given[i] == 'A':
        point += 5
# print(count)
# print(point)

"""規則b: 對子得10分 & 規則e: 葫蘆得80分 & 規則f: 鐵支得100分"""

bdict = {}  # 創造一個規則b的dict
for key in given:  # 統計每個東西出現的次數
    bdict[key] = bdict.get(key, 0) + 1
count = 0  # 若出現次數為2，則出現一個對子；出現次數為3，則為一個三條
for i in list(bdict.values()):
    if i == 2:
        point += 10
        count += 2
    if i == 3:
        point += 30
        count += 3
    if i == 4:
        point += 160
    if i == 5:
        point += (5 * 4 / 2) * 10 + 5 * 100 
# print(point)

# 若為一個對子+一個三條，則為葫蘆
if count == 5:
    point += 80
print(point)
# print(bdict)
# print(list(bdict)[0]) 
# print(list(bdict.values())[0])

"""規則c: 同花得30分"""

cdict = {}
for key in color:
    cdict[key] = cdict.get(key, 0) + 1
for i in list(cdict.values()):
    if i == 5:
        point += 30
# print(point)

"""規則d: 順子得50分 & 規則g: 同花順得300分"""

for i in range(5):  # 先將JQKA轉成數字
    if given[i] == 'A':
        given[i] = 14
    if given[i] == 'J':
        given[i] = 11
    if given[i] == 'Q':
        given[i] = 12
    if given[i] == 'K':
        given[i] = 13
    else:  # 若不是JQKA，則轉成int
        given[i] = int(given[i])
given.sort()

# print(given)

# 創造一個順子list
straight_list = [[2, 11, 12, 13, 14], [2, 3, 12, 13, 14], [2, 3, 4, 13, 14], [2, 3, 4, 5, 14]]

sfcount = 0
# 若given的牌在list裡，則此牌組為順子
for i in range(4):
    if given == straight_list[i]:
        point += 50
        sfcount = 1
# print(sfcount)

# 若不在list裡，進行排序，檢查是否為順子
# given = np.array(given)  # 轉為numpy陣列
# diff = np.diff(given)  # diff為相鄰元素的差組成的陣列
# diff = list(diff)  # 將diff轉成list
# print(diff)

# if diff.count(1) == 4:  # 若每相鄰元素皆相差1，則總共有4個
    # point += 50
    # sfcount = 1  # 符合條件，順子計數+1
# print(point)
# print(diff)

gdict = {}  # 規則g的dict
for key in color:  # 檢查花色
    gdict[key] = gdict.get(key, 0) + 1
for i in list(gdict.values()):  # 若5同樣花色，且符合順子條件，則為同花順
    if i == 5 and sfcount == 1:
        point += 300
# print(point)
