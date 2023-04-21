import tkinter as tk
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import datetime
import twstock
from twstock import Stock
import csv
import mplfinance as mpf
twstock.__update_codes()

from backtesting import Backtest, Strategy #引入回測和交易策略功能
from backtesting.lib import crossover #引入判斷均線交會功能
from backtesting.test import SMA #引入繪製均線功能



os.chdir('C:\\Users\\alo57\\OneDrive\\桌面\\PBC 110-1')
def grab_data(num):
    try:
        stock = Stock(str(num))                             # 擷取股價
        return stock
    except KeyError as key:  # 股票代碼防呆
        print("stock not found")
        return None


def check_date_start_end(stock_code,start_date, end_date,filename):
    with open(filename, newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        list_of_rows = list(rows)  # csv 轉 list
#         print('list_of_rows:')
#         for i in list_of_rows:
#             print(i)
        # 以迴圈輸出每一列
        count = -1
        date_list = [0]  # 放 datetime data type的日期，第一行是第一天
        #print(list_of_rows)
        for row in list_of_rows:
            # print(row)
            count += 1
            if count == 0:
                continue
            temp = row[1].split('-')
            #print('temp', temp)
            date_list.append(datetime.date(int(temp[0]), int(temp[1]), int(temp[2])))
        date_needed = []
#         print(f'date_list:{date_list}')
        for i in range(1, len(date_list)):  # 第0行標題無用
            # print(date_list[i])
            if date_list[i] >= start_date and date_list[i] <= end_date:
                # print("加進去")
                date_needed.append(i)
            else:
                pass
                # print('不加')
            # print('------------------------')
        print('date_needed', date_needed)
    outfname = f'{stock_code}_date.csv'
    with open(outfname, 'w', newline = '') as csvfile:
        #建立 CSV 檔寫入器
        writer = csv.writer(csvfile)
        #寫入一列資料
        writer.writerow(list_of_rows[0])
        for index in date_needed:           
            writer.writerow(list_of_rows[index])
        print(f'{stock_code}_date.csv created')
        

def annualized_return(ticker):
    working_doc = open(f'C:/Users/alo57/OneDrive/桌面/PBC 110-1/{ticker}_date.csv', 'r',encoding='utf-8' )
    doc = csv.DictReader(working_doc)
    count = 0
    entry = 0
    price = []
    for i in doc:
        if count == 0:
            count += 1
            continue
        entry += 1
        price.append(float(i['Close']))
    print(price, entry)
    simple_return = ((price[-1] - price[0]) / price[0])
    annualized_return = ((price[-1]  / price[0]) ** (1/(entry/252))) -1
    # f'{simple_return*100:.02f}' + '%' + f'{annualized_return*100:.02f}'+'%'
    # print(output)
    return([f'Simple return = {simple_return*100:.01f}' + '%', f'Annualized return = {annualized_return*100:.01f}'+'%'])


# --------------------------------------回測相關-----------------------------------------------
class SmaCross(Strategy): #交易策略命名為SmaClass，使用backtesting.py的Strategy功能
    n1 = 5 #設定第一條均線日數為5日(周線)
    n2 = 20 #設定第二條均線日數為20日(月線)，這邊的日數可自由調整

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1) #定義第一條均線為sma1，使用backtesting.py的SMA功能算繪
        self.sma2 = self.I(SMA, self.data.Close, self.n2) #定義第二條均線為sma2，使用backtesting.py的SMA功能算繪

    def next(self):
        if crossover(self.sma1, self.sma2): #如果周線衝上月線，表示近期是上漲的，則買入
            self.buy()
        elif crossover(self.sma2, self.sma1): #如果周線再與月線交叉，表示開始下跌了，則賣出
            self.sell()


def backtest():
    stock = str(code_entry.get()) #設定要測試的股票標的名稱

    df = pd.read_csv(f'C:/Users/alo57/OneDrive/桌面/PBC 110-1/{stock}_date.csv', index_col = 1) #pandas讀取資料，並將第1欄作為索引欄
    # df = df.interpolate() #CSV檔案中若有缺漏，會使用內插法自動補值，不一定需要的功能

    df.index = pd.to_datetime(df.index) #將索引欄資料轉換成pandas的時間格式，backtesting才有辦法排序
    print(df)

    test = Backtest(df, SmaCross, cash=10000, commission=.002)
    # 指定回測程式為test，在Backtest函數中依序放入(資料來源、策略、現金、手續費)

    result = test.run()
    # 執行回測程式並存到result中

    print(result) # 直接print文字結果
    result_label2.configure(text=result)

    # test.plot(filename=f"D:\PBC\期末\{stock}.html") #將線圖網頁依照指定檔名保存
    # 畫圖功能怪怪的暫時不要
    
#--------------------------------------介面相關-----------------------------------------------
#UI設定
window = tk.Tk()
# 設定視窗標題、大小和背景顏色
window.title('股票資料小幫手')
window.geometry('800x600')
window.configure(background='white')

header_label = tk.Label(window, text="台股個股資訊")
header_label.pack()

def calculate_bmi_number():
    stock_code = str(code_entry.get())
    begin_day_input = str(start_entry.get()).split('-')
    end_day_input = str(end_entry.get()).split('-')
    begin_day = datetime.date(int(begin_day_input[0]), int(begin_day_input[1]), int(begin_day_input[2]))
    end_day = datetime.date(int(end_day_input[0]), int(end_day_input[1]), int(end_day_input[2]))
    stock = grab_data(stock_code)
    target_price = stock.fetch_from(int(begin_day.year),int(begin_day.month))
    name_attribute = ['Date', 'Capacity', 'Turnover', 'Open', 'High', 'Low', 'Close', 'Change','Trascation']  #幫收集到的資料設定表頭
    df = pd.DataFrame(columns=name_attribute, data=target_price)#將twstock抓到的清單轉成Data Frame格式的資料表
    #df = df.set_index('Date')   
    # 要看的話資料夾要改
    filename = f'C:/Users/alo57/OneDrive/桌面/PBC 110-1/{stock_code}_date.csv'
    #指定Data Frame轉存csv檔案的檔名與路徑
    df.to_csv(filename) # index=False
    print(f'C:/Users/alo57/OneDrive/桌面/PBC 110-1/{stock_code}.csv saved')
    # 將Data Frame轉存為csv檔案
    check_date_start_end(stock_code,begin_day, end_day,filename)
    result = annualized_return(stock_code)
    result_label.configure(text=result)



    
# 以下為 height_frame 群組
code_frame = tk.Frame(window)
# 向上對齊父元件
code_frame.pack(side=tk.TOP)
code_label = tk.Label(code_frame, text='股票代碼')
code_label.pack(side=tk.LEFT)
code_entry = tk.Entry(code_frame)
code_entry.pack(side=tk.LEFT)


# ---------------------------繪圖相關------------------------------
def draw():
    stock_code = str(code_entry.get())
    
    df = pd.read_csv(f'C:/Users/alo57/OneDrive/桌面/PBC 110-1/{stock_code}_date.csv', parse_dates=True, index_col=1)
    # 針對資料表做修正，因為交易量(Turnover)在mplfinance中須被改為Volume才能被認出來
    df.rename(columns={'Turnover': 'Volume'}, inplace=True)
    # 針對線圖的外觀微調，將上漲設定為紅色，下跌設定為綠色，符合台股表示習慣
    mc = mpf.make_marketcolors(up='r', down='g', inherit=True)
    # 把自訂的marketcolors放到自訂的style中，而這個改動是基於預設的yahoo外觀
    s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
    # 設定可變參數kwargs，並在變數中填上繪圖時會用到的設定值
    kwargs = dict(type='candle', mav=(5, 20, 60), volume=True, figratio=(10, 8), figscale=0.75, title=stock_code,
                  style=s)
    # 選擇df資料表為資料來源，帶入kwargs參數，畫出目標股票的走勢圖
    mpf.plot(df, **kwargs)
    


# 以下為 start_frame 群組
start_frame = tk.Frame(window)
start_frame.pack(side=tk.TOP)
start_label = tk.Label(start_frame, text='起始日')
start_label.pack(side=tk.LEFT)
start_entry = tk.Entry(start_frame)
start_entry.pack(side=tk.LEFT)

end_frame = tk.Frame(window)
end_frame.pack(side=tk.TOP)
end_label = tk.Label(start_frame, text='結束日')
end_label.pack(side=tk.LEFT)
end_entry = tk.Entry(start_frame)
end_entry.pack(side=tk.LEFT)



result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='快速報酬率計算',command=calculate_bmi_number)
calculate_btn.pack()

backtest_btn = tk.Button(window, text='開始回測',command=backtest)
backtest_btn.pack()

calculate_btn2 = tk.Button(window, text='顯示圖表',command=lambda:[draw()])
calculate_btn2.pack()

result_label2 = tk.Label(window)
result_label2.pack()

# 運行主程式
window.mainloop()
