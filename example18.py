# Example 18: Find an expression for the derivative of the exponential function  f(x) = e **x using the definition of derivative

import sympy as sp
x = sp.symbols('x')
f = sp.exp(x)
der = sp.diff(f,x)
print(der)

# output : exp(x)