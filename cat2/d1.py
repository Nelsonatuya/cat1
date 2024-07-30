def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def f_prime(x):
    return 3*x**2 - 0.33*x

def newton_method(f, f_prime, x0, iterations):
    
    x = x0
    for i in range(iterations):
        fx = f(x)
        fpx = f_prime(x)
        
        if fpx == 0:
            print("no derivative")
        
        x_new = x - fx / fpx
        print(f"Iteration {i+1}: x = {x_new:.4f}, f(x) = {fx:.4e}")
        
        x = x_new
    
    return x

initial_guess = 0.1 
iterations = 3
depth = newton_method(f, f_prime, initial_guess, iterations)
print(f"Estimated depth after {iterations} iterations: {depth:.4f} meters")
