nmr_list = input().split(',')
x_limit = int(nmr_list[0])
y_limit = int(nmr_list[1])
r = int(nmr_list[2])

pop = []

for i in range(y_limit+1):
    pop_list = input().split(',')
    for j in range(x_limit+1):
        pop_list[j] = int(pop_list[j])
    pop.append(pop_list)

max_cover_pop = 0

for x in range(y_limit+1):
    for y in range(x_limit+1):
        cover_pop = 0
        for i in range(y_limit+1):
            for j in range(x_limit+1):
                if abs(x-i)+abs(y-j) <= r:
                    cover_pop += pop[i][j]
        if cover_pop > max_cover_pop:
            max_cover_pop = cover_pop

print(max_cover_pop)
