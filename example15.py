# Example 15: Find the derivative of the sine function  f(x) = sinx
import math
import sympy as sp
x = sp.symbols('x')
f = sp.sin(x)
der = sp.diff(f,x)
print(der)

# output : cos(x)