##To display calculation results in SymPy, the ‘print()’ function is required.

When running in VSCode or similar environments, the `print()` function is essential to display calculation results.
Without it, only memory addresses will be shown, and the actual results will not be visible.


```python
from sympy import symbols, factor
x = symbols('x')

# ☓
factor(x**2 - 1)

# ○
print(factor(x**2 - 1))
```
or

```python
from sympy import symbols, factor

x = symbols('x')
a = factor(x**2 - 1)
print(a)

#'a' can be anything as long as it doesn't overlap with the others.


