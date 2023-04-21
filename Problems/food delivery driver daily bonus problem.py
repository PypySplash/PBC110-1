n = int(input())
x = int(input())
y = int(input())
r = int(input())

if n <= r:
    total = x*n+y*(r-n)
else:
    total = x*r    
print(total)

"""
for i in range(1,n+1):
"""
