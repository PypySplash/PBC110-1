file = input()
# file = 'C:\\Users\\alo57\\OneDrive\\桌面\\PBC 110-1\\small1.csv'

lineList = []

with open(file, 'r', encoding = 'utf-8') as infile:
    for line in infile:
        temp = line.split(',')
        lineList.append(temp)
    # print(lineList)
    for i in range(len(lineList)):
        if '\"' in lineList[i][1]:
            lineList[i][0] = str(lineList[i][0] + ',' + lineList[i][1])
            lineList[i].pop(1)
            
    Maxcolumn = ['']*len(lineList[1])
    
    for i in range(len(lineList[1])):
        Maxstr = 0
        for j in range(len(lineList)):
            Curstr = 0
            Curstr = len(str(lineList[j][i]))
            if Curstr > Maxstr:
                Maxstr = Curstr
                for k in (str(lineList[j][i])):
                    if k == ' ':
                        Maxstr -= 1
        if i == 0 or i == 3:
            Maxstr -= 2
        if i == 15:
            Maxstr -= 1
            
        Maxcolumn[i] = Maxstr
        
    for i in Maxcolumn:
        print(i)
