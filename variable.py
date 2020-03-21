import sympy as sp
x = sp.symbols('x')
f = x
der = sp.diff(f,x)
print(der)