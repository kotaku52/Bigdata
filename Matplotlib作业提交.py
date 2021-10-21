"""
@FileName：Lecture6-3.py
@Description：
@Author：Kotaku52
@Time：2021/10/20 11:06
"""
from numpy import linspace, sin, pi
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist

x = linspace(-2 * pi, 2 * pi, 600)
y = sin(x)

fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis['x'] = ax.new_floating_axis(0, 0)
ax.axis['y'] = ax.new_floating_axis(1, 0)
ax.axis['x'].set_axis_direction('top')
ax.axis['x']
ax.axis['y'].set_axis_direction('left')
ax.axis['x'].set_axisline_style('->', size = 3)
ax.axis['y'].set_axisline_style('-|>', size = 3)
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.plot(x, y)
plt.show()