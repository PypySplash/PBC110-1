stu1 = int(input())
stu2 = int(input())
stu3 = int(input())

dep1 = int(input())
dep2 = int(input())
dep3 = int(input())

# 初選reserve系
res1 = int(input())
res2 = int(input())

# 被permit的學生
if dep1 == res1 or dep1 == res2:
    per1 = stu1
else:
    per1 = 0

if dep2 == res1 or dep2 == res2:
    per2 = stu2
else:
    per2 = 0

if dep3 == res1 or dep3 == res2:
    per3 = stu3
else:
    per3 = 0

# 排順序
if per1 >= per2:
    if per2 >= per3:
        one = per3
        two = per2
        three = per1
    elif per3 >= per1:
        one = per2
        two = per1
        three = per3
    elif per1 >= per3 >= per2:
        one = per2
        two = per3
        three = per1
elif per2 >= per1:
    if per3 >= per2:
        one = per1
        two = per2
        three = per3
    elif per3 <= per1:
        one = per3
        two = per1
        three = per2
    elif per2 >= per3 >= per1:
        one = per1
        two = per3
        three = per2

# 輸出
if one != 0 and two != 0 and three != 0:
    print(str(one) + "," + str(two) + "," + str(three))
elif one == 0 and two != 0 and three != 0:
    print(str(two) + "," + str(three))
elif one == 0 and two == 0 and three != 0:
    print(str(three))
elif one == 0 and two == 0 and three == 0:
    print("-1")

"""
if res1 == res2 == dep1:
    print(stu1)

if res1 == res2 == dep2:
    print(stu2)

if res1 == res2 == dep3:
    print(stu3)

if res1 != dep1 and res1 != dep2 and res1 != dep3 and res2 != dep1 and res2 != dep2 and res2 != dep3:
    print("-1")
"""
