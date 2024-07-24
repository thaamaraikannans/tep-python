## Python Basics: Installation, Verification, Hello World, and Variables

### Installing Python on Windows

**1. Download the Installer:**
   * Visit the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).
   * Choose the appropriate Python version (usually the latest stable release).
   * Download the Windows installer.

**2. Run the Installer:**
   * Double-click the downloaded installer.
   * Ensure "Add Python 3.x to PATH" is checked.
   * Click "Install Now" for default settings or customize installation options as needed.

### Verifying Python Installation on Windows Terminal

**1. Open Windows Terminal:**
   * Press `Win + R` to open the Run dialog.
   * Type `cmd` and press Enter.

**2. Check Python Version:**
   * Type `python --version` and press Enter.
   * If Python is installed correctly, you'll see the installed Python version.

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

### Understanding Variables in Python

A variable is a named storage location that holds a value. You can assign different data types to variables.

**Basic Data Types:**

* **Numbers:**
  * Integers (whole numbers): `x = 10`
  * Floating-point numbers (numbers with decimals): `y = 3.14`
* **Strings:**
  * Textual data: `name = "Alice"`
* **Booleans:**
  * True or False values: `is_active = True`

**Example:**

```python
# Assigning values to variables
message = "Hello, Python!"
number = 42
is_valid = False

# Printing variable values
print(message)
print(number)
print(is_valid)
```

**Key points about variables:**

* Variable names should be descriptive and meaningful.
* Python is dynamically typed, so you don't need to specify the data type explicitly.
* You can change the value of a variable later in your code.
