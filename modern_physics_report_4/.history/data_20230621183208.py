import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter

data = genfromtxt('data.csv', delimiter=',', encoding='UTF8')

## 모든(:) column=0에 대해 low=0을 출력
X = data[:, 0]
## 모든(:) column=1에 대해 low=1을 출력
Y = data[:, 1]

# Yhat = savitzky_golay(Y, 51, 3)

# Smot
def smooth(Y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(Y, box, mode='same')
    return y_smooth

# Figure
fig, ax = plt.subplots()
plt.plot(X, Y, color='b', marker='.', markersize=5, linewidth=0)
plt.plot(X, smooth(Y,19), color='g', marker='.', markersize=5, linewidth=0)

# Figure title
plt.xlabel('The acceleration voltage ($U_2/10$, V/10)')
plt.ylabel('The electron current flowing to the collector')

# figure tick setting
plt.tick_params(axis='x', labelsize=10, direction='in')    # tick setting
plt.tick_params(axis='y', labelsize=10, direction='in')

# figure minor tick setting
ax.tick_params(axis='x', which='minor', bottom=True, direction='in')
ax.tick_params(axis='y', which='minor', left=True, direction='in')
## x값이 5의 배수일 때마다 메인 눈금 표시
ax.xaxis.set_major_locator(MultipleLocator(2)) 
ax.yaxis.set_major_locator(MultipleLocator(2))
## 메인 눈금이 표시될 형식
ax.xaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_major_formatter('{x:.0f}')  
## 서브 눈금은 x값이 1의 배수인 경우마다 표시
ax.xaxis.set_minor_locator(MultipleLocator(1)) 
ax.yaxis.set_minor_locator(MultipleLocator(1))

# Plot show
plt.show()