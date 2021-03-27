import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 图3-21 血浆IL-6浓度比较：（a）病例组与对照组第1天血浆IL-6浓度比较（“*”代表P＜0.05）
def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细


color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../data-final.csv")
# df = df.dropna()
print(df.columns)
plt.figure(figsize=(8, 8))
# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(1, 1, 1)

df1 = df[["脓毒症组IL-6", "脓毒症组IL-6对照组"]]

ax1.boxplot([df1["脓毒症组IL-6"].dropna(), df1["脓毒症组IL-6对照组"].dropna()], notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['病例组', '对照组'], fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel("IL-6(pg/ml)", fontsize=20)
x1, x2 = 1, 2
y, h, col = 105, 3, 'k'
ax1.set_ylim(0, 120)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+0.5, "$P=.032$", ha='center', va='bottom', color=col, fontsize=20)
# ax1.set_title("(a)", y=-0.2, fontsize=20)
set_ax(ax1)



plt.show()
