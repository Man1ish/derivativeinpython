import sympy as sp
x = sp.symbols('x')
f = 3* x + 2
der = sp.diff(f,x)
print(der)