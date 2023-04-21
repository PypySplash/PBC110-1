nk = input().split(',')  # 輸入城鎮數量、消防局數量
townNum = int(nk[0])  # 城鎮數量
stationNum = int(nk[1])  # 消防局數量
hList = input().split(',')  # 輸入預期火災次數

distance_ijji = []  # 城鎮i和城鎮j間的距離list
townIndex = []  # 用來記錄城鎮的index
townList = []  # 用來記錄城鎮編號

for i in range(townNum):  # 用迴圈輸入城鎮間的距離
    distance_ijji.append(input().split(','))
    for j in range(townNum):  # 把list轉成int
        distance_ijji[i][j] = int(distance_ijji[i][j])

while(stationNum):  # 使用while迴圈來執行消防局的設站，每當找到一個消防局，while迴圈的數字就減少1
    if(len(townList) == 0):  # 第一個消防局的找法
        minDijji = float("inf")
        for i in range(townNum):  # 找出較小總預期距離的城鎮
            distance = 0
            for j in range(townNum):
                fire = int(hList[j])
                distance += fire * distance_ijji[i][j]
            if minDijji > distance:  # 平手則取編號較小的城鎮
                minDijji = distance
                town1 = i + 1
        townIndex.append(town1 - 1)  # 每找到一個城鎮，分別存進城鎮index和城鎮List裡
        townList.append(town1)
        stationNum -= 1  # 每找到一個城鎮設站，接下來要設的消防局數量就少一個

    elif(len(townList) == 1):  # 在第一個找的城鎮i的list中，找距離最長者為第2個城鎮
        town2 = distance_ijji[townIndex[0]].index(max(distance_ijji[townIndex[0]])) + 1
        townIndex.append(town2 - 1)
        townList.append(town2)
        stationNum -= 1

    elif(len(townList) > 1):  # 在前面找的兩座城鎮以外的列，分別找townIndex行中的最小值，互相比較，取最小值中最大值者
        maxList = []
        indexList = []
        for i in range(townNum):
            if(i in townIndex):  # 若城鎮i已經被選過，則繼續執行外圈for迴圈
                continue
            minDis = float('inf')
            for j in townIndex:  # 平手時若編號一樣，取編號較小者
                if minDis > distance_ijji[i][j]:
                    minDis = distance_ijji[i][j]
            maxList.append(minDis)  # 記錄每個非城鎮列中，城鎮行的最小值
            indexList.append(i)  # 紀錄每個非城鎮列的Index
        townUp3 = indexList[maxList.index(max(maxList))] + 1  # 找到第三個以後的城鎮
        townIndex.append(townUp3-1)
        townList.append(townUp3)
        stationNum -= 1

totalDistance = 0

for i in range(townNum):  # 使用for迴圈來尋找總距離
    minDij = float('inf')
    fire = int(hList[i])
    if i not in townIndex:  # 挑出沒有被選到的城鎮列
        for j in range(townNum):
            if j in townIndex:  # 挑出有被選到的城鎮行
                if minDij > distance_ijji[i][j]:  # 平手時選編號小的
                    minDij = distance_ijji[i][j]
        totalDistance += minDij * fire  # 總距離 = 失火次數 * 剩下城鎮到最近設站城鎮的距離

print(",".join(str(i) for i in townList), end='')
print(str(';') + str(totalDistance))
