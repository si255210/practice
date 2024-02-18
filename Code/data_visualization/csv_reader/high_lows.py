import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = "D:\Google\Code\data_visualization\csv_reader\sitka_weather_2014.csv"


with open(filename) as f:
    reader = csv.reader(f)  # class '_csv.reader'文件，应该是列表嵌套列表 
    # 执行一遍next抬头就没了
    header_row = next(reader)
    # 用for遍历一遍reader的值就没了,需要三个列表同时定义
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")  # 把时间字符串换成pyplot能用的
            dates.append(current_date)
            high = int(row[1])
            highs.append(high)
            low = int(row[3])
            lows.append(low)
        except:
            print('value went wrong')

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # 避免重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()