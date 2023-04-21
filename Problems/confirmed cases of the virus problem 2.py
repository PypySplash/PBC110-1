def mono_inc_plus(inlist, k):
    if k < 3:
        k = 3
    newList = []
    for element in inlist:
        newList.append(int(element))
    temp = []
    final_list = []
    
    for i in range(len(newList)-1):
        if newList[i] < newList[i+1]:
            if len(temp) > 0:
                temp.pop(-1)
            temp.append(i)
            temp.append(i+1)
        if newList[i] >= newList[i+1] and len(temp) <= k:
            temp.clear()
        if newList[i] >= newList[i+1] and len(temp) > k:
            indexList = []
            indexList.append(temp[0])
            indexList.append(temp[len(temp)-1])
            final_list.append(indexList)
            temp.clear()
    if len(temp) > k:
        indexList = []
        indexList.append(temp[0])
        indexList.append(temp[len(temp)-1])
        final_list.append(indexList)
    
    if len(final_list) > 0:
        for i in range(len(final_list)):
            print(final_list[i][0], final_list[i][1], sep=' ', end='\n')
    elif len(final_list) == 0 and len(temp) > k:
        print(temp[0], temp[len(temp)-1])
    else:
        print(None)

confirmedCase = input().split(',')
continuousDays = int(input())
mono_inc_plus(confirmedCase, continuousDays)
