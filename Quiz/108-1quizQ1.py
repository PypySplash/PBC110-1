n = int(input())
sqr_n = n ** 0.5
sqr_n_int = int(sqr_n)
sqr_n_float = float(sqr_n)

if sqr_n_float - sqr_n_int == 0:
    print(int(sqr_n))
else:
    print(0)
