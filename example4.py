# Example 4: Find the derivative of a linear function y = ax + b using the definition of derivative

import sympy as sp
x,a,b = sp.symbols('x, a, b')
f =  a * x + b
der = sp.diff(f,x)
print(der)

# output : a