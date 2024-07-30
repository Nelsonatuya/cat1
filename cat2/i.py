import numpy as np

def lagrange_coefficients(xi, yi):
    n = len(xi)
    coeffs = [0] * n
    
    def lagrange_basis(x, i):
        result = 1
        for j in range(n):
            if i != j:
                result *= (x - xi[j]) / (xi[i] - xi[j])
        return result

    def compute_polynomial_coefficients():
        from sympy import symbols, expand
        x = symbols('x')
        polynomial = 0
        for i in range(n):
            term = yi[i] * lagrange_basis(x, i)
            polynomial += term
        expanded_polynomial = expand(polynomial)
        return expanded_polynomial

    expanded_polynomial = compute_polynomial_coefficients()
    
    poly_coeffs = [float(coeff) for coeff in expanded_polynomial.as_poly().all_coeffs()]
    
    return poly_coeffs

xi = [1, 2, 3, 4]
yi = [1, 4, 9, 16]

coeffs = lagrange_coefficients(xi, yi)
print(f"Polynomial coefficients: {coeffs}")
