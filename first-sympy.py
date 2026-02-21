from sympy import symbols, factor

x = symbols('x')

a = factor(x**15 - 1)

print(a)