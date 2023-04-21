file = input()
# file = 'C:\\Users\\alo57\\OneDrive\\桌面\\PBC 110-1\\small1.csv'
num = input()
sp2 = "　"
lineList = []
with open(file, 'r', encoding = 'utf-8') as infile:
    for line in infile:
        lineList.append(line)
    infoList = []
    for i in lineList:
        i = list(i)
        index = 1
        for j in range(len(i)):
            if i[j] == '"':
                index *= (-1)
            elif i[j] == ',' and index == 1:
                i[j] = "!"
        string = "".join(i)
        infoList.append(string.split('!'))
    for i in range(1, len(infoList)):
        infoList[i][5] = str(int(infoList[i][5]) + 19110000)
        infoList[i][5] = infoList[i][5][:4] + '-' + infoList[i][5][4:6] + '-' + infoList[i][5][6:8]
        infoList[i][4] = format(int(infoList[i][4]), ',d')
        infoList[i][0] = infoList[i][0].strip('"')
        infoList[i][3] = infoList[i][3].strip('"')
    count = 0
    temp = []
    for shop in infoList:
        if num in shop[1] or num in shop[2]:
            if shop[2] == '':
                temp.append([shop[3], shop[1], shop[5], shop[4], shop[0]])
            else:
                temp.append([shop[3], f'{shop[1]}({shop[2]})', shop[5], shop[4], shop[0]])
    for shop in temp:
        if len(shop[0]) < 20:
            shop[0] += sp2 * (20 - len(shop[0]))
        for j in range(1, len(shop)):
            if len(shop[j]) < 20:
                shop[j] += ' ' * (20 - len(shop[j]))
    temp2 = sorted(temp, key = (lambda x:x[2]))
    count20 = 0
    final = []
    for i in range(len(temp2)):
        try:
            if count20 >= 20 and temp2[i][2] != temp2[i - 1][2]:
                break
            elif count20 >= 20 and temp2[i][2] == temp2[i - 1][2]:
                pass
        except:
            pass
        final.append(temp2[i])
        count20 += 1
    for i in range(1, len(final)):
        if final[i][2] == final[i - 1][2] and final[i][3] > final[i - 1][3]:
            final[i], final[i-1] = final[i-1], final[i]
    for i in range(1, len(final)):
        if final[i][2] == final[i - 1][2] and final[i][3] == final[i - 1][3] and final[i][1] < final[i - 1][1]:
            final[i], final[i-1] = final[i-1], final[i]
    
    for i in range(min(20, len(final))):
        print(*final[i])
    if len(temp) == 0:
        print('NO_DATA_FOUND')
