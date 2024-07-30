def linear_interpolation(x,x0,x1,y0,y1):
    return y0 + (x-x0)*(y1-y0)/(x1-x0)

x=4
x0=2
y0=7.2
x1= 4.25
y1=7.1
y= linear_interpolation(x,x0,x1,y0,y1)
print(f"the value of y at point x {x} is = {y:.4f}")