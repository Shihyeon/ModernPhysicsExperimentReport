import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
from numpy import genfromtxt
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter

data = genfromtxt('data1.csv', delimiter=',', encoding='UTF8')

## from row=3 to infty, column=0에 대해 low=0을 출력
X1 = data[3:, 0]
## from row=3 to infty, column=1에 대해 low=1을 출력
Y1 = data[3:, 1]

# Figure
fig, ax = plt.subplots()
plt.plot(X, Y, color='k', linestyle='solid', linewidth=1)

# Figure title
plt.xlabel('Bragg angle (2$\\theta$, degree)')
plt.ylabel('Intensity (cps)')

# figure tick setting
plt.tick_params(axis='x', labelsize=10, direction='in')    # tick setting
plt.tick_params(axis='y', labelsize=10, direction='in')

# figure minor tick setting
ax.tick_params(axis='x', which='minor', bottom=True, direction='in')
ax.tick_params(axis='y', which='minor', left=True, direction='in')
## x값이 5의 배수일 때마다 메인 눈금 표시
ax.xaxis.set_major_locator(MultipleLocator(10)) 
ax.yaxis.set_major_locator(MultipleLocator(500))
## 메인 눈금이 표시될 형식
ax.xaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_major_formatter('{x:.0f}')  
## 서브 눈금은 x값이 n의 배수인 경우마다 표시
ax.xaxis.set_minor_locator(MultipleLocator(5)) 
ax.yaxis.set_minor_locator(MultipleLocator(250))

# Plot show
plt.show()