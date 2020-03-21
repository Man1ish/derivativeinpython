# Example 11: Find the derivative of the function y = sqrt(x)
import math
import sympy as sp
x = sp.symbols('x')
f = sp.sqrt(x)
der = sp.diff(f,x)
print(der)

# output :1/(2*sqrt(x))