def func(x):
    return x**2 - x - 2

def diff(x, f, h=1 ) :
    return (f ( x + h )- f ( x )) /h

x=1.0
derivative= diff(func, x)
print({derivative})