import numpy as np

def gradient_descent(learning_rate, initial_guess, num_iterations):
    def f(x, y):
        return x**2 + y**2 - x*y + x - y + 1

    def df_dx(x, y):
        return 2*x - y + 1

    def df_dy(x, y):
        return 2*y - x - 1

    
    x, y = initial_guess
    for i in range(num_iterations):
        grad_x = df_dx(x, y)
        grad_y = df_dy(x, y)
        
        x = x - learning_rate * grad_x
        y = y - learning_rate * grad_y

        print(f"Iteration {i+1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {f(x, y):.4f}")

    return x, y

learning_rate = 0.1
initial_guess = (0, 0)
num_iterations = 5

final_x, final_y = gradient_descent(learning_rate, initial_guess, num_iterations)
print(f"Final result: x = {final_x:.4f}, y = {final_y:.4f}")
