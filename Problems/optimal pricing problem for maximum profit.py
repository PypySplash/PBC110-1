n = int(input())  # package way

# 令預設值為完全無法獲利，則若for迴圈條件不成立，答案直接輸出預設值
max_profit = 0
optimal_price = 1000
method = 1

# 外層for迴圈跑不同包裝方式
for i in range(1, n+1):
    a = int(input())  # base demand
    b = int(input())  # price sensitivity
    c = int(input())  # unit cost
    if c <= a:  # 內層for迴圈找價格&最大利潤&包裝方式
        for p in range(c + 1, a // b):  # p=c時，無利潤；p=a/b時，需求量為0
            profit = (a - b * p) * (p - c)  # 利潤=PQ-cQ
            #   print(p, profit)
            if profit > max_profit:  # 二次曲線解有極值，超過極值即不用繼續找
                max_profit = profit
                optimal_price = p
                method = i
            elif profit == max_profit and method == i:  # 一樣高的利潤，用編號小的包裝方式
                optimal_price = p  # 。在一種包裝方法中，如果有複數個價格都能得到最高的利潤，請選擇比較大的價格
print(str(method) + "," + str(optimal_price) + "," + str(max_profit))

"""
print("optimal price = " + str(optimal_price))
print("maximized profit = " + str(max_profit))
"""
