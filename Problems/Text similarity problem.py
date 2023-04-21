punctuation = """。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&'()*+,-./:;<=>?@[]^_`{¦}~"""
length = int(input())
target = str(input())

temp2 = []
for i in range(len(target)-(length-1)):
    temp = []
    index = 0
    for j in range(length):
        if target[i+j] in punctuation:
            index = 1
            break
    if index == 0:
        for j in range(length):
            temp.append(target[i+j])
        temp2.append(temp)
LEN = len(temp2)

source = str(input())
temp3 = []
for i in range(len(source)-(length-1)):
    temp = []
    index = 0
    for j in range(length):
        if source[i+j] in punctuation:
            index = 1
            break
    if index == 0:
        for j in range(length):
            temp.append(source[i+j])
        temp3.append(temp)

MATCH_COUNT = 0
MATCHED_SEGMENTS = []
for i in range(len(temp2)):
    for j in range(len(temp3)):
        if temp2[i] == temp3[j]:
            MATCHED_SEGMENTS.append(temp2[i])
            MATCH_COUNT += 1

print("LEN=", LEN, sep='')
print('MATCH_COUNT=', MATCH_COUNT, sep='')
SIMILARITY = MATCH_COUNT/LEN
print('SIMILARITY=%0.4f' %SIMILARITY)
print('MATCHED SEGMENTS:')
for i in range(len(MATCHED_SEGMENTS)):
         count = length
         while(count):
            for j in range(length):
                print(str(MATCHED_SEGMENTS[i][j]), end='')
                count -= 1
            print()
