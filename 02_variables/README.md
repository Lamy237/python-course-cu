# Variables

[**Variables**](https://www.learnpython.org/en/Variables_and_Types) are one of the most fundamental concepts in programming. They are not specific to python and exist in pretty much every programming language. 

We use variables to temporarily store data in a computer’s memory.

```python
area = 1750
water_saturation = 0.3  # 30%
branch = 'Petroleum Engineering'
```

When the python interpreter executes this code, it will:
- Allocate some memory, 
- Store the number **1750** in that memory 
- Attach the `area` label to that memory location

The scenario is the same for the other variables.

# Rules to create variables in Python

- A variable can consist of upper and lowercase letters, digits (_0-9_) and the underscore character.
- The first character of a variable cannot be a digit.
- Keywords like **if** or the Boolean **True** are reserved and cannot be used as variable names.
- Variables are case-sensitive; therefore `porosity` is different from `POROSITY`, `Porosity`, `PoRoSiTy`.

### Recommended Pratices

- Use snake_case for variable names that contain spaces
- Don’t use names that look like the digits 1 and 0 (such as lowercase L)

### Note
In python, you do not need to declare variables before using them, or declare their data type. This is because python is completely object oriented, i.e every variable in python is an object.

We use the [**`type()`**](https://www.w3schools.com/python/ref_func_type.asp) function to determine the type of a variable.

# Exercise

Let’s say you want to calculate the oil in place (OIP) for a hydrocarbon reservoir. To do so, you need to know various reservoir parameters such as the **area**, the **thickness**, the **porosity** and the **water saturation**.

Using the following data, create variables to store the values of those parameters using python syntax.

### Data

|Parameter                        | Value (units)                                 |
|---------------------------------|:----------------------------------------------|
|Area of the zone (A)             | 2000 acres                                    |
|Thickness (h)                    | 150 ft                                        |
|Porosity (ϕ)                     | 15%                                           |
|Water saturation (Sw)            | 30%                                           |

**Data source: Dr. Paul W.J. Glover, Petrophysics MSc Course Notes, (University of Aberdeen, 2000), pp. 285 - 287.**

