# Python Programming Notes

---

# Section 1

# Variables, String Formatting, Comments & Assignment

## 1. Python Variables

### What are Variables?

Variables are **containers for holding data values** - they store information that can be used later in your program.

### Basic Variable Creation

```python
cost = 10
print(cost)  # Output: 10

```

### Variable Rules and Types

### Integer Variables

- Store whole numbers (no decimals)
- Example: `cost = 10`

### Float Variables

- Store decimal numbers
- Example: `tax_percent = 0.25`

### String Variables

- Store text data
- Must be surrounded by quotes (single ' or double ")
- Example: `username = "coding with Ruby"`

### Variable Reassignment

```python
first_num = 10      # Initially 10
print(first_num)    # Output: 10
first_num = 1       # Reassigned to 1
print(first_num)    # Output: 1

```

### Practical Example: Tax Calculator

```python
cost = 10
tax_percent = 0.25
tax = cost * tax_percent
price = cost + tax
print(price)  # Output: 12.5

```

**Visual Representation:**

```
Original Cost: $10.00
Tax (25%):     $2.50
Final Price:   $12.50

```

---

## 2. String Formatting

### Basic String Concatenation

```python
first_name = "Eric"
print("Hi " + first_name)  # Output: Hi Eric

```

### F-String Formatting (Recommended)

```python
first_name = "Eric"
print(f"Hi {first_name}")  # Output: Hi Eric

```

### Format Method

```python
sentence = "Hi {}"
first_name = "Eric"
print(sentence.format(first_name))  # Output: Hi Eric

```

### Multiple Variables in Formatting

```python
first_name = "Eric"
last_name = "Robbie"

# Using F-strings
print(f"Hi {first_name} {last_name}")

# Using format method
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))

```

**Output:** Hi Eric Robbie

---

## 3. Python Comments

### What are Comments?

Comments are text that **doesn't run** when your program executes. They help developers understand code.

### Single Line Comments

```python
# This is a single line comment
print("Hello World")  # This also works

```

### Multi-Line Comments

### Method 1: Multiple Hash Signs

```python
# This comment goes over
# multiple lines
# using hash signs

```

### Method 2: Triple Quotes

```python
"""
This is a multi-line comment
using triple double quotes
It can span many lines
"""

'''
This also works with
triple single quotes
'''

```

### Comment Examples

```python
# Going to print Hello World
print("Hello World")
print("Hi Eric")

# If you comment out code, it won't run
# print("This won't appear")

```

---

## 4. Assignment Problem Solution

### Problem Statement

- You have $50
- Buy an item costing $15
- Tax is 3%
- Calculate money left

### Solution Method 1: Using Variables

```python
money = 50
item = 15
tax = 0.03

money_left = money - item - (item * tax)
print(money_left)  # Output: 34.55

```

### Solution Method 2: Direct Calculation

```python
print(50 - 15 - (15 * 0.03))  # Output: 34.55

```

### Calculation Breakdown

```
Starting money:     $50.00
Item cost:          $15.00
Tax (3% of $15):    $0.45
Total spent:        $15.45
Money left:         $34.55

```

**Visual Calculation:**

```
$50.00 (start)
-$15.00 (item)
-$0.45 (tax)
________
$34.55 (remaining)

```

---

## Key Takeaways

1. **Variables** store data and can be reassigned
2. **F-strings** (`f"text {variable}"`) are the preferred formatting method
3. **Comments** use `#` for single lines or `"""` for multiple lines
4. **Problem-solving** can use variables (clearer) or direct calculations (shorter)

## Data Types Summary

```
INTEGER:  whole numbers (10, 5, -3)
FLOAT:    decimal numbers (0.25, 12.5, -1.75)
STRING:   text in quotes ("Hello", 'World')

```

---

---

---

# Section 2

## Python Programming Notes: String Formatting & User Input

## 1. String Formatting (Advanced)

### Basic String Creation and Printing

```python
first_name = "Eric"
print(first_name)  # Output: Eric

```

### String Concatenation Methods

### Method 1: Using + Operator

```python
first_name = "Eric"
print("Hi " + first_name)  # Output: Hi Eric

```

**Note:** Remember to add spaces manually: `"Hi " + first_name`

### Method 2: F-String Formatting (Recommended)

```python
first_name = "Eric"
print(f"Hi {first_name}")  # Output: Hi Eric

```

- Put `f` before the opening quote
- Wrap variables in curly braces `{}`
- No need for + signs

### Method 3: Format Method

```python
sentence = "Hi {}"
first_name = "Eric"
print(sentence.format(first_name))  # Output: Hi Eric

```

### Multiple Variables in Formatting

```python
first_name = "Eric"
last_name = "Robbie"

# F-string method
print(f"Hi {first_name} {last_name}, I hope you are learning")

# Format method
sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))

```

### Multi-line Strings in Code

```python
# PyCharm automatically formats long strings
print(f"Hi {first_name}, only {days} "
      f"days until your birthday")

```

---

## 2. User Input

### Basic Input Function

```python
first_name = input("Enter your first name: ")
print(first_name)

```

**How it works:**

```
Program asks: "Enter your first name: "
User types: Eric
Program stores: "Eric" in first_name variable
Program prints: Eric

```

### Multiple Input Example

```python
first_name = input("Enter your first name: ")
days = input("How many days before your birthday? ")

print(f"Hi {first_name}, only {days} days until your birthday")

```

**Visual Flow:**

```
Input 1: "Enter your first name: " → User: "Eric"
Input 2: "How many days before your birthday? " → User: "270"
Output: "Hi Eric, only 270 days until your birthday"

```

---

## 3. Data Type Conversion (Critical Concept)

### The Problem with Input

**Important:** All input from users comes as **strings**, even numbers!

```python
days = input("How many days until your birthday? ")
print(type(days))  # Output: <class 'str'>

```

### Type Checking

```python
days = input("Enter number of days: ")
print(type(days))  # Shows: <class 'str'>

```

### Converting String to Integer

```python
days = int(input("How many days until your birthday? "))
print(type(days))  # Shows: <class 'int'>

```

### The int() Function

- **Purpose:** Converts strings to integers
- **Syntax:** `int(value)`
- **Example:** `int("300")` returns `300` as integer

---

## 4. String Assignment - Practical Example

### Problem Statement

- Ask user: days until birthday
- Calculate: approximate weeks (divide by 7)
- Allow decimals in result

### Solution Step-by-Step

### Step 1: Get User Input (Wrong Way)

```python
days = input("How many days until your birthday? ")
print(days / 7)  # ERROR! Can't divide string by number

```

### Step 2: Convert to Integer (Correct Way)

```python
days = int(input("How many days until your birthday? "))
weeks = days / 7
print(weeks)  # Output: 42.857142857142854

```

### Step 3: Round the Result (Optional)

```python
days = int(input("How many days until your birthday? "))
weeks = round(days / 7, 2)
print(weeks)  # Output: 42.86

```

### Complete Solution

```python
days = int(input("How many days until your birthday? "))
weeks = round(days / 7, 2)
print(f"That's approximately {weeks} weeks until your birthday!")

```

---

## 5. Important Functions

### round() Function

- **Purpose:** Rounds numbers to specified decimal places
- **Syntax:** `round(number, decimal_places)`
- **Examples:**

  ```python
  round(42.857142, 2)  # Returns: 42.86round(42.857142, 1)  # Returns: 42.9round(42.857142, 0)  # Returns: 43.0

  ```

### type() Function

- **Purpose:** Shows the data type of a variable
- **Examples:**

  ```python
  print(type("hello"))    # <class 'str'>print(type(42))         # <class 'int'>print(type(3.14))       # <class 'float'>

  ```

---

## 6. Common Error and Solution

### Error Message

```
TypeError: unsupported operand types for /: 'str' and 'int'

```

### What This Means

- You're trying to do math with a string
- Input always gives strings, even for numbers

### Solution

```python
# Wrong
age = input("Enter age: ")
print(age + 5)  # ERROR!

# Correct
age = int(input("Enter age: "))
print(age + 5)  # Works!

```

---

## 7. Visual Summary

### Data Flow Diagram

```
User Input → String → Convert to Int → Math Operations → Output

"300" → int("300") → 300 → 300/7 → 42.86

```

### String Formatting Comparison

```
Method 1: "Hi " + name           → "Hi Eric"
Method 2: f"Hi {name}"           → "Hi Eric"  ✅ Recommended
Method 3: "Hi {}".format(name)   → "Hi Eric"

```

---

## 8. Key Takeaways

1. **F-strings are the best** method for string formatting
2. **All user input is strings** - must convert for math
3. **Use int()** to convert string numbers to integers
4. **Use round()** to limit decimal places
5. **Check data types** with type() when debugging
6. **Plan your string formatting** for readability

### Practice Exercises

```python
# Exercise 1: Name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hi {name}, you are {age} years old")

# Exercise 2: Simple calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print(f"{num1} + {num2} = {result}")

```

**Remember:** Always convert user input to the correct data type before doing calculations!

---

---

---

---

---

# Section 3

# Lists, Sets, and Tuples - Study Notes

## 1. Lists in Python

### What is a List?

- A **list** is a collection of data stored in one variable
- Can hold multiple values instead of just one
- Uses **square brackets [ ]**
- Items are separated by commas

### Creating Lists

#### Number List:

```python
my_list = [80, 96, 72, 100, 8]
print(my_list)  # Output: [80, 96, 72, 100, 8]
```

#### String List:

```python
people_list = ["Devaza", "Adele", "Jeff"]
print(people_list)  # Output: ['Devaza', 'Adele', 'Jeff']
```

### List Indexing

- **Index** = specific position in a list
- **Always starts at 0** (not 1!)

```
Visual representation:
Index:  0    1    2     3     4
Value: [80, 96, 72, 100,  8]
```

#### Accessing Elements:

```python
print(my_list[0])  # Output: 80 (first element)
print(my_list[1])  # Output: 96 (second element)
print(my_list[-1]) # Output: 8 (last element)
```

#### Changing Elements:

```python
people_list[0] = "Mel"  # Changes "Devaza" to "Mel"
print(people_list[0])   # Output: Mel
```

### List Length

```python
print(len(people_list))  # Output: 3
```

### List Slicing

- **Slicing** = getting only part of a list
- Format: `list[start:end]`
- **Important**: End index is NOT included

```python
people_list = ["Devaza", "Adele", "Jeff"]
print(people_list[0:2])  # Output: ['Devaza', 'Adele']
# Starts at index 0, stops BEFORE index 2
```

```
Visual slicing example:
Index:    0        1       2
Value: ["Devaza", "Adele", "Jeff"]
         ↑________________↑
       start=0          end=2 (not included)
Result: ["Devaza", "Adele"]
```

### Adding to Lists

#### append() - Add to End:

```python
my_list.append(1000)
# Before: [80, 96, 72, 100, 8]
# After:  [80, 96, 72, 100, 8, 1000]
```

#### insert() - Add at Specific Position:

```python
my_list.insert(2, 1000)  # Insert 1000 at index 2
# Before: [80, 96, 72, 100, 8]
# After:  [80, 96, 1000, 72, 100, 8]
```

### Removing from Lists

#### remove() - Remove by Value:

```python
my_list.remove(8)  # Removes the value 8
```

#### pop() - Remove by Index:

```python
my_list.pop(0)  # Removes element at index 0
```

### Sorting Lists

```python
my_list.sort()  # Sorts numbers from smallest to largest
print(my_list)  # Output: [72, 96, 100, 1000, 1000]
```

---

## 2. Sets in Python

### What is a Set?

- Similar to lists but with key differences:
  - **No duplicates allowed**
  - **Unordered** (no specific order)
  - Uses **curly brackets { }**

### Creating Sets

```python
my_set = {1, 2, 3, 4, 5, 1, 2}  # Duplicates will be removed
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

### Key Set Properties

- **No indexing**: Cannot use `my_set[0]` (will cause error)
- **No duplicates**: Automatically removes duplicate values
- **Length ignores duplicates**: `len(my_set)` counts unique values only

### Set Operations

#### Adding Elements:

```python
my_set.add(6)  # Add single element
my_set.update({7, 8})  # Add multiple elements
```

#### Removing Elements:

```python
my_set.discard(3)  # Remove element with value 3
my_set.clear()     # Remove all elements
```

#### Looping Through Sets:

```python
for x in my_set:
    print(x)
```

---

## 3. Tuples in Python

### What is a Tuple?

- **Ordered** like lists
- **Unchangeable** (cannot modify after creation)
- Uses **parentheses ( )**

### Creating Tuples

```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
```

### Tuple Operations

#### Accessing Elements (Allowed):

```python
print(my_tuple[1])  # Output: 2
print(len(my_tuple))  # Output: 5
```

#### Modifying Elements (NOT Allowed):

```python
my_tuple[0] = 100  # ERROR! Cannot change tuple values
```

---

## 4. When to Use Each Data Structure

### Use Lists When:

- You need to change/modify data
- Order matters
- Most common choice for general use

### Use Sets When:

- You need to remove duplicates
- You need fast organization
- Order doesn't matter

### Use Tuples When:

- Data should never change
- You want to protect data from modification

---

## 5. Practice Assignment Solution

**Task**: Create a zoo list with 5 animals, then:

1. Delete animal at third index
2. Append new animal at end
3. Delete animal at beginning
4. Print all animals
5. Print first three animals

```python
# Step 1: Create list
zoo = ["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"]

# Step 2: Delete third index (index 3 = "Lion")
zoo.pop(3)

# Step 3: Append new animal
zoo.append("Lizard")

# Step 4: Delete beginning (index 0 = "Monkey")
zoo.pop(0)

# Step 5: Print all animals
print(zoo)  # Output: ['Zebra', 'Gorilla', 'Tiger', 'Lizard']

# Step 6: Print first three animals
print(zoo[0:3])  # Output: ['Zebra', 'Gorilla', 'Tiger']
```

---

## Quick Reference Chart

| Feature    | Lists | Sets | Tuples |
| ---------- | ----- | ---- | ------ |
| Brackets   | [ ]   | { }  | ( )    |
| Ordered    | ✓     | ✗    | ✓      |
| Changeable | ✓     | ✓    | ✗      |
| Duplicates | ✓     | ✗    | ✓      |
| Indexing   | ✓     | ✗    | ✓      |

**Remember**: Lists are the most commonly used data structure in Python programming!
