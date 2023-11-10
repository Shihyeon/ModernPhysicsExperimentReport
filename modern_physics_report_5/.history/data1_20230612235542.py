import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter, FormatStrFormatter
from matplotlib.dates import MonthLocator, DateFormatter
from matplotlib.transforms import Bbox

# Data1
data = genfromtxt('data1.csv', delimiter=',', encoding='UTF8', dtype=float)
## 모든(:) column=0에 대해 row=0을 출력
X = data[:, 0]
## 모든(:) column=1에 대해 row=1을 출력
Y1 = data[:, 1]
## 모든(:) column=2에 대해 row=1을 출력
Y2 = data[:, 2]

# Figure
fig, ax = plt.subplots()
plt.plot(X, Y2, label='$D_2$', color='k', marker='s', markersize=5, linestyle='solid', linewidth=1)
plt.plot(X, Y1, label='$D_1$', color='k', marker='o', markersize=5, linestyle='solid', linewidth=1)

# Figure title
plt.xlabel('Acceleration voltage ($U$, kV)')
plt.ylabel('Diameter (cm)')

# Place a legend on the Axes. (location=0='best')
plt.legend(loc=0)

# Figure tick setting
plt.tick_params(axis='x', labelsize=10, direction='in')
plt.tick_params(axis='y', labelsize=10, direction='in')

# Figure minor tick setting
ax.tick_params(axis='x', which='minor', bottom=True, direction='in')
ax.tick_params(axis='y', which='minor', left=True, direction='in')
## x값이 n의 배수일 때마다 메인 눈금 표시
ax.xaxis.set_major_locator(MultipleLocator(.5)) 
ax.yaxis.set_major_locator(MultipleLocator(.5))
## 메인 눈금이 표시될 형식
ax.xaxis.set_major_formatter('{x}')
ax.yaxis.set_major_formatter('{x}')
## 서브 눈금은 x값이 n의 배수인 경우마다 표시
ax.xaxis.set_minor_locator(MultipleLocator(.25)) 
ax.yaxis.set_minor_locator(MultipleLocator(.25))

# Plot show
plt.show()