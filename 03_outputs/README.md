# Output
To display information in python, we use the built-in funtion [**`print()`**](https://www.w3schools.com/python/ref_func_print.asp). Depending on whether we want to display a simple message or the value of a variable, this function can be used in several ways.

## Displaying a simple message
To display a simple message, all we have to do is write the message we want to be printed in single or double quotes within the [**`print()`**](https://www.w3schools.com/python/ref_func_print.asp) function.

### Example
```python
print('Oil and Gas')
print('Hello', 'Petroleum Engineers!')  # Displays the two messages seperated by a space 
```

## Displaying the value of a variable
There are several ways to display the value of variable in python, including:
- Concatenation
- Formatted string literals
- The string `format()` method

### Example
```python
name = 'Alice Kruger'
age = 24

# All of the following will display the same output

# 1. Concatenation
print('Hi! My name is ' + name + '.')
print('I am ' + str(age) + ' year(s) old.')

# 2. Formatted string literals
print(f'Hi! My name is {name}.')
print(f'I am {age} year(s) old.')

# 3. The string format() method
print('Hi! My name is {}.'.format(name))
print('I am {} year(s) old.'.format(age))
```


# 📚 References
- 🔗 [W3schools: Python print() Function](https://www.w3schools.com/python/ref_func_print.asp)
- 🔗 [W3schools: Python Built in Functions](https://www.w3schools.com/python/python_ref_functions.asp)
- 🔗 [Python: Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

