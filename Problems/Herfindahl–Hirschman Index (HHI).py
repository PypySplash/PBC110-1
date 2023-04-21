def printresult(value):
    print(f"{value:.4f}")

def my_hhi(ylist, htype):
    newList = []
    for element in ylist:
        newList.append(float(element))
    total = 0
    for i in range(len(newList)):
        total += abs(newList[i])
    HHI = 0
    if htype == 'Original':
        for j in range(len(newList)):
            HHI += (newList[j]/total)**2
    if htype == 'Normalized':
        for j in range(len(newList)):
            HHI += (newList[j]/total)**2
        HHI = (HHI-1/len(newList))/(1-1/len(newList))
    printresult(HHI)

revenue = input().split(',')
method = str(input())
my_hhi(revenue, method)
