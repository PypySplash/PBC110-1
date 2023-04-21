a = int(input())
b = int(input())
c = int(input())
d = int(input())

abcd = []

abcd.append(a)
abcd.append(b)
abcd.append(c)
abcd.append(d)

abcd.sort()

num = 0

if abcd[0] + abcd[1] == abcd[2]:
    num += 1

if abcd[0] + abcd[1] == abcd[3]:
    num += 1

if abcd[0] + abcd[2] == abcd[3]:
    num += 1

if abcd[1] + abcd[2] == abcd[3]:
    num += 1

print(num)
