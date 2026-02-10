# Good Coding Practices

## Table of Contents
1. [Introduction](#introduction)
2. [Micro Level Coding Practices](#micro-level-coding-practices)
   - [Introductory Video](#introductory-video)
   - [Guidelines](#guidelines)
   - [Practice 1](#practice-1)
   - [Black Formatter](#black-formatter)
   - [Practice 2](#practice-2)
3. [Macro Level Coding Practices](#macro-level-coding-practices)
   - [Introductory Video](#introductory-video)
   - [Guidelines](#guidelines)
   - [Practice 1](#practice-1)
   - [Practice 2](#practice-2)
4. [Summary](#summary)

---

## Introduction

Welcome to the module on good coding practices! Congratulations on finishing your basic Python programming course. Now that you have learned how to write functioning Python code, it's time to make it readable and maintainable so that it can be kept up and expanded on by other developers.

This guide consists of **2 main sections**:

- **Micro Level Coding Practices**: Good formatting practices for legibility
- **Macro Level Coding Practices**: Good code organization and structure

---

## Micro Level Coding Practices

Micro level coding practices focus on the formatting and style of individual lines and code blocks to ensure readability and consistency. Python's official style guide, **PEP 8**, provides detailed recommendations for writing clean, readable code.

### Introductory Video

Watch the video **`PEP8_guidelines_for_python_developers.mp4`** to get a feel for these micro level practices

### Guidelines

Below are key PEP 8 guidelines with examples.

#### Maximum Line Length

- Limit lines to **79 characters** for code and **72** for comments/docstrings
- Use backslashes for line continuation if necessary, but prefer parentheses for better readability

**✓ Good:**
```python
result = some_function(argument1, argument2,
                       argument3, argument4)
```

**✗ Bad:**
```python
result = some_function(argument1, argument2, argument3, argument4)  # Too long
```

---

#### Indentation

- Use **4 spaces** per indentation level
- **Never** mix tabs and spaces
- Align continuation lines with the opening delimiter or use hanging indentation

**✓ Good:**
```python
def function_name(param1, param2,
                  param3, param4):
    if condition:
        do_something()
```

**✗ Bad:**
```python
def function_name(param1, param2,
    param3, param4):  # Inconsistent indentation
	if condition:  # Tab instead of spaces
		do_something()
```

---

#### Blank Lines

- Use blank lines to separate top-level function and class definitions
- Use blank lines sparingly inside functions to indicate logical sections

**✓ Good:**
```python
def function1():
    pass


def function2():
    pass
```

---

#### Imports

- Place imports at the **top** of the file (after module comments and docstrings)
- **Group imports** in order: standard library, third-party, local
- Use **absolute imports** when possible

**✓ Good:**
```python
import os
import sys

from datetime import datetime
import requests

from mymodule import myfunction
```

**✗ Bad:**
```python
import os, sys  # Multiple imports on one line
from datetime import *  # Wildcard import
```

---

#### String Quotes

- Be **consistent** in your choice of quotes
- Our unit uses single quotes (') by default
- Use double quotes only if the string contains single quotes

**✓ Good:**
```python
name = 'John'
message = "It's a beautiful day"
```

---

#### Whitespace in Expressions and Statements

- Avoid extraneous whitespace
- Use spaces around operators and after commas
- Do **not** use spaces around the `=` sign for keyword arguments or default parameter values

**✓ Good:**
```python
x = 1 + 2
my_list = [1, 2, 3]

def test_func(object, key=8):
    pass
```

**✗ Bad:**
```python
x=1+2  # No spaces
my_list = [1,2,3]  # No spaces after commas
def test_func(object, key = 8):  # Spaces around = for default
    pass
```

---

#### Comments

- Comments should be **complete sentences**
- Use inline comments **sparingly**
- Keep comments **up to date** with your code

**✓ Good:**
```python
# Calculate the total price
total = price * quantity
```

---

#### Naming Conventions

Follow these naming standards across your codebase:

| Type | Convention | Example |
|------|-----------|---------|
| Functions & Variables | `snake_case` | `calculate_total()`, `user_age` |
| Classes | `PascalCase` | `ShoppingCart`, `UserManager` |
| Constants | `UPPERCASE` | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |

**✓ Good:**
```python
def calculate_total(price, quantity):
    TOTAL_DISCOUNT = 0.1
    class ShoppingCart:
        pass
```

**✗ Bad:**
```python
def CalculateTotal(price, quantity):  # CamelCase for function
    total_discount = 0.1  # Not uppercase for constant
    class shopping_cart:  # Not PascalCase
        pass
```

---

### Practice 1

In the folder, you will find the Python file **`micro_level_practice_1.py`**, which contains poor micro-level coding practices.

**Your task**: Use your knowledge of good micro practices to improve it manually, then format it with Black and compare the results.

---

### Black Formatter

Black is an **uncompromising Python code formatter** that automatically formats your code to conform to PEP 8 standards. It handles many micro-level formatting issues automatically, saving time and ensuring consistency across your team.

#### Installing Black

```bash
pip install black
```

#### Using Black

Format a single file:
```bash
black micro_level_practice_1.py
```

Format all Python files in a directory:
```bash
black .
```

#### What Black Does Automatically

- ✓ Fixes indentation (4 spaces)
- ✓ Adjusts line lengths (may exceed 79 chars if necessary)
- ✓ Adds proper spacing around operators and after commas
- ✓ Formats imports correctly
- ✓ Standardizes string quotes
- ✓ And more!

---

### Practice 2

In the folder, you will find the Python file **`micro_level_practice_2.py`**, which contains poor micro-level coding practices.

**Your task**: Use Black to format this file, and compare it to your formatted version of **`micro_level_practice_2.py`**

---

## Macro Level Coding Practices

Macro level coding practices focus on the **overall structure and organization** of your code, making it easier to maintain, scale, and collaborate on. These practices help create modular, reusable, and logical codebases.

### Introductory_video

Watch the video **`An_Introduction_to_Software_Design.mp4`** to get a feel for these micro level practices

### Guidelines

Below are key macro coding practices you should follow.

#### Avoid Hardcoding Variables

Hardcoding values directly in your code makes it inflexible and prone to errors. Instead, use variables or configuration files for values that might change.

**✗ Bad:**
```python
def calculate_discount(price: float) -> float:
    return price * 0.1  # Hardcoded discount rate
```

**✓ Good:**
```python
DISCOUNT_RATE = 0.1

def calculate_discount(price:float) -> float:
    return price * DISCOUNT_RATE
```

---

#### Define Constants at the Top of the File

Constants should be defined at the **module level**, preferably at the top after imports. This makes them easy to find and modify.

**✓ Good:**
```python
import math

# Constants
PI = 3.14159
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

def calculate_area(radius: float) -> float:
    return PI * radius ** 2
```

---
#### Clarify Function Input and Output Data Types

Functions should clearly describe their inputs and outputs and the resective datatypes for both. This improves readability and makes your code easier to use and maintain. 
Use type hints to clarify the datatypes of the functions inputs/ outputs, and docstrings to clarify and elaborate on the functions purpose 


**✗ Bad:**
```python
def find_average(values):
    return sum(values)/ len(values)
```

**✓ Good:**
```python

def find_average(values: List[float]) --> float: # type hints used to clarify functions inputs/outputs
    ''' 
    Function which takes in a list of floats, and returns the average value of the list.
    Inputs:
        values (List(Float)): List containing one or more floats
    Returns:
        average (Float): Float representing the average of the list
    ''' ## Use of docstring to document function
    average = sum(values)/ len(values)
    return average


```

---

#### Group Similar Functions Together

Organize your code by placing related functions close to each other. This improves readability and makes it easier to understand the code's purpose.

**✓ Good:**
```python
# string_utils.py

#################### String validation functions #################### 
def is_valid_email(email: str) -> bool:
    pass

def is_valid_phone(phone: str) -> bool:
    pass

#################### String formatting functions #################### 
def format_name(first: str, last: str) -> str:
    pass

def format_address(street: str, city: str, zip_code: str) -> str:
    pass
```

---
**
#### Standardise Inputs and Outputs Across Similar Functions

Functions that perform similar tasks should follow **consistent** input and output conventions. This makes code easier to understand, reduces mistakes, and allows functions to be used interchangeably.
**✗ Bad:**
```python
def get_usernames(users: list(dict)) -> list:
    """Return all usernames."""
    return [user["name"] for user in users]  # returns a list

def get_user_ages(users: list(dict)) -> dict:
    """Return all ages."""
    return {user["id"]: user["age"] for user in users}  # returns a dict
```


**✓ Good:**
```python
def get_usernames(users: list(dict)) -> list:
    """Return all usernames."""
    return {user["id"]: user["name"] for user in users}  # returns a dict

def get_user_ages(users: list(dict)) -> dict:
    """Return all ages."""
    return {user["name"]: user["age"] for user in users}  # returns a dict
```


---

#### Group Large Functionality into Classes and Use OOP

When functions become large or share related data, group them into classes. This encapsulates functionality into manageable chunks, improving code organization and maintainability.

**✗ Bad:**
```python
def create_user(name: str, email: str):
    # validation logic
    # database insertion
    pass

def update_user(user_id: int, name: str, email: str):
    # validation logic
    # database update
    pass

def delete_user(user_id: int):
    # database deletion
    pass
```

**✓ Good:**
```python
class UserManager:
    '''
    Class for the management of user data from a system
    
    Attributes:
        db (str): key for accessing the database #example

    Methods:
        create_user(name: str, email: str): Validate a new user and add to database
        update_user(user_id: int, name: str, email: str): Validates the user and updates his profile
        delete_user(user_id: int): Deletes user from database
    '''
    def __init__(self, db_connection):
        self.db = db_connection

    def create_user(self, name, email):
        # validation and creation logic
        pass

    def update_user(self, user_id, name, email):
        # validation and update logic
        pass

    def delete_user(self, user_id):
        # deletion logic
        pass
```

---


#### Use Modules for Imports

Break your code into logical Modules and import them appropriately. Modules can be easily maintained and reused across projects while making your project structure clearer and more professional.

Common modules include a utils folder, which contains functions that are used accross your project, though as your project becomes more complex, greater fragmentation may be necessary.

**Project Structure:**
```
my_project/
├── main.py
├── __init__.py
├── utils/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
└── models/
    ├── __init__.py
    └── User.py
```

**✓ Good:**
```python
# main.py
from utils.math_utils import calculate_average
from models.user import User

# Use the imported functions and classes
result = calculate_average([1, 2, 3, 4, 5])
user = User("John", "john@example.com")
```

---

### Practice 1

In the folder, you will find the Python file **`macro_level_practice_1.py`**, which contains poor macro-level coding practices organized into sections.

**Your task**: Refactor each section to follow the macro-level best practices outlined above. 

---

### Practice 2

In the folder, you will find the Python file **`macro_level_practice_2.py`**, which contains an extract of **REAL** SCVU code with poor coding practices.

**Your task**: Refactor this script to the best of your ability. At minimum, move the simple functions to a utils file, remove hardcoded variables, and group the large functionality into a single classs

---

## Summary

By following these micro and macro level coding practices, you will write code that is:

- ✓ **Readable** - Easy to understand at a glance
- ✓ **Maintainable** - Easy to modify and extend
- ✓ **Scalable** - Easy to grow without becoming complex
- ✓ **Professional** - Meets industry standards
- ✓ **Collaborative** - Easy for teams to work with

Happy coding! 🎉





