import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

slope, intercept, r_value, p_value, std_err = linregress(x, y)

y_fit = slope * x + intercept

plt.scatter(x, y, label='Data points')
plt.plot(x, y_fit, label='Fitted line', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
