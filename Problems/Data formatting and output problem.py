width = int(input())
format = input().split(',')
dataList = []

while True:
    data = input()
    if data == 'RECORD_END':
        break
    dataList.append(data.split(','))

for i in range(len(dataList)):
    for j in range(len(format)):
        if format[j] == 'f':
            dataList[i][j] = '%.2f' % float(dataList[i][j])

for i in range(len(dataList)):
    for j in range(len(format)):
        if len(dataList[i][j]) > width:
            dataList[i][j] = (dataList[i][j][:width - 1] + '~')
        if len(dataList[i][j]) < width:  # ' ' * 文字即是在前面+上空格(空格也算字元，可直接用 *
            dataList[i][j] = ' ' * (width - len(dataList[i][j])) + dataList[i][j]
    print(*dataList[i])  # *是去逗號+去框格
