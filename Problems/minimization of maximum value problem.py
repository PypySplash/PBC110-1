n = int(input())

x_list = input().split(',')

temp = []

for i in range(n-1):
    x = int(x_list[i])
    x_1 = int(x_list[i+1])
    if x - x_1 >= 0:
        y = x - x_1
    else:
        y = 0
    temp.append(int(y))

min_y = min(temp)

print(min_y)
