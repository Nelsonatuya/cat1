import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

degree = 2
coefficients = np.polyfit(x, y, degree)
polynomial = np.poly1d(coefficients)
y_fit = polynomial(x)
plt.scatter(x, y, label='Data points')
plt.plot(x, y_fit, label='Fitted curve', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

print(f"Polynomial coefficients: {coefficients}")
