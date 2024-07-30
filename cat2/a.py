#false positioning method: f(x)=x**2-x-2 [l=1,u=3]

import math

def func(x):
    return x**2 - x - 2

def regula_falsi(l, u, max_iterations, tol):
    fl = func(l)
    fu = func(u)
    
    if fl * fu >= 0:
        print("no root")
        return None
    
    for i in range(max_iterations):
      
        x = (fl * u - fu * l) / (fl - fu)
        fx = func(x)
        if (abs(fx) <tol):
            return x
        print(f"iteration: {i+1}, x= ,{x}, fx=, {fx}")
        
        
       
        if fl * fx < 0:
            u = x
            fu = fx
        else:
            l = x
            fl = fx
       
    return fx
   
    


l = 1
u = 3
max_iterations = 3
tolerance = 1e-1


root = regula_falsi(l, u, max_iterations, tolerance)
print(f"The final root after {max_iterations} iterations is: {root}")
