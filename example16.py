# Example 16: Find the derivative of the cosine function  y = cosx
import math
import sympy as sp
x = sp.symbols('x')
f = sp.cos(x)
der = sp.diff(f,x)
print(der)

# output : -sin(x)