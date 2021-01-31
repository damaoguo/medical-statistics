import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../data-final.csv")
df = df.dropna()
print(df.columns)

# ---------百分比vs乳酸(实验组)----------------
ax1 = plt.subplot(2, 2, 1)
df1 = df[["脓毒症组单核细胞PD-L1", "脓毒症组血乳酸mmol/L"]]
ax1.boxplot(df1, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比(%)', '血乳酸mmol/L'])
# 绘制比较线
x1, x2 = 1, 2
y, h, col = 60, 3, 'k'
ax1.set_ylim(0, 80)
ax1.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax1.text((x1+x2)*.5, y+h+1, "$^{*}P=.000$", ha='center', va='bottom', color=col)
ax1.set_title("(a) 百分比vs乳酸(实验组)", y=-0.35)


# ----------百分比vs乳酸(对照组)---------------
ax2 = plt.subplot(2, 2, 2)
df2 = df[["脓毒症组单核细胞PD-L1百分比（%）对照组", "脓毒症组血乳酸mmol/L对照组"]]
ax2.boxplot(df2, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比(%)', '血乳酸mmol/L'])
x1, x2 = 1, 2
y, h, col = 9, 0.5, 'k'
ax2.set_ylim(0, 12)
ax2.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax2.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.418$", ha='center', va='bottom', color=col)
ax2.set_title("(b) 百分比vs乳酸(对照组)", y=-0.35)

# ----------百分比vsPCT(实验组)---------------
ax3 = plt.subplot(2, 2, 3)
df3 = df[["脓毒症组单核细胞PD-L1", "脓毒症组PCT"]]
ax3.boxplot(df3, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比（%）', 'PCT'])
x1, x2 = 1, 2
y, h, col = 55, 3, 'k'
ax3.set_ylim(0, 80)
ax3.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax3.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.000$", ha='center', va='bottom', color=col)
ax3.set_title("(c) 百分比vsPCT(实验组)", y=-0.35)

# -----------百分比vsPCT(对照组)--------------
ax4 = plt.subplot(2, 2, 4)

df4 = df[["脓毒症组单核细胞PD-L1百分比（%）对照组", "脓毒症组PCT对照组"]]
ax4.boxplot(df4, notch=False, sym='o', vert=True)
plt.xticks([x+1 for x in range(2)], ['单核细胞PD-L1百分比（%）', 'PCT'])
x1, x2 = 1, 2
y, h, col = 9, 0.5, 'k'
ax4.set_ylim(0, 12)
ax4.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
ax4.text((x1+x2)*.5, y+h+0.5, "$^{*}P=.934$", ha='center', va='bottom', color=col)
ax4.set_title("(d) 百分比vsPCT(对照组)", y=-0.35)

plt.show()
