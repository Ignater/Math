import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import math
# x_data = np.array([1, 3, 5, 7, 9])
#
# y_data = np.array([2, 5, 2, -1, 2])

x = np.array([i for i in np.arange(1, 9, 0.005)])

y = np.array([math.sqrt(i) for i in x])

x_data = np.array([i for i in np.arange(1, 10, 2)])

y_data = np.array([math.sqrt(i) for i in x_data])

x_data_smooth = np.linspace(min(x_data), max(x_data), 50)
# fig, ax = plt.subplots(1,1)

spl = UnivariateSpline(x_data, y_data, s=0, k=2)
y_data_smooth = spl(x_data_smooth)
plt.plot(x_data_smooth, y_data_smooth, 'black')

# plt.plot(x_data, y_data, 'red')
plt.plot(x, y, 'red')
plt.plot(x_data_smooth, y_data_smooth, 'black')
plt.scatter(x_data, y_data)
plt.show()