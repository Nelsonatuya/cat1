#Numerical diffrentiation using trapezoidal rule.
def trapezoidal_rule(f, a, b, n=5):
    h = (b - a) / n 
     #n= the number of points to be created between the upper bound(b) and the lower bound(a)                            
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

def func(x):
    return x**2-x-2

a, b = 0, 1

integral = trapezoidal_rule(func, a, b)
print(f"Approximate integral of x^2 from {a} to {b}: {integral}")
