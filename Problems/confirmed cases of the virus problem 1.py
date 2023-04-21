def mono_inc(inlist, k):  # 定義mono_inc函數及其parameters
    if k < 3:  # 題目敘述，若k<3則視為預設值k=3
        k = 3
    newList = []  # 建立一新清單，將inlist內的資料轉換成int
    for element in inlist:
        newList.append(int(element))
    indexList = []  # 建立一清單來記錄人數開始上升到結束之index

    for i in range(len(newList)-1):  # 使用迴圈來找尋，這裡的上界-1是為了避免超出範圍
        if newList[i] < newList[i+1]:  # 若前一項小於後一項，則找到人數上升
            if len(indexList) > 0:  # 找到index時同時記錄第i個及第i+1個，故在下一次迴圈進行時先踢出重複的數字
                indexList.pop(-1)  # 前提條件是indexList裡已經有存數字，否則會out of range
            indexList.append(i)
            indexList.append(i+1)
        elif newList[i] >= newList[i+1] and len(indexList) <= k:
            indexList.clear()  # 若人數沒有繼續上升且連續上升天數<=k時，則清空list，繼續尋找
        elif newList[i] >= newList[i+1] and len(indexList) > k:
            break  # 若人數沒有繼續上升，且連續上升天數已經>k時，則找到答案，跳出迴圈
    if len(indexList) > k:  # 若有找到符合條件之區間，則print出start index & end index
        print(indexList[0], end="\n")
        print(indexList[len(indexList)-1])
    else:  # 若無，則print出None
        print(None)

confirmedCase = input().split(',')  # 輸入確診人數
continuousDays = int(input())  # 輸入連續上升天數
mono_inc(confirmedCase, continuousDays)  # 呼叫mono_inc函數及其arguements
