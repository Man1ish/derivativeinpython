# Example 14: Differentiate the power function f(x) = x**4 using the limit definition
import math
import sympy as sp
x = sp.symbols('x')
f = x**4
der = sp.diff(f,x)
print(der)

# output : 4*x**3