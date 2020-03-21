# Example 8: Using the definition of the derivative, find the derivative of the function y = 1/x

import sympy as sp
x = sp.symbols('x')
f = 1/x
der = sp.diff(f,x)
print(der)

# output :-1/x**2