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

---

---

---

---

# Section 4

# If, Elif, Else & Data Types

## 1. Flow Control Basics

### What is Flow Control?

- **Flow Control** = deciding which code to run based on conditions
- Uses `if`, `elif`, and `else` statements
- Controls the "flow" of your program

### Basic Structure

```
if condition:
    # Code runs if condition is True
elif another_condition:
    # Code runs if first condition is False but this one is True
else:
    # Code runs if all conditions are False

```

---

## 2. If Statements

### Basic If Statement

```python
x = 1

if x == 1:
    print("X is one")  # This will run

print("Outside of if statement")  # This always runs

```

**Output:**

```
X is one
Outside of if statement

```

### Important Notes:

- **Colon (:)** is required after the condition
- **Indentation** (4 spaces) shows which code belongs to the if statement
- Code outside the if block always runs

### Visual Representation:

```
x = 1
│
├─ if x == 1:           ← Condition check
│     print("X is one") ← Inside if block (4 spaces indent)
│
└─ print("Outside")     ← Outside if block (no indent)

```

---

## 3. If-Else Statements

### Basic If-Else

```python
x = 2

if x > 1:
    print("X is greater than one")
else:
    print("X is not greater than one")

```

### Practical Example - Time of Day:

```python
hour = 13

if hour < 15:
    print("Good morning")
else:
    print("Good afternoon")

```

**Logic Flow:**

```
hour = 13
│
├─ Is hour < 15? → YES → Print "Good morning"
└─ Is hour < 15? → NO  → Print "Good afternoon"

```

---

## 4. If-Elif-Else Statements

### Multiple Conditions

```python
hour = 18

if hour < 15:
    print("Good morning")
elif hour < 20:
    print("Good afternoon")
else:
    print("Good night")

```

### How It Works:

1. **First**: Check `if hour < 15`
2. **If False**: Check `elif hour < 20`
3. **If Also False**: Run `else` code

### Visual Flow Chart:

```
hour = 18
│
├─ hour < 15? → NO
│               │
├─ hour < 20? → YES → Print "Good afternoon"
│
└─ else → Print "Good night"

```

### Key Rules:

- Can have **multiple elif** statements
- Can have **only one if** and **only one else**
- **Order matters** - checks conditions from top to bottom

---

## 5. Boolean Data Types

### What are Booleans?

- **Boolean** = True or False values
- Used for conditions and logical operations

```python
like_coffee = True
like_tea = False
favorite_food = "pizza"
favorite_number = 32

print(type(like_coffee))     # Output: <class 'bool'>
print(type(like_tea))        # Output: <class 'bool'>
print(type(favorite_food))   # Output: <class 'str'>
print(type(favorite_number)) # Output: <class 'int'>

```

---

## 6. Comparison Operators

### Basic Comparison Operators:

| Operator | Meaning               | Example  | Result |
| -------- | --------------------- | -------- | ------ |
| `==`     | Equal to              | `5 == 5` | `True` |
| `!=`     | Not equal to          | `5 != 3` | `True` |
| `>`      | Greater than          | `5 > 3`  | `True` |
| `<`      | Less than             | `3 < 5`  | `True` |
| `>=`     | Greater than or equal | `5 >= 5` | `True` |
| `<=`     | Less than or equal    | `3 <= 5` | `True` |

### Examples:

```python
age = 18

if age >= 18:
    print("You can vote")
else:
    print("Too young to vote")

```

---

## 7. Logical Operators

### Three Main Logical Operators:

### AND Operator (`and`)

- **Both conditions must be True**

```python
age = 20
has_license = True

if age >= 18 and has_license:
    print("You can drive")

```

### OR Operator (`or`)

- **At least one condition must be True**

```python
day = "Saturday"
day2 = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

```

### NOT Operator (`not`)

- **Reverses True/False**

```python
is_raining = False

if not is_raining:
    print("Go for a walk!")  # This will run

```

### Truth Tables:

```
AND Truth Table:        OR Truth Table:         NOT Truth Table:
True  and True  = True  True  or True  = True   not True  = False
True  and False = False True  or False = True   not False = True
False and True  = False False or True  = True
False and False = False False or False = False

```

---

## 8. Practice Assignment Solution

### Assignment: Grade Calculator

**Task**: Create grade system using if/elif/else statements

- A = 90-100
- B = 80-89
- C = 70-79
- D = 60-69
- F = 0-59

### Solution:

```python
grade = 87

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Output: B

```

### Why This Works:

```
grade = 87
│
├─ grade >= 90? → NO  (87 is not >= 90)
├─ grade >= 80? → YES (87 is >= 80) → Print "B"
└─ (Stops checking remaining conditions)

```

### More Examples:

```python
# Example 1: grade = 95
if grade >= 90:    # 95 >= 90? YES → Print "A"

# Example 2: grade = 75
if grade >= 90:    # 75 >= 90? NO
elif grade >= 80:  # 75 >= 80? NO
elif grade >= 70:  # 75 >= 70? YES → Print "C"

# Example 3: grade = 45
# All conditions fail → else → Print "F"

```

---

## 9. Quick Reference

### Indentation Rules:

```python
if condition:
    # 4 spaces indentation
    print("Inside if block")
    # All code at same level belongs to if block
print("Outside if block")  # No indentation = outside block

```

### Common Mistakes to Avoid:

- ❌ Forgetting the colon `:` after conditions
- ❌ Wrong indentation (must be exactly 4 spaces)
- ❌ Using `=` instead of `==` for comparison
- ❌ Not considering the order of elif statements

### Best Practices:

- ✅ Use meaningful variable names
- ✅ Keep conditions simple and readable
- ✅ Order elif statements from most specific to least specific
- ✅ Always test edge cases (boundary values)

---

## 10. Data Type Summary

| Type    | Example              | Description     |
| ------- | -------------------- | --------------- |
| `bool`  | `True`, `False`      | Boolean values  |
| `int`   | `32`, `100`          | Whole numbers   |
| `str`   | `"pizza"`, `"hello"` | Text strings    |
| `float` | `3.14`, `2.5`        | Decimal numbers |

### Checking Data Types:

```python
value = True
print(type(value))  # Output: <class 'bool'>

```

**Remember**: Flow control is fundamental to programming - it makes your programs smart and interactive!

---

---

---

---

# Section 5

# Python Loops: For and While Loops

## 1. What are Loops?

### Definition

- **Loop** = a way to repeat code multiple times
- **Iterator** = a variable that goes through each item in a collection
- Saves time instead of writing repetitive code

### Why Use Loops?

**Without loops (bad way):**

```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # 1
print(my_list[1])  # 2
print(my_list[2])  # 3
print(my_list[3])  # 4
print(my_list[4])  # 5
```

**With loops (good way):**

```python
my_list = [1, 2, 3, 4, 5]
for x in my_list:
    print(x)  # Prints 1, 2, 3, 4, 5
```

---

## 2. For Loops

### Basic Structure

```python
for iterator in collection:
    # Code to repeat
```

### Simple For Loop Example

```python
my_list = [1, 2, 3, 4, 5]

for iterator in my_list:
    print(iterator)
```

**Output:**

```
1
2
3
4
5
```

### Visual Representation

```
my_list = [1, 2, 3, 4, 5]
           ↓   ↓   ↓   ↓   ↓
Iteration: 1st 2nd 3rd 4th 5th
iterator:  1   2   3   4   5
```

### Common Iterator Names

- Usually named: `x`, `i`, `item`, or any meaningful name

```python
for x in my_list:        # Most common
for i in my_list:        # Also common
for number in my_list:   # Descriptive name
```

---

## 3. For Loops with Range

### Using Range Function

```python
for x in range(3, 6):
    print(x)
```

**Output:**

```
3
4
5
```

### Range Parameters

- `range(start, stop)` - starts at `start`, stops before `stop`
- `range(10)` - starts at 0, stops before 10

### Visual Range Example

```
range(3, 6):
Numbers: 0  1  2  [3  4  5]  6  7  8...
              ↑   └─────┘   ↑
            start  included  stop (not included)
```

---

## 4. Practical For Loop Examples

### Example 1: Sum All Numbers

```python
my_list = [1, 2, 3, 4, 5]
sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x  # Same as: sum_of_for_loop = sum_of_for_loop + x

print(sum_of_for_loop)  # Output: 15
```

**Step-by-step process:**

```
Initial: sum_of_for_loop = 0
Iteration 1: sum_of_for_loop = 0 + 1 = 1
Iteration 2: sum_of_for_loop = 1 + 2 = 3
Iteration 3: sum_of_for_loop = 3 + 3 = 6
Iteration 4: sum_of_for_loop = 6 + 4 = 10
Iteration 5: sum_of_for_loop = 10 + 5 = 15
```

### Example 2: Loop Through Strings

```python
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]

for x in my_list:
    print(f"Happy {x}")
```

**Output:**

```
Happy Monday
Happy Tuesday
Happy Wednesday
Happy Thursday
```

---

## 5. While Loops

### Basic Structure

```python
while condition:
    # Code to repeat
    # Must change condition eventually!
```

### Simple While Loop Example

```python
i = 0

while i < 5:
    i += 1  # IMPORTANT: Change the condition variable!
    print(i)
```

**Output:**

```
1
2
3
4
5
```

### How While Loop Works

```
Step 1: i = 0, is 0 < 5? YES → i = 1, print 1
Step 2: i = 1, is 1 < 5? YES → i = 2, print 2
Step 3: i = 2, is 2 < 5? YES → i = 3, print 3
Step 4: i = 3, is 3 < 5? YES → i = 4, print 4
Step 5: i = 4, is 4 < 5? YES → i = 5, print 5
Step 6: i = 5, is 5 < 5? NO  → STOP LOOP
```

### ⚠️ Infinite Loop Warning

```python
# DANGER: This will run forever!
i = 0
while i < 5:
    print(i)  # i never changes, so condition is always True
```

**Always remember to change the condition variable inside the loop!**

---

## 6. Loop Control Statements

### Continue Statement

- **Continue** = skip the rest of current iteration, go to next iteration

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # Skip printing 3
    print(i)
```

**Output:**

```
1
2
4
5
```

### Visual Continue Flow

```
i = 1: print 1
i = 2: print 2
i = 3: continue → skip print, go back to start
i = 4: print 4
i = 5: print 5
```

### Break Statement

- **Break** = exit the loop completely

```python
i = 0
while i < 5:
    i += 1
    if i == 4:
        break  # Exit loop when i equals 4
    print(i)
```

**Output:**

```
1
2
3
```

### Visual Break Flow

```
i = 1: print 1
i = 2: print 2
i = 3: print 3
i = 4: break → EXIT LOOP COMPLETELY
i = 5: never reached
```

---

## 7. While Loop with Else

### While-Else Structure

```python
i = 0
while i < 5:
    i += 1
    print(i)
else:
    print("i is now larger or equal to 5")
```

**Output:**

```
1
2
3
4
5
i is now larger or equal to 5
```

### When Else Runs

- **Else runs** when while condition becomes False naturally
- **Else doesn't run** when loop exits with `break`

---

## 8. For vs While Loops

### When to Use For Loops

- **Use for loops when:**
  - You know how many times to loop
  - You're iterating through collections (lists, strings, etc.)
  - You need to process each item in a sequence

### When to Use While Loops

- **Use while loops when:**
  - You don't know how many iterations you need
  - You want to loop until a condition changes
  - You're waiting for something to happen

### Comparison Table

| Feature       | For Loop               | While Loop         |
| ------------- | ---------------------- | ------------------ |
| **Best for**  | Known iterations       | Unknown iterations |
| **Structure** | `for x in collection:` | `while condition:` |
| **Counter**   | Automatic              | Manual             |
| **Risk**      | Low                    | Infinite loop risk |

---

## 9. Practice Assignment Solution

### Assignment

- Create a while loop that prints all elements of my_list 3 times
- Use a for loop inside to print elements
- Skip printing "Monday" using continue

### Solution

```python
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# While loop counter
loop_count = 0

# While loop runs 3 times
while loop_count < 3:
    print(f"\n--- Round {loop_count + 1} ---")

    # For loop goes through each day
    for day in my_list:
        if day == "Monday":
            continue  # Skip Monday
        print(day)

    loop_count += 1  # Important: increment counter
```

**Output:**

```
--- Round 1 ---
Tuesday
Wednesday
Thursday
Friday

--- Round 2 ---
Tuesday
Wednesday
Thursday
Friday

--- Round 3 ---
Tuesday
Wednesday
Thursday
Friday
```

### Step-by-Step Explanation

```
Outer While Loop (runs 3 times):
├─ Round 1: loop_count = 0 < 3? YES
│   ├─ Inner For Loop:
│   │   ├─ day = "Monday" → continue (skip)
│   │   ├─ day = "Tuesday" → print
│   │   ├─ day = "Wednesday" → print
│   │   ├─ day = "Thursday" → print
│   │   └─ day = "Friday" → print
│   └─ loop_count = 1
├─ Round 2: loop_count = 1 < 3? YES
│   └─ (Same inner for loop process)
├─ Round 3: loop_count = 2 < 3? YES
│   └─ (Same inner for loop process)
└─ loop_count = 3 < 3? NO → END
```

---

## 10. Quick Reference

### Loop Syntax Cheat Sheet

```python
# FOR LOOP
for variable in collection:
    # code here

# WHILE LOOP
while condition:
    # code here
    # MUST change condition variable

# CONTINUE (skip current iteration)
if condition:
    continue

# BREAK (exit loop completely)
if condition:
    break
```

### Common Mistakes to Avoid

- ❌ Forgetting to change condition variable in while loops
- ❌ Using wrong indentation (must be 4 spaces)
- ❌ Forgetting colon `:` after for/while statements
- ❌ Creating infinite loops in while loops

### Best Practices

- ✅ Use meaningful variable names for iterators
- ✅ Always increment counter in while loops
- ✅ Use for loops for collections, while loops for conditions
- ✅ Test your loops with small data first
- ✅ Add print statements to debug loop behavior

**Remember**: Loops are essential for processing collections of data efficiently!

---

---

---

# Section 6

# Dictionaries and Functions

## 1. Dictionaries in Python

### What is a Dictionary?

- A dictionary stores data as **key-value pairs**
- Each key points to a specific value
- Uses curly brackets `{}` to create

### Creating a Dictionary

```python
user_dictionary = {
    "username": "coding with Ruby",
    "name": "Devaza",
    "age": 32
}

```

**ASCII Visualization:**

```
Dictionary Structure:
┌─────────────────────────────────┐
│  Key      │  Value             │
├─────────────────────────────────┤
│ "username" │ "coding with Ruby" │
│ "name"     │ "Devaza"          │
│ "age"      │ 32                │
└─────────────────────────────────┘

```

### Dictionary Operations

### Getting Values

```python
# Get specific value
print(user_dictionary.get("username"))  # Returns: coding with Ruby

```

### Adding New Key-Value Pairs

```python
user_dictionary["married"] = True

```

### Finding Dictionary Length

```python
print(len(user_dictionary))  # Returns: 4

```

### Removing Items

```python
# Remove specific key-value pair
user_dictionary.pop("age")

# Clear entire dictionary
user_dictionary.clear()

# Delete entire dictionary
del user_dictionary

```

### Looping Through Dictionaries

```python
# Loop through keys only
for x in user_dictionary:
    print(x)  # Prints: username, name, age

# Loop through keys and values
for x, y in user_dictionary.items():
    print(x, y)  # Prints: username coding with Ruby, etc.

```

### Important: Copying Dictionaries

**Wrong way:**

```python
user_dictionary2 = user_dictionary  # This creates a reference, not a copy!

```

**Correct way:**

```python
user_dictionary2 = user_dictionary.copy()  # This creates an actual copy

```

---

## 2. Functions in Python

### What is a Function?

- A function is a block of code that runs only when called
- Helps organize code and avoid repetition
- Uses the keyword `def` to define

### Basic Function Structure

```python
def function_name(parameters):
    # code to execute
    return value  # optional

```

**ASCII Visualization:**

```
Function Structure:
┌─────────────────────────────────┐
│ def my_function(parameter):     │
│     # code here                 │
│     return result               │
└─────────────────────────────────┘
          ↓ (when called)
┌─────────────────────────────────┐
│ my_function("input")            │
└─────────────────────────────────┘

```

### Function Examples

### Simple Function (No Parameters)

```python
def my_function():
    print("Inside my function")

# Call the function
my_function()

```

### Function with Parameters

```python
def print_my_name(name):
    print(f"Hello {name}")

# Call with parameter
print_my_name("Devaza")  # Output: Hello Devaza

```

### Function with Multiple Parameters

```python
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

# Call with multiple parameters
print_my_name("Steve", "Jobs")  # Output: Hello Steve Jobs

# Or use named parameters (order doesn't matter)
print_my_name(last_name="Jobs", first_name="Steve")

```

### Function that Returns Values

```python
def multiply_numbers(a, b):
    return a * b

# Store the result
solution = multiply_numbers(10, 6)
print(solution)  # Output: 60

```

### Variable Scope

### Global vs Local Variables

```python
color = "blue"  # Global variable (accessible everywhere)

def print_color_red():
    color = "red"  # Local variable (only accessible inside function)
    print(color)

print(color)        # Output: blue (global)
print_color_red()   # Output: red (local)

```

**ASCII Visualization:**

```
Variable Scope:
┌─────────────────────────────────┐
│ Global Scope                    │
│ color = "blue"                  │
│                                 │
│ ┌─────────────────────────────┐ │
│ │ Function Scope              │ │
│ │ color = "red"               │ │
│ │ (only accessible here)      │ │
│ └─────────────────────────────┘ │
└─────────────────────────────────┘

```

### Functions Calling Other Functions

```python
def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

# Usage
final_cost = buy_item(50)
print(final_cost)  # Output: 51.5

```

---

## 3. Practice Assignment Solutions

### Dictionary Assignment

**Task:** Work with a vehicle dictionary

```python
# Create the dictionary
my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

# Print all keys and values
for key, value in my_vehicle.items():
    print(key, value)

# Create a copy
vehicle_2 = my_vehicle.copy()

# Add new key-value pair
vehicle_2["number_of_tires"] = 4

# Remove mileage
vehicle_2.pop("mileage")

# Print only keys
for key in vehicle_2:
    print(key)

```

### Function Assignment

**Task:** Create a function that returns a user dictionary

```python
def user_dictionary(first_name, last_name, age):
    created_user_dictionary = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age
    }
    return created_user_dictionary

# Usage
solution_dictionary = user_dictionary("Devaza", "Robi", 32)
print(solution_dictionary)
# Output: {'first_name': 'Devaza', 'last_name': 'Robi', 'age': 32}

```

---

## Key Takeaways

1. **Dictionaries** store data as key-value pairs using `{}`
2. **Always use `.copy()`** when copying dictionaries to avoid reference issues
3. **Functions** help organize code using `def` keyword
4. **Parameters** allow functions to accept input data
5. **Return statements** send data back from functions
6. **Scope** determines where variables can be accessed (global vs local)
7. **Functions can call other functions** for complex operations

---

---

---

# Section 7

# Object-Oriented Programming (OOP) in Python - Complete Guide

## What is Object-Oriented Programming?

**OOP** is a programming paradigm based on the concept of **objects** which contain data and code.

**Benefits:**

- Scalability
- Efficiency
- Reusability

## Understanding Objects

Objects exist everywhere in real life - trees, houses, dogs. In programming, we can create these objects in code.

**Two ways to define objects:**

1. **By Behavior** - What the object does (bark, eat, sleep)
2. **By State** - What the object is (4 legs, 2 ears, golden color)

### ASCII Representation - Object Structure

```
    OBJECT
    ┌─────────────┐
    │   STATE     │  ← What it IS
    │  (4 legs,   │
    │   2 ears)   │
    ├─────────────┤
    │  BEHAVIOR   │  ← What it DOES
    │  (bark,     │
    │   eat)      │
    └─────────────┘

```

## Creating Classes and Objects

### Basic Class Structure

```python
# dog.py
class Dog:
    legs = 4
    ears = 2
    type = "goldendoodle"
    age = 5
    color = "yellow"

```

### Using the Class

```python
# main.py
from dog import *

dog = Dog()
print(dog.legs)  # Output: 4
print(dog.ears)  # Output: 2

```

## The Four Pillars of OOP

```
    OOP PILLARS
    ┌──────────────────┐
    │   ABSTRACTION    │
    ├──────────────────┤
    │  ENCAPSULATION   │
    ├──────────────────┤
    │   INHERITANCE    │
    ├──────────────────┤
    │  POLYMORPHISM    │
    └──────────────────┘

```

## 1. Abstraction

**Definition:** Hide implementation details and show only necessary features to the user.

**Example:** A flashlight - you know the on/off switch works, but don't need to know how the light bulb turns on.

### Implementation

```python
# enemy.py
class Enemy:
    type_of_enemy = ""
    health_points = 10
    attack_damage = 1

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage")

```

```python
# main.py
from enemy import *

zombie = Enemy()
zombie.type_of_enemy = "zombie"
zombie.talk()        # Simple interface
zombie.walk_forward() # User doesn't need to know implementation
zombie.attack()

```

## 2. Constructors

**Purpose:** Initialize objects with starting values when created.

### Types of Constructors:

### 1. Default/Empty Constructor

```python
def __init__(self):
    pass  # Python creates this automatically

```

### 2. No-Argument Constructor

```python
def __init__(self):
    print("New enemy created with no starting values")

```

### 3. Parameterized Constructor

```python
class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

```

**Usage:**

```python
zombie = Enemy("zombie", 15, 3)  # Custom values
ogre = Enemy("ogre")             # Default health/attack

```

## 3. Encapsulation

**Definition:** Bundle data and restrict direct access to some object components.

### Making Attributes Private

```python
class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy  # Private (double underscore)
        self.health_points = health_points     # Public
        self.attack_damage = attack_damage     # Public

    # Getter method
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    # No setter = cannot change type after creation

```

**Usage:**

```python
zombie = Enemy("zombie", 10, 1)
print(zombie.get_type_of_enemy())  # ✓ Works
# zombie.__type_of_enemy = "ogre"  # ✗ Error - cannot access private

```

### ASCII - Encapsulation Concept

```
    PUBLIC INTERFACE
    ┌─────────────────┐
    │ get_type()      │ ← Accessible
    │ talk()          │ ← Accessible
    ├─────────────────┤
    │ __type_of_enemy │ ← Hidden/Private
    │ internal_data   │ ← Hidden/Private
    └─────────────────┘

```

## 4. Inheritance

**Definition:** Process of acquiring properties from a parent class to child classes.

### Class Hierarchy

```
        Enemy (Parent)
        ┌─────────────┐
        │ health_pts  │
        │ attack_dmg  │
        │ talk()      │
        │ attack()    │
        └─────────────┘
              │
        ┌─────┴─────┐
        │           │
     Zombie      Ogre
   (Child)     (Child)

```

### Implementation

### Parent Class (Enemy)

```python
# enemy.py
class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("Enemy has no special attack")

```

### Child Class (Zombie)

```python
# zombie.py
from enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points=10, attack_damage=1):
        super().__init__("zombie", health_points, attack_damage)

    # Method Overriding
    def talk(self):
        print("*grumbling*")

    # New method unique to Zombie
    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50  # 50% chance
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP")

```

### Child Class (Ogre)

```python
# ogre.py
from enemy import *
import random

class Ogre(Enemy):
    def __init__(self, health_points=20, attack_damage=3):
        super().__init__("ogre", health_points, attack_damage)

    # Method Overriding
    def talk(self):
        print("Ogre is slamming hands all around")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20  # 20% chance
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and increases attack by 4")

```

### Self vs Super

- **`self`**: Refers to the current object being created
- **`super()`**: Refers to the parent class

```python
class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)  # Call parent constructor
        self.degree = degree         # Set child-specific property

```

## 5. Polymorphism

**Definition:** Objects can have multiple shapes - same interface, different implementations.

```python
# main.py
def battle(enemy):  # Takes any Enemy type
    enemy.talk()    # Will use the specific implementation
    enemy.attack()

zombie = Zombie(10, 1)
ogre = Ogre(20, 3)

battle(zombie)  # Uses Zombie's talk() method
battle(ogre)    # Uses Ogre's talk() method

```

## Complete Battle System Implementation

### Main Battle Function

```python
# main.py
from zombie import *
from ogre import *
import random

def battle(e1, e2):
    print(f"{e1.get_type_of_enemy().title()} vs {e2.get_type_of_enemy().title()}")
    e1.talk()
    e2.talk()
    print("-" * 40)

    while e1.health_points > 0 and e2.health_points > 0:
        # Special attacks
        e1.special_attack()
        e2.special_attack()

        # Show current health
        print(f"{e1.get_type_of_enemy()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemy()}: {e2.health_points} HP left")

        # Combat round
        e2.attack()
        e1.health_points -= e2.attack_damage

        if e1.health_points > 0:
            e1.attack()
            e2.health_points -= e1.attack_damage

        print("-" * 20)

    # Determine winner
    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemy().title()} wins!")
    else:
        print(f"{e2.get_type_of_enemy().title()} wins!")

# Create fighters and battle
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
battle(zombie, ogre)

```

## Composition - Hero and Weapon System

**Composition:** "Has-a" relationship (Hero HAS a Weapon)

### Weapon Class

```python
# weapon.py
class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase

```

### Hero Class

```python
# hero.py
from weapon import *

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon = None  # Composition - Hero HAS a weapon

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            print(f"Hero equipped {self.weapon.weapon_type}")

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")

```

### Hero Battle System

```python
# Complete hero vs enemy battle
def hero_battle(hero, enemy):
    print(f"Hero vs {enemy.get_type_of_enemy().title()}")
    enemy.talk()
    print("-" * 40)

    while hero.health_points > 0 and enemy.health_points > 0:
        # Enemy special attack
        enemy.special_attack()

        # Show health
        print(f"Hero: {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemy()}: {enemy.health_points} HP left")

        # Combat
        enemy.attack()
        hero.health_points -= enemy.attack_damage

        if hero.health_points > 0:
            hero.attack()
            enemy.health_points -= hero.attack_damage

        print("-" * 20)

    if hero.health_points > 0:
        print("Hero wins!")
    else:
        print(f"{enemy.get_type_of_enemy().title()} wins!")

# Usage
hero = Hero(10, 1)
sword = Weapon("sword", 5)
hero.weapon = sword
hero.equip_weapon()

zombie = Zombie(10, 1)
hero_battle(hero, zombie)

```

## Key Concepts Summary

### Class vs Object

- **Class**: Blueprint/template (like a cookie cutter)
- **Object**: Instance of a class (like the actual cookie)

### Method Overriding

When a child class provides its own implementation of a parent method.

### Composition vs Inheritance

- **Inheritance**: "Is-a" relationship (Zombie IS an Enemy)
- **Composition**: "Has-a" relationship (Hero HAS a Weapon)

This complete OOP implementation demonstrates all four pillars working together in a practical battle arena game system.I've created comprehensive notes on Object-Oriented Programming in Python based on the transcript, with all references changed from "Eric" to "Devaza" as requested. The notes include:

## Key Features:

**Clear Structure:**

- Organized with headings and bullet points
- Removed repetition and filler words
- Added ASCII diagrams for visual understanding

**Complete Code Implementation:**

- All four OOP pillars demonstrated
- Full battle arena system
- Hero and weapon composition example
- Working battle functions

**Technical Explanations:**

- Simple definitions for complex concepts
- Step-by-step implementation guides
- Practical examples throughout

The complete code artifact includes:

- Enemy parent class with encapsulation
- Zombie and Ogre child classes showing inheritance
- Hero and Weapon classes demonstrating composition
- Battle system showcasing polymorphism
- Full demonstration of all OOP concepts

The code is functional and demonstrates real-world application of OOP principles through an engaging battle arena game system, all credited to Devaza's teaching approach.

## Complete Code

```cpp
# enemy.py
class Enemy:
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy  # Private attribute (encapsulation)
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")

    def special_attack(self):
        print("Enemy has no special attack")

# zombie.py
from enemy import *
import random

class Zombie(Enemy):  # Inheritance
    def __init__(self, health_points=10, attack_damage=1):
        super().__init__("zombie", health_points, attack_damage)  # Call parent constructor

    # Method Overriding
    def talk(self):
        print("*grumbling*")

    # Zombie-specific method
    def spread_disease(self):
        print("The zombie is trying to spread infection")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50  # 50% chance
        if did_special_attack_work:
            self.health_points += 2
            print("Zombie regenerated 2 HP")

# ogre.py
from enemy import *
import random

class Ogre(Enemy):  # Inheritance
    def __init__(self, health_points=20, attack_damage=3):
        super().__init__("ogre", health_points, attack_damage)

    # Method Overriding
    def talk(self):
        print("Ogre is slamming hands all around")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20  # 20% chance
        if did_special_attack_work:
            self.attack_damage += 4
            print("Ogre gets angry and increases attack by 4")

# weapon.py
class Weapon:
    def __init__(self, weapon_type, attack_increase):
        self.weapon_type = weapon_type
        self.attack_increase = attack_increase

# hero.py
from weapon import *

class Hero:
    def __init__(self, health_points, attack_damage):
        self.health_points = health_points
        self.attack_damage = attack_damage
        self.is_weapon_equipped = False
        self.weapon = None  # Composition - Hero HAS a weapon

    def equip_weapon(self):
        if self.weapon is not None and not self.is_weapon_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_equipped = True
            print(f"Hero equipped {self.weapon.weapon_type}!")

    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")

# main.py - Complete Battle Arena System
from zombie import *
from ogre import *
from hero import *
from weapon import *

def battle(e1, e2):
    """Battle between two enemies - demonstrates Polymorphism"""
    print(f"\n=== {e1.get_type_of_enemy().upper()} VS {e2.get_type_of_enemy().upper()} ===")
    e1.talk()
    e2.talk()
    print("-" * 50)

    round_num = 1
    while e1.health_points > 0 and e2.health_points > 0:
        print(f"\n--- Round {round_num} ---")

        # Special attacks
        e1.special_attack()
        e2.special_attack()

        # Show current health
        print(f"{e1.get_type_of_enemy().title()}: {e1.health_points} HP")
        print(f"{e2.get_type_of_enemy().title()}: {e2.health_points} HP")

        # Combat round
        print("\nCombat:")
        e2.attack()
        e1.health_points -= e2.attack_damage

        if e1.health_points > 0:
            e1.attack()
            e2.health_points -= e1.attack_damage

        round_num += 1
        print("-" * 30)

    # Determine winner
    print("\n" + "=" * 50)
    if e1.health_points > 0:
        print(f"🏆 {e1.get_type_of_enemy().upper()} WINS! 🏆")
    else:
        print(f"🏆 {e2.get_type_of_enemy().upper()} WINS! 🏆")
    print("=" * 50)

def hero_battle(hero, enemy):
    """Battle between hero and enemy"""
    print(f"\n=== HERO VS {enemy.get_type_of_enemy().upper()} ===")
    enemy.talk()
    print("-" * 50)

    round_num = 1
    while hero.health_points > 0 and enemy.health_points > 0:
        print(f"\n--- Round {round_num} ---")

        # Enemy special attack
        enemy.special_attack()

        # Show health
        print(f"Hero: {hero.health_points} HP")
        print(f"{enemy.get_type_of_enemy().title()}: {enemy.health_points} HP")

        # Combat
        print("\nCombat:")
        enemy.attack()
        hero.health_points -= enemy.attack_damage

        if hero.health_points > 0:
            hero.attack()
            enemy.health_points -= hero.attack_damage

        round_num += 1
        print("-" * 30)

    # Determine winner
    print("\n" + "=" * 50)
    if hero.health_points > 0:
        print("🏆 HERO WINS! 🏆")
    else:
        print(f"🏆 {enemy.get_type_of_enemy().upper()} WINS! 🏆")
    print("=" * 50)

def demonstrate_oop_concepts():
    """Demonstrate all four pillars of OOP"""
    print("=" * 60)
    print("    OBJECT-ORIENTED PROGRAMMING BATTLE ARENA")
    print("         Created by Devaza")
    print("=" * 60)

    # ABSTRACTION - Simple interfaces hiding complex implementation
    print("\n1. ABSTRACTION DEMO:")
    zombie = Zombie(12, 2)
    zombie.talk()      # Simple interface
    zombie.attack()    # User doesn't see internal complexity

    # ENCAPSULATION - Data protection
    print("\n2. ENCAPSULATION DEMO:")
    print(f"Zombie type: {zombie.get_type_of_enemy()}")  # Accessing private data safely
    # zombie.__type_of_enemy = "ogre"  # This would cause an error!

    # INHERITANCE - Code reuse and specialization
    print("\n3. INHERITANCE DEMO:")
    ogre = Ogre(25, 4)
    zombie.spread_disease()  # Zombie-specific method
    ogre.talk()              # Overridden method

    # POLYMORPHISM - Same interface, different behavior
    print("\n4. POLYMORPHISM DEMO:")
    def make_enemy_talk(enemy):  # Works with any Enemy type
        enemy.talk()

    make_enemy_talk(zombie)  # Uses Zombie's talk()
    make_enemy_talk(ogre)    # Uses Ogre's talk()

    # COMPOSITION - Hero has a weapon
    print("\n5. COMPOSITION DEMO:")
    hero = Hero(15, 2)
    sword = Weapon("Excalibur", 6)
    hero.weapon = sword
    hero.equip_weapon()
    hero.attack()

    return zombie, ogre, hero

# Run the complete demonstration
if __name__ == "__main__":
    # Demonstrate OOP concepts
    zombie, ogre, hero = demonstrate_oop_concepts()

    # Battle 1: Enemy vs Enemy
    print("\n\n" + "🗡️ " * 20)
    battle(zombie, ogre)

    # Battle 2: Hero vs Enemy (create fresh enemies for fair fight)
    print("\n\n" + "⚔️ " * 20)
    fresh_zombie = Zombie(10, 1)
    hero_battle(hero, fresh_zombie)

    print("\n\n" + "=" * 60)
    print("Thanks for exploring OOP with Devaza's Battle Arena!")
    print("You've seen all four pillars in action:")
    print("✅ Abstraction - Simple interfaces")
    print("✅ Encapsulation - Data protection")
    print("✅ Inheritance - Code reuse")
    print("✅ Polymorphism - Multiple forms")
    print("✅ Composition - Object relationships")
    print("=" * 60)
```
