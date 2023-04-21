def printrec(records):
    for arec in records:
        # 避免浮點數誤差
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")


def apply_discount(records):
    """折扣依照各品項的總金額攤列，並對原價格進行折扣"""
    pos_sum = 0.0  # 記錄正項（或零項）總和（價格）
    neg_sum = 0.0  # 記錄負項總和（折扣）

    for arec in records:
        if arec[2] >= 0:
            pos_sum += arec[2]
        else:
            neg_sum += arec[2]

    outrecs = []
    for arec in records:
        # 使用迴圈讀取每筆交易資料時，再用單筆交易資料 arec.copy() 進行每筆交易資料的複製
        newrec = arec.copy()
        # 如果該項是正的，那就可以有總金額攤列後的折扣
        if newrec[2] >= 0:
            newrec[2] = newrec[2] + neg_sum * (newrec[2] / pos_sum)
            outrecs.append(newrec)
    return outrecs

records = []
# 每次輸入的資料筆數不會超過1000筆
for i in range(1000):
    line = input().split('_')
    # 如果一行的輸入為「RECORDSTOP」，則代表所有的紀錄已經輸入完畢
    if line[0] == 'RECORDSTOP':
        break
    else:
        records.append(line)
        # 將品項數量及小計轉成小數
        records[i][1] = float(records[i][1])
        records[i][2] = float(records[i][2])

records_discounted = apply_discount(records)
printrec(records_discounted)
print("---Original---")
printrec(records)
