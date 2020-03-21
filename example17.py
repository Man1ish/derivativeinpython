# Example 17: Find the derivative of the trigonometric function  f(x) = sin2x using the limit definition

import sympy as sp
x = sp.symbols('x')
f = sp.sin(2*x)
der = sp.diff(f,x)
print(der)

# output : 2*cos(2*x)