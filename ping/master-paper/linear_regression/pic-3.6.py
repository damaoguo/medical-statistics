import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
plt.rcParams['font.sans-serif'] = ['SimHei']

def set_ax(ax):
    ax.spines['bottom'].set_linewidth(2);  ###设置底部坐标轴的粗细
    ax.spines['left'].set_linewidth(2);  ####设置左边坐标轴的粗细
    ax.spines['right'].set_linewidth(2);  ###设置右边坐标轴的粗细
    ax.spines['top'].set_linewidth(2);  ###设置右边坐标轴的粗细

color = ['orangered', 'g', 'blue', 'k']
df = pd.read_csv("../data-final.csv")
print(df.columns)
plt.figure(figsize=(8, 8))

# -------(1)脓毒症存活组：百分比与血乳酸-------------
ax1 = plt.subplot(1, 1, 1)
df1 = df[["脓毒症存活组单核细胞PD-L1百分比（%）", "脓毒症存活组血乳酸"]]
df1 = df1.dropna()
X = df1["脓毒症存活组单核细胞PD-L1百分比（%）"].values.reshape(-1, 1)
y = df1["脓毒症存活组血乳酸"].values.reshape(-1, 1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlabel("单核细胞PD-L1百分比（%）", fontsize=20)
plt.ylabel("血乳酸(mmol/L)", fontsize=20)

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)
print(model.score(X, y))
ax1.plot(X, y, linestyle='none', marker='o', alpha=0.6)
y2 = model.predict(X)
ax1.plot(X, y2, '-', color='dodgerblue')
ax1.text(x=20, y=7, s='$r=0.587$', fontsize=20)
ax1.text(x=20, y=6, s='$^{*}p=0.000$', fontsize=20)
ax1.set_title("对照组", y=-0.2, fontsize=20)
set_ax(ax1)
plt.show()
