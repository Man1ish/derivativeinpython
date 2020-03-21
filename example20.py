# Example 18: Find the derivative of the power function  f(x) = x**n

import sympy as sp
x = sp.symbols('x')
f = sp.ln(x)
der = sp.diff(f,x)
print(der)

# output : 1/x