v = int(input())

temp = input().split(',')
x_list = []

for i in temp:
    x_list.append(int(i))

num = 0
first_location = 0
location = -1

for i in range(len(x_list)):
    x = int(x_list[i])
    if v == x:
        num += 1
        if first_location > location:
            location = i+1
            first_location = location

print(num, first_location, sep=',')
