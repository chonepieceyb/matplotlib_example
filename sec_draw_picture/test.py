# import matplotlib.pyplot as plt
# import numpy as np

# # Create some example data
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = x
# y4 = x**2

# # Create a 2x2 grid of subplots, sharing both x and y axes
# fig, ax = plt.subplots(2, 1, sharex=True, sharey=True)

# # Plot data on each subplot
# ax[0].plot(x, y1, label='sin(x)')
# # ax[0, 1].plot(x, y2, label='cos(x)')
# ax[1].plot(x, y3, label='linear')
# # ax[1, 1].plot(x, y4, label='quadratic')

# # Add legends to each subplot
# ax[0].legend()
# # ax[0, 1].legend()
# ax[1].legend()
# # ax[1, 1].legend()

# # Add labels to axes and a title to the overall figure
# fig.suptitle('Example Subplots')
# for axis in ax.flat:
#     axis.set(xlabel='x-axis', ylabel='y-axis')

# # Adjust layout to prevent clipping of labels
# plt.tight_layout()

# # Show the plot
# plt.show()

# import matplotlib.pyplot as plt

# # 创建示例数据
# x = [1, 2, 3, 4, 5]
# y = [2, 5, 1, 7, 4]

# # 创建子图
# fig, ax = plt.subplots()

# # 绘制折线图
# ax.plot(x, y)

# # 设置 x 轴范围
# ax.set_xlim(1, 5)

# # 显示图形
# plt.show()

# import matplotlib.pyplot as plt

# # 创建示例数据
# x = [1, 2, 3, 4, 5]
# y1 = [2, 5, 1, 7, 4]
# y2 = [1, 4, 2, 6, 3]

# # 创建子图
# fig, ax = plt.subplots()

# # 绘制两个折线图
# line1, = ax.plot(x, y1, label='Line 1')
# line2, = ax.plot(x, y2, label='Line 2')

# # 获取图例信息
# handles, labels = ax.get_legend_handles_labels()

# # 显示图例
# ax.legend(handles, labels)

# # 显示图形
# plt.show()

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(13, 4))
# 构造x轴刻度标签、数据
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
first = [20, 34, 30, 35, 27]
second = [25, 32, 34, 20, 25]
third = [21, 31, 37, 21, 28]
fourth = [26, 31, 35, 27, 21]

# 两组数据
plt.subplot(131)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width/2，x + width/2即每组数据在x轴上的位置
plt.bar(x - width/2, first, width, label='1')
plt.bar(x + width/2, second, width, label='2')
plt.ylabel('Scores')
plt.title('2 datasets')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
# 三组数据
plt.subplot(132)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width，x， x + width即每组数据在x轴上的位置
plt.bar(x - width, first, width, label='1')
plt.bar(x, second, width, label='2')
plt.bar(x + width, third, width, label='3')
plt.ylabel('Scores')
plt.title('3 datasets')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
# 四组数据
plt.subplot(133)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.2  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
plt.bar(x - 1.5*width, first, width, label='1')
plt.bar(x - 0.5*width, second, width, label='2')
plt.bar(x + 0.5*width, third, width, label='3')
plt.bar(x + 1.5*width, fourth, width, label='4')
plt.ylabel('Scores')
plt.title('4 datasets')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()

plt.show()




