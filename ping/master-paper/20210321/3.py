import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../2021-03-21-final.csv")
df = df.dropna()
print(df.columns)
plt.figure(figsize=(8, 8))
# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(1, 1, 1)
df1 = df[["WBC第1天", "WBC第3天"]]
# df1 = df1.dropna()
ax1.boxplot([df1["WBC第1天"].dropna(), df1["WBC第3天"].dropna()], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['第1天', '第3天'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("WBC评分", fontsize=16)
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 25, 1, 'k'
ax1.set_ylim(0, 30)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+1, "$P=.459$", ha='center', va='bottom', color=col, fontsize=20)
# ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)
plt.show()