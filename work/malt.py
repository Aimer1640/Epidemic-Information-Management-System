import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

xlsx = pd.read_excel('data.xlsx', sheet_name='国内疫情实时数据')
xlsx.to_csv('data.csv', header=None)
new, total, now, dead, heal = np.loadtxt('data.csv', delimiter=',', usecols=(2, 3, 4, 5, 6), unpack=True,
                                         encoding='utf_8')
# print(new)
# print(total[1])
matplotlib.rcParams['font.family'] = 'STsong'
matplotlib.rcParams['font.style'] = 'normal'
matplotlib.rcParams['font.size'] = 12

plt.subplot(2, 1, 1)
data = [new[1], now[1], total[1], dead[1], heal[1]]
labels = ['新增人数', '现有确诊', '累计确诊', '死亡人数', '治愈人数']

plt.bar(range(len(data)), data, tick_label=labels)
plt.bar(labels, data, 0.4, color="steelblue")
why = zip(labels, data)

for a, b in why:  # 柱子上的数字显示
    plt.text(a, b, '%.2f' % b, ha='center', va='bottom', fontsize=7)
plt.title('国内疫情实时数据统计')
plt.xlabel('人数分布（x）')
plt.ylabel('人数（y）')

plt.subplot(2, 1, 2)
labels = '新增人数', '现有确诊', '累计确诊', '死亡人数', '治愈人数'
sizes = [new[1], now[1], total[1], dead[1], heal[1]]
explode = (0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, autopct="%1.1f%%")
plt.show()
