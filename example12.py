# Example 12: Determine the derivative of the cube root function f(x) = cuberoot(x) using the limit definition
import math
import sympy as sp
x = sp.symbols('x')
f = sp.real_root(x,3)
der = sp.diff(f,x)
print(der)

# output :