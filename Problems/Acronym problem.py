# punctuation = """。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&'()*+,-./:;<=>?@[]^_`{¦}~"""
punctuation = """。，、；：「」『』（）─？！─…﹏《》〈〉．～　,.; !"#$%&'*+,-./:;<=>?@[]^_`{¦}~"""  # 去掉小括號
passage = input()

for everyone in punctuation:
    passage = passage.replace(everyone, ' ')  # 將括號以外的標點符號都轉成空格
wordList = passage.split()

parenthesisIndex = []
acronymNum = []
acronym = []
for i in range(len(wordList)):
    if wordList[i][0] == '(':
        parenthesisIndex.append(i)
        acronymNum.append(len(wordList[i])-2)  # 長度 = (...) - 2個括號
        acronym.append(wordList[i][1:len(wordList[i])-1])

frontword = []
frontchar = []
for i in range(len(parenthesisIndex)):
    frontchar = str()
    for j in range(parenthesisIndex[i] - acronymNum[i], parenthesisIndex[i]):
        frontchar += (' ' + wordList[j])
    frontchar = frontchar.strip(' ')
    frontword.append(frontchar)

for i in range(len(frontword)):
    if "".join(j[0].upper() for j in frontword[i].split()) == acronym[i]:
        print(f"{acronym[i]}: {frontword[i]}")
