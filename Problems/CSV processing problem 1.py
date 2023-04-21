file = input()
# file = 'C:\\Users\\alo57\\OneDrive\\桌面\\PBC 110-1\\small1.csv'
num = int(input())

lineList = []

with open(file, 'r', encoding = 'utf-8') as infile:
    for line in infile:
        # print(line)
        lineList.append(line)
    # print(lineList)
    infoList = []
    for i in lineList:
        i = list(i)
    # print(i)
        index = 1
        for j in range(len(i)):
            # print(i[j])
            if i[j] == '"':
                index *= (-1)
            elif i[j] == ',' and index == 1:
                i[j] = '!'
            # print(i[j])
        string = ''.join(i)
        # print(string)
        infoList.append(string.split('!'))
    # print(infoList)
    print(f"{infoList[0][3]}:", infoList[num][3].strip('"'))
    print(f"{infoList[0][1]}:", infoList[num][1])
    print(f"{infoList[0][0]}:", infoList[num][0].strip('"'))
