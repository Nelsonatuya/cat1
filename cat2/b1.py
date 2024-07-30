def forward_finite_divided_difference(f, x, h=1):
    return (f(x + h) - f(x)) / h

def func(x):
    return x**2+x-2

x = 2

approx_derivative = forward_finite_divided_difference(func, x)
print(f"the derivative of the function at x={x}: is=  {approx_derivative}")
