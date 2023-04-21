def printrec(records):
    for arec in records:
        # 避免浮點數誤差
        if abs(arec[2]) < 1e-3:
            arec[2] = 0
        print(f"{arec[0]}_{arec[1]:.2f}_{arec[2]:.2f}")
        
def apply_discount(records):
    """折扣依照各品項的總金額攤列，並對原價格進行折扣"""
    doubleList = []
    discountList = []
    discountSum = 0.0
    price = 0.0
    """
    while True:
        data = input().split('_')
        if data[0] == 'RECORDSTOP':
            break
        doubleList.append(data)
    # print(doubleList)
    """
    for i in range(1000):  # 每次輸入的資料筆數不會超過1000筆
        data = input().split('_')
        if data[0] == 'RECORDSTOP':
            break
        doubleList.append(data)
    # print(doubleList)
    
    for i in range(len(doubleList)):
        for j in range(1, 3):  # 1~2
            doubleList[i][j] = float(doubleList[i][j])
        if doubleList[i][2] < 0:
            discountSum += doubleList[i][2]
        else:
            discountList.append(doubleList[i].copy())
            price += doubleList[i][2]
    for i in range(len(discountList)):
        discountList[i][2] += discountSum * (discountList[i][2]/price)
    printrec(discountList)
    print('---Original---')
    printrec(doubleList)
    
apply_discount(list)    
