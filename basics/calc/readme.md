
### Program Overview

This program performs basic arithmetic operations based on user input. It takes two integer values from the user and asks which arithmetic operation they would like to perform. Based on the user's choice, it performs the operation and prints the result. If the operation is not recognized, it displays an error message.

### Detailed Explanation

#### 1. **Input Values**

```python
val1 = int(input("Enter Number 1: "))
val2 = int(input("Enter Number 2: "))
```

- **`input()` Function**: Used to take input from the user. It returns the input as a string.
- **`int()` Function**: Converts the string input into an integer.
- **`val1` and `val2`**: These variables store the integer values input by the user.

**Example**:
If the user inputs `5` for `val1` and `3` for `val2`, then:
- `val1` will be `5`
- `val2` will be `3`

#### 2. **Operation Input**

```python
opp = input("which operation would you like to perform ? eg: +, -, *, / :- ")
```

- **`input()` Function**: Used again to take the operation symbol as a string.
- **`opp`**: This variable stores the operation symbol (e.g., `+`, `-`, `*`, `/`) provided by the user.

**Example**:
If the user inputs `+`, then `opp` will be `+`.

#### 3. **Conditionals to Perform Operations**

```python
if opp == "+":
    print(val1 + val2)
elif opp == "-":
    pass
elif opp == "*":
    print(val1 * val2)
elif opp == "/":
    print(val1 / val2)
else:
    print("not valid operation")
```

- **`if` Statement**: Checks if the `opp` variable matches the addition operator `+`.
  - **Action**: If `opp` is `+`, it calculates `val1 + val2` and prints the result.

- **`elif` Statement**: Checks if the `opp` variable matches the subtraction operator `-`.
  - **Action**: If `opp` is `-`, it does nothing (`pass`). This means subtraction functionality is not implemented in this code.

- **`elif` Statement**: Checks if the `opp` variable matches the multiplication operator `*`.
  - **Action**: If `opp` is `*`, it calculates `val1 * val2` and prints the result.

- **`elif` Statement**: Checks if the `opp` variable matches the division operator `/`.
  - **Action**: If `opp` is `/`, it calculates `val1 / val2` and prints the result. Note that if `val2` is `0`, this will raise a `ZeroDivisionError`.

- **`else` Statement**: Handles any cases where `opp` does not match any of the recognized operators.
  - **Action**: Prints "not valid operation" to indicate that the input was not a recognized operation symbol.

### Additional Notes

- **Error Handling**: The program does not handle invalid inputs (e.g., if the user enters a non-integer value or tries to divide by zero). It might be useful to add error handling to manage these cases.
  
- **Using `pass`**: The `pass` statement is a placeholder used in the `elif` block for subtraction. It does not perform any operation but is used to indicate where code could be added later.

- **Division by Zero**: The program does not check if `val2` is `0` before performing division, which will result in a runtime error if it occurs.
