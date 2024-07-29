## Python Fundamentals: Hello World, and Variables

### Writing Your First Python Program: Hello, World!

**1. Create a Python File:**
   * Use a text editor like Notepad or a dedicated code editor to create a new file.
   * Save the file with a `.py` extension (e.g., `hello.py`).

**2. Write the Code:**
   * Open the file and type the following code:
     ```python
     print("Hello, World!")
     ```

**3. Run the Program:**
   * Open Windows Terminal.
   * Navigate to the directory where you saved the `hello.py` file using the `cd` command.
   * Type `python hello.py` and press Enter.
   * The output "Hello, World!" will be displayed in the terminal.


## Python Variables and Data Types

Python is a dynamically-typed language, which means you don't have to declare the type of a variable when you create one. The interpreter infers the type of the variable based on the value you assign to it.

## Variables

A variable in Python is created the moment you first assign a value to it. For example:

```python
x = 5
name = "Alice"
print(x)
print(name)
```

In the above example, `x` is a variable assigned with an integer value `5`, and `name` is a variable assigned with a string value `"Alice"`.

### Variable Naming Rules

1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. The rest of the variable name can contain letters, numbers (0-9), or underscores.
3. Variable names are case-sensitive (e.g., `myVar` and `myvar` are different variables).
4. Avoid using Python reserved keywords (e.g., `if`, `else`, `while`, `for`, etc.).

Valid variable names:

```python
my_var = 10
_var = 5
Var123 = "Hello"
print(my_var)
print(_var)
print(Var123)
```

Invalid variable names:

```python
# 2var = 10  # starts with a number
# my-var = 5  # contains a hyphen
# class = "Python"  # 'class' is a reserved keyword
```

## Data Types

Python has several built-in data types, including:

### 1. String (`str`)

A string is a sequence of characters enclosed within single quotes `'` or double quotes `"`. 

```python
text = "Hello, World!"
name = 'Alice'
print(text)
print(name)
```

### 2. Integer (`int`)

An integer is a whole number without a fractional part. 

```python
number = 42
age = 30
print(number)
print(age)
```

### 3. Float (`float`)

A float is a number with a fractional part, represented by a decimal point.

```python
pi = 3.14
height = 5.9
print(pi)
print(height)
```

### 4. Complex (`complex`)

A complex number is represented by `a + bj`, where `a` is the real part and `b` is the imaginary part.

```python
complex_num = 1 + 2j
z = 3 - 4j
print(complex_num)
print(z)
```

### 5. List (`list`)

A list is an ordered collection of items, which can be of different types. Lists are mutable, meaning their elements can be changed.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.14]
print(fruits)
print(numbers)
print(mixed)
```

### 6. Tuple (`tuple`)

A tuple is an ordered collection of items similar to a list, but it is immutable, meaning once created, its elements cannot be changed.

```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
print(coordinates)
print(colors)
```

### 7. Dictionary (`dict`)

A dictionary is an unordered collection of key-value pairs. Each key must be unique and of an immutable type.

```python
person = {"name": "John", "age": 30}
inventory = {"apples": 5, "bananas": 10}
print(person)
print(inventory)
```

### 8. Set (`set`)

A set is an unordered collection of unique items. Sets are mutable.

```python
unique_numbers = {1, 2, 3, 4, 5}
letters = {'a', 'b', 'c'}
print(unique_numbers)
print(letters)
```

### 9. Boolean (`bool`)

A boolean is a type with two possible values: `True` and `False`.

```python
is_valid = True
is_empty = False
print(is_valid)
print(is_empty)
```


## Type Checking and Type Conversion in Python

### Type Checking

In Python, you can check the type of a variable using the `type()` function. Here are some examples:

```python
x = 5
y = 3.14
z = "Hello"
w = [1, 2, 3]

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(w))  # <class 'list'>
```

### Type Conversion

Type conversion in Python refers to the conversion of one data type to another. Python provides several built-in functions for this purpose:

1. **`int()`**: Converts a value to an integer.

```python
a = "123"
b = 3.14
c = "45.6"

print(int(a))  # 123
print(int(b))  # 3
# print(int(c))  # ValueError: invalid literal for int() with base 10: '45.6'
```

2. **`float()`**: Converts a value to a float.

```python
a = "123"
b = 3
c = "45.6"

print(float(a))  # 123.0
print(float(b))  # 3.0
print(float(c))  # 45.6
```

3. **`str()`**: Converts a value to a string.

```python
a = 123
b = 3.14
c = True

print(str(a))  # "123"
print(str(b))  # "3.14"
print(str(c))  # "True"
```

4. **`list()`**: Converts a value to a list.

```python
a = "hello"
b = (1, 2, 3)

print(list(a))  # ['h', 'e', 'l', 'l', 'o']
print(list(b))  # [1, 2, 3]
```

5. **`tuple()`**: Converts a value to a tuple.

```python
a = [1, 2, 3]
b = "hello"

print(tuple(a))  # (1, 2, 3)
print(tuple(b))  # ('h', 'e', 'l', 'l', 'o')
```

6. **`set()`**: Converts a value to a set.

```python
a = [1, 2, 3, 3, 2, 1]
b = "hello"

print(set(a))  # {1, 2, 3}
print(set(b))  # {'e', 'h', 'l', 'o'}
```

7. **`dict()`**: Converts a value to a dictionary (if applicable).

```python
a = [("name", "John"), ("age", 30)]

print(dict(a))  # {'name': 'John', 'age': 30}
```

8. **`bool()`**: Converts a value to a boolean.

```python
a = 1
b = 0
c = ""
d = "hello"

print(bool(a))  # True
print(bool(b))  # False
print(bool(c))  # False
print(bool(d))  # True
```

## Examples for List, Tuple, and Dictionary

### List

A list is an ordered collection of items. Lists are mutable, meaning their elements can be changed.

#### Creating a List

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
```

#### Retrieving Values from a List

You can retrieve values from a list using indexing (0-based) and slicing.

```python
# Retrieve the first item
first_fruit = fruits[0]
print(first_fruit)  # apple

# Retrieve the last item
last_fruit = fruits[-1]
print(last_fruit)  # date

# Retrieve a slice (second and third items)
some_fruits = fruits[1:3]
print(some_fruits)  # ['banana', 'cherry']
```

### Tuple

A tuple is an ordered collection of items similar to a list, but it is immutable, meaning once created, its elements cannot be changed.

#### Creating a Tuple

```python
coordinates = (10, 20, 30)
print(coordinates)  # (10, 20, 30)
```

#### Retrieving Values from a Tuple

You can retrieve values from a tuple using indexing and slicing, similar to lists.

```python
# Retrieve the first item
first_coordinate = coordinates[0]
print(first_coordinate)  # 10

# Retrieve the last item
last_coordinate = coordinates[-1]
print(last_coordinate)  # 30

# Retrieve a slice (first and second items)
some_coordinates = coordinates[0:2]
print(some_coordinates)  # (10, 20)
```

### Dictionary

A dictionary is an unordered collection of key-value pairs. Each key must be unique and of an immutable type.

#### Creating a Dictionary

```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person)  # {'name': 'John', 'age': 30, 'city': 'New York'}
```

#### Retrieving Values from a Dictionary

You can retrieve values from a dictionary using the keys.

```python
# Retrieve the value associated with the key 'name'
name = person["name"]
print(name)  # John

# Retrieve the value associated with the key 'age'
age = person["age"]
print(age)  # 30

# Retrieve the value associated with the key 'city'
city = person["city"]
print(city)  # New York
```

### Dictionary with List of Dictionaries and List of Strings

#### Creating a Complex Dictionary

```python
my_value = {
    "person": {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    "hobbies": ["reading", "swimming", "coding"],
    "friends": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 28},
        {"name": "Charlie", "age": 35}
    ]
}

print(my_value)
```

#### Retrieving Values from a Complex Dictionary

To retrieve values from such a complex dictionary, you need to use multiple indexing and key lookups.

```python
# Retrieve the name of the person
person_name = my_value["person"]["name"]
print(person_name)  # John

# Retrieve the first hobby
first_hobby = my_value["hobbies"][0]
print(first_hobby)  # reading

# Retrieve the name of the first friend
first_friend_name = my_value["friends"][0]["name"]
print(first_friend_name)  # Alice

# Retrieve the age of the second friend
second_friend_age = my_value["friends"][1]["age"]
print(second_friend_age)  # 28

# Retrieve all friends' names
all_friend_names = [friend["name"] for friend in my_value["friends"]]
print(all_friend_names)  # ['Alice', 'Bob', 'Charlie']
```

### Explanation

- **Nested Dictionary**: `my_value["person"]["name"]` retrieves the value associated with the key `name` inside the `person` dictionary.
- **List Indexing**: `my_value["hobbies"][0]` retrieves the first item from the `hobbies` list.
- **List of Dictionaries**: `my_value["friends"][0]["name"]` retrieves the name of the first dictionary in the `friends` list.
- **List Comprehension**: `[friend["name"] for friend in my_value["friends"]]` retrieves all names from the dictionaries inside the `friends` list.
