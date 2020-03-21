# Example 13: Calculate the derivative of cubic function y = x **3
import math
import sympy as sp
x = sp.symbols('x')
f = x**3
der = sp.diff(f,x)
print(der)

# output : 3*x**2