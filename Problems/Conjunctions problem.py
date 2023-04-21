punctuation = """。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&'()*+,-./:;<=>?@[]^_`{¦}~"""
length = int(input())
char = str(input())
temp2 = []
for i in range(len(char)-(length-1)):
    temp = []
    index = 0
    for j in range(length):
        if char[i+j] in punctuation:
            index = 1
            break
    if index == 0:
        for j in range(length):
            temp.append(char[i+j])
        temp2.append(temp)

if length >= 2:
    for i in range(len(temp2)):
        count = length
        while(count):
            for j in range(length):
                print(str(temp2[i][j]), end='')
                count -= 1
        print()
else:
    print("ILLEGAL_N")
