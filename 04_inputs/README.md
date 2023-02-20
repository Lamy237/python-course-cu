# Input
To receive an input from the user in python, we use the built-in function [**`input()`**](https://www.geeksforgeeks.org/python-input-function/). The received input is returned as a string.

### Example
```python
name = input('What is your name? ')
color = input('What is your favorite color? ')
```

## Type Conversion/Casting
When we want to take data other than string data from the user, some type conversion is required. This is because the [**`input()`**](https://www.geeksforgeeks.org/python-input-function/) function returns everything as a string. Casting functions include:
- [`int()`](https://www.w3schools.com/python/ref_func_int.asp) : takes float or string as an argument and returns int type object.
- [`float()`](https://www.w3schools.com/python/ref_func_float.asp) : takes int or string as an argument and return float type object.
- [`str()`](https://www.w3schools.com/python/ref_func_str.asp) : takes float or int as an argument and return string type object.

**Note:** To find out the type of a variable, we use the function [**`type()`**](https://www.w3schools.com/python/ref_func_type.asp).

### Example
```python
# Get the reservoir porosity from the user

# Method 1
porosity = input('Enter the reservoir porosity: ')
porosity = int(porosity)

# Method 2
porosity = int(input('Enter the reservoir porosity: '))
porosity = porosity
```

# 📚 References
- 🔗 [GeeksforGeeks: Python input() Function](https://www.geeksforgeeks.org/python-input-function/)
- 🔗 [GeeksforGeeks: Type Casting in Python (Implicit and Explicit) with Examples](https://www.geeksforgeeks.org/type-casting-in-python-implicit-and-explicit-with-examples/)
- 🔗 [W3schools: Python Casting](https://www.w3schools.com/python/python_casting.asp)
- 🔗 [W3schools: Python Built in Functions](https://www.w3schools.com/python/python_ref_functions.asp)
- 🔗 [Python: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
