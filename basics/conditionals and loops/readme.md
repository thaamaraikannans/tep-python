
## Conditionals in Python

### Indentation

- **Definition**: In Python, indentation is used to define the scope of code blocks. Indentation determines which statements are executed together. It is crucial for defining the structure of conditionals, loops, functions, and other control statements.

- **Syntax**: Python uses whitespace (spaces or tabs) for indentation. The standard convention is to use 4 spaces per indentation level.

- **Example**:

  ```python
  if condition:
      # Indented block
      statement1
      statement2
  else:
      # Another indented block
      statement3
  ```

  In this example, `statement1` and `statement2` are executed if `condition` is `True`, while `statement3` is executed if the condition is `False`.

### Indentation Error

- **Definition**: An indentation error occurs when the code does not follow the consistent indentation level required by Python. This often happens when mixing tabs and spaces, or when the indentation is not uniform.

- **Common Causes**:
  - Mixing tabs and spaces.
  - Incorrect indentation level after control statements like `if`, `for`, `while`, etc.
  - Misalignment of code blocks.

- **Example of an Indentation Error**:

  ```python
  if condition:
      print("Condition is True")
    print("This will cause an indentation error")
  ```

  **Error Message**:

  ```
  IndentationError: unindent does not match any outer indentation level
  ```

- **Example of Correct Indentation**:

  ```python
  if condition:
      print("Condition is True")
      print("This is properly indented")
  ```

  In this corrected version, both `print` statements are at the same indentation level within the `if` block.

## `for` Loop in Python

### Indentation

- **Definition**: Indentation is used to define the body of the `for` loop. All statements that are part of the loop must be consistently indented.

- **Example**:

  ```python
  for i in range(5):
      print(i)  # This line is inside the loop
      # Other statements in the loop can be added here
  ```

### Indentation Error in Loops

- **Definition**: An indentation error in a loop occurs if the code inside the loop is not indented correctly. This can lead to runtime errors or logical errors.

- **Common Causes**:
  - Incorrect indentation after the `for` statement.
  - Mixing tabs and spaces within the loop block.

- **Example of an Indentation Error**:

  ```python
  for i in range(5):
      print(i)
            print("This line will cause an indentation error")
  ```

  **Error Message**:

  ```
  IndentationError: unexpected indent
  ```

- **Example of Correct Indentation**:

  ```python
  for i in range(5):
      print(i)  # Correctly indented within the loop
      # Other properly indented statements
  ```

### Summary

- **Indentation**: Essential for defining the structure of code blocks in Python. Consistent use of indentation is crucial for correct program execution and readability.
- **Indentation Errors**: Can occur due to inconsistent indentation, mixing tabs and spaces, or incorrect alignment of code blocks.

Proper indentation ensures that your code is executed as intended and helps maintain clarity and organization in your Python programs.