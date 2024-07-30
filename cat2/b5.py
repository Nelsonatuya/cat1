def linear_spline(x, y, x_new):
    for i in range(len(x) - 1):
        if x[i] <= x_new <= x[i + 1]:
            slope = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
            return y[i] + slope * (x_new - x[i])
    return None

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

x_new = 2.5
y_new = linear_spline(x, y, x_new)

print(f"Interpolated value at x={x_new}: {y_new}")
