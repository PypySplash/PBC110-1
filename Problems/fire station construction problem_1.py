n = int(input())
h_list = input().split(',')

dst = []
for i in range(n):
    dst.append(input().split(','))
    for j in range(n):
        dst[i][j] = int(dst[i][j])

min_dist = float("inf")

for i in range(n):
    dist = 0
    for j in range(n):
        h = int(h_list[j])
        dist += h * dst[i][j]
    if min_dist > dist:
        min_dist = dist
        city = i+1

print(city, min_dist, sep=',')
