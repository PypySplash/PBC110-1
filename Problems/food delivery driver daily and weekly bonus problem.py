n = int(input())
m = int(input())
x = int(input())
y = int(input())
b = int(input())
r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())
r5 = int(input())
r6 = int(input())
r7 = int(input())

if n <= r1:
    day1 = x*n+y*(r1-n)
else:
    day1 = x*r1

if n <= r2:
    day2 = x*n+y*(r2-n)
else:
    day2 = x*r2
    
if n <= r3:
    day3 = x*n+y*(r3-n)
else:
    day3 = x*r3

if n <= r4:
    day4 = x*n+y*(r4-n)
else:
    day4 = x*r4
    
if n <= r5:
    day5 = x*n+y*(r5-n)
else:
    day5 = x*r5
    
if n <= r6:
    day6 = x*n+y*(r6-n)
else:
    day6 = x*r6

if n <= r7:
    day7 = x*n+y*(r7-n)
else:
    day7 = x*r7

if r1 + r2 + r3 + r4 + r5 + r6 + r7 >= m:
    total = day1 + day2 + day3 + day4 + day5 + day6 + day7 + b
else:
    total = day1 + day2 + day3 + day4 + day5 + day6 + day7
print(total)
