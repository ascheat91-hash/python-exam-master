import json

# Load existing paper 1 and paper 2
with open("data/model-papers.json", "r", encoding="utf-8") as f:
    existing_papers = json.load(f)

paper1 = existing_papers[0]
paper2 = existing_papers[1]

# Build completely unique Model Paper 3
paper3 = {
    "id": "model-3",
    "title": "MODEL PAPER 3",
    "subtitle": "College Examination Practice Paper - Pattern Standard",
    "course": "Python Programming (BSC/BA/CSE/MD/5/DSC/301) - Semester V",
    "maxMarks": 35,
    "timeMinutes": 180,
    "instructions": [
        "Question 1 is COMPULSORY (7 Marks) containing 7 objective/short questions of 1 mark each.",
        "Answer ANY ONE question from UNIT-I (Question 2 OR Question 3) - 14 Marks.",
        "Answer ANY ONE question from UNIT-II (Question 4 OR Question 5) - 14 Marks.",
        "Total Marks: 35 | Examination Duration: 3 Hours (180 Minutes)."
    ],
    "q1": {
        "title": "QUESTION 1 (COMPULSORY) — 7 MARKS (1 Mark each)",
        "questions": [
            {
                "subId": "q1-1",
                "question": "Which of the following is an invalid variable name in Python?\n(A) my_var\n(B) _myvar\n(C) 123var\n(D) var123",
                "type": "objective",
                "options": ["my_var", "_myvar", "123var", "var123"],
                "modelAnswer": "(C) 123var. Identifiers cannot begin with numeric digits.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-2",
                "question": "What will be the output of: print(type(3 + 4.5j))?",
                "type": "short",
                "modelAnswer": "<class 'complex'>",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-3",
                "question": "What is the result of the expression: 19 % 4?",
                "type": "short",
                "modelAnswer": "3 (Remainder when 19 is divided by 4).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-4",
                "question": "State the difference between '==' and 'is' operators.",
                "type": "short",
                "modelAnswer": "'==' checks for equality of values; 'is' checks for equality of object memory address/identity.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-5",
                "question": "What is the output of: range(1, 10, 3) when converted to a list?",
                "type": "short",
                "modelAnswer": "[1, 4, 7] (Starts at 1, steps by 3, stops before 10).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-6",
                "question": "Which list method is used to insert an element at a specified index?",
                "type": "short",
                "modelAnswer": "insert() method (e.g., list.insert(index, element)).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-7",
                "question": "What does a 'continue' statement do when executed inside a loop?",
                "type": "short",
                "modelAnswer": "It skips the remaining statements of the current iteration and jumps to the next cycle.",
                "marking": "1 Mark."
            }
        ]
    },
    "unit1": {
        "title": "UNIT - I (Attempt ANY ONE: Question 2 OR Question 3 — 14 Marks)",
        "q2": {
            "title": "Question 2 (14 Marks)",
            "parts": [
                {
                    "part": "2(a)",
                    "marks": 7,
                    "question": "Explain Implicit Declaration and Dynamic Typing in Python with suitable program examples and contrast with statically typed languages like C.",
                    "modelAnswer": "1. Definition & Core Concept (2 Marks):\n- In Python, variable types do NOT need to be explicitly declared before use (no 'int x;' or 'float y;'). This is known as Implicit Declaration.\n- Dynamic Typing: A variable is not bound to a fixed data type; its type is inferred at runtime and can change dynamically whenever a value of another type is assigned.\n\n2. Comparison Table with C/Java (2 Marks):\n- C/Java (Static Typing): Type is fixed at compile-time (e.g., int a = 10; a = 'hi'; causes compile error).\n- Python (Dynamic Typing): Type is checked at runtime (e.g., x = 10; x = 'hi' is valid).\n\n3. Python Program Example & type() Demonstration (3 Marks):\n```python\n# Implicit declaration and dynamic re-typing\nval = 100\nprint(\"Value:\", val, \"| Type:\", type(val))  # <class 'int'>\n\nval = \"Examination\"\nprint(\"Value:\", val, \"| Type:\", type(val))  # <class 'str'>\n\nval = 45.75\nprint(\"Value:\", val, \"| Type:\", type(val))  # <class 'float'>\n```\n- Explanation: The type() function reveals that the same variable 'val' references different data type objects in memory without any error."
                },
                {
                    "part": "2(b)",
                    "marks": 7,
                    "question": "Explain Boolean and String data types in Python. Discuss string indexing (positive and negative), slicing syntax, and why strings are immutable.",
                    "modelAnswer": "1. Boolean Data Type (2 Marks):\n- bool represents truth values: True (numeric 1) or False (numeric 0).\n- Keywords True and False must be capitalized.\n- Result of comparison operations: 10 > 5 evaluates to True.\n\n2. String Indexing & Slicing (3 Marks):\n- Strings are ordered sequences of characters in quotes.\n- Positive indexing starts from 0 (left-to-right).\n- Negative indexing starts from -1 (right-to-left, -1 is last character).\n- Slicing: `str[start : stop : step]` where stop is exclusive (stop-1).\n- Example: `s = 'PYTHON'`; `s[1:4]` gives `'YTH'`; `s[::-1]` reverses string.\n\n3. String Immutability with Example (2 Marks):\n- Strings cannot be modified in-place once created.\n- `s = 'HELLO'; s[0] = 'M'` raises `TypeError: 'str' object does not support item assignment`.\n- Any modification creates a brand new string object in memory."
                }
            ]
        },
        "q3": {
            "title": "Question 3 (14 Marks)",
            "parts": [
                {
                    "part": "3(a)",
                    "marks": 7,
                    "question": "Explain all Arithmetic and Comparison/Relational Operators in Python with purpose, syntax, examples, and the difference between division (/) and floor division (//).",
                    "modelAnswer": "1. Arithmetic Operators (3 Marks):\n- + (Add), - (Subtract), * (Multiply).\n- / (Float Division): Always produces a float result: 14 / 4 = 3.5.\n- // (Floor Division): Discards the fractional part, rounding down to integer quotient: 14 // 4 = 3.\n- % (Modulus): Returns division remainder: 14 % 4 = 2.\n- ** (Exponentiation): Base raised to power: 2 ** 4 = 16.\n\n2. Comparison / Relational Operators (2 Marks):\n- ==, !=, >, <, >=, <=.\n- Always return Boolean (True or False).\n- Difference: '=' is assignment; '==' is relational comparison.\n\n3. Code Example & Verification (2 Marks):\n```python\na, b = 15, 4\nprint(\"Float Div (/):\", a / b)   # 3.75\nprint(\"Floor Div (//):\", a // b) # 3\nprint(\"Modulus (%):\", a % b)     # 3\nprint(\"Equality (==):\", a == b)  # False\n```"
                },
                {
                    "part": "3(b)",
                    "marks": 7,
                    "question": "What is Operator Precedence and Associativity? Provide a comprehensive hierarchy table and step-by-step evaluation for the expression: 20 - 4 * 2 ** 3 // 2 + 5.",
                    "modelAnswer": "1. Definitions (2 Marks):\n- Operator Precedence determines which operations are evaluated first in compound expressions.\n- Associativity determines the direction (Left-to-Right or Right-to-Left) of evaluation when operators share equal priority.\n\n2. Precedence Hierarchy Table (2 Marks):\n- 1. () Parentheses (Highest)\n- 2. ** Exponentiation (Right-to-Left)\n- 3. *, /, //, % (Left-to-Right)\n- 4. +, - (Left-to-Right)\n- 5. ==, !=, >, < (Comparisons)\n- 6. not, and, or (Logical)\n- 7. =, +=, -= (Assignment - Lowest)\n\n3. Step-by-Step Expression Evaluation (3 Marks):\nExpression: 20 - 4 * 2 ** 3 // 2 + 5\n- Step 1: 2 ** 3 = 8 (Power has highest precedence) -> 20 - 4 * 8 // 2 + 5\n- Step 2: 4 * 8 = 32 (Multiplication evaluated L-to-R) -> 20 - 32 // 2 + 5\n- Step 3: 32 // 2 = 16 (Floor division) -> 20 - 16 + 5\n- Step 4: 20 - 16 = 4 (Subtraction evaluated L-to-R) -> 4 + 5\n- Step 5: 4 + 5 = 9 (Addition)\nFinal Output = 9."
                }
            ]
        }
    },
    "unit2": {
        "title": "UNIT - II (Attempt ANY ONE: Question 4 OR Question 5 — 14 Marks)",
        "q4": {
            "title": "Question 4 (14 Marks)",
            "parts": [
                {
                    "part": "4(a)",
                    "marks": 7,
                    "question": "Explain Nested if and if-elif-else statements in Python. Write a complete Python program to find the largest among three distinct numbers with flowchart/algorithm.",
                    "modelAnswer": "1. Concepts & Indentation (2 Marks):\n- Nested if: An if statement placed inside another if or else statement to check multi-level dependent conditions.\n- if-elif-else: Multi-way sequential branching construct. Executes the first matching condition and bypasses the rest.\n\n2. Algorithm to Find Largest of Three (2 Marks):\n- Read three numbers: a, b, c.\n- If a >= b and a >= c: largest is a.\n- Elif b >= a and b >= c: largest is b.\n- Else: largest is c.\n\n3. Complete Python Program (3 Marks):\n```python\na = float(input(\"Enter first number: \"))\nb = float(input(\"Enter second number: \"))\nc = float(input(\"Enter third number: \"))\n\nif (a >= b) and (a >= c):\n    largest = a\nelif (b >= a) and (b >= c):\n    largest = b\nelse:\n    largest = c\n\nprint(\"Largest number is:\", largest)\n```\n- Demonstrates multi-way branching and logical 'and' conjunction."
                },
                {
                    "part": "4(b)",
                    "marks": 7,
                    "question": "What is the while loop? Explain entry-controlled iteration, components of a loop, and write a program to calculate the sum of digits of an entered number with dry-run table.",
                    "modelAnswer": "1. while Loop Definition & Components (2 Marks):\n- Entry-controlled loop that repeats statements while its condition remains True.\n- Three components: Initialization (counter = 1), Condition (while counter <= N:), and Increment/Update (counter += 1).\n\n2. Program to Calculate Sum of Digits (3 Marks):\n```python\nnum = int(input(\"Enter integer: \"))\noriginal = num\ndigit_sum = 0\n\nwhile num > 0:\n    digit = num % 10       # Extract last digit\n    digit_sum += digit     # Add to sum\n    num = num // 10        # Remove last digit\n\nprint(f\"Sum of digits of {original} is: {digit_sum}\")\n```\n\n3. Dry Run Table for input 245 (2 Marks):\n| Step | num | digit (num%10) | digit_sum | num (num//10) |\n| 1    | 245 | 5              | 5         | 24            |\n| 2    | 24  | 4              | 9         | 2             |\n| 3    | 2   | 2              | 11        | 0             |\nLoop terminates. Output = 11."
                }
            ]
        },
        "q5": {
            "title": "Question 5 (14 Marks)",
            "parts": [
                {
                    "part": "5(a)",
                    "marks": 7,
                    "question": "Explain Deletion mechanisms in Python lists: del statement, pop(), remove(), and clear() with syntax, differences, and exceptions raised.",
                    "modelAnswer": "1. Comparison of 4 Deletion Techniques (3 Marks):\n- del statement: Keyword statement deleting by index or slice (e.g., del L[0] or del L[1:3]). Does NOT return any value.\n- pop([index]): Method removing and returning the element at specified index. If index omitted, removes and returns last element. Raises IndexError on empty list.\n- remove(value): Method removing the first matching element by VALUE. Raises ValueError if element is not in list.\n- clear(): Removes all elements, leaving an empty list [].\n\n2. Code Demonstration (4 Marks):\n```python\nnums = [10, 20, 30, 40, 50, 60]\ndel nums[0]         # [20, 30, 40, 50, 60]\npopped = nums.pop() # removes 60, nums=[20, 30, 40, 50]\nnums.remove(30)     # removes value 30, nums=[20, 40, 50]\nnums.clear()        # nums=[]\nprint(\"Popped item:\", popped, \"| Final:\", nums)\n```"
                },
                {
                    "part": "5(b)",
                    "marks": 7,
                    "question": "Explain how 1D arrays are implemented using lists in Python. Write a complete Python program to perform Traversal, Insertion, and Linear Search.",
                    "modelAnswer": "1. Array Concept in Python (2 Marks):\n- Python lacks a primitive fixed array type in syntax, so lists of homogeneous elements are used to implement 1D and 2D arrays.\n- Provides contiguous zero-based indexing and O(1) access time.\n\n2. Complete Array Implementation Code (5 Marks):\n```python\n# 1D Array Implementation via List\narr = [10, 20, 30, 40, 50]\n\n# 1. Traversal\nprint(\"Array Traversal:\")\nfor i in range(len(arr)):\n    print(f\"Index {i}: {arr[i]}\")\n\n# 2. Insertion\narr.insert(2, 25) # Inserts 25 at index 2\nprint(\"After Insertion:\", arr)\n\n# 3. Linear Search\ntarget = 40\nfound_pos = -1\nfor i in range(len(arr)):\n    if arr[i] == target:\n        found_pos = i\n        break\n\nif found_pos != -1:\n    print(f\"Element {target} found at index {found_pos}\")\nelse:\n    print(\"Element not found\")\n```"
                }
            ]
        }
    }
}

# Build completely unique Model Paper 4
paper4 = {
    "id": "model-4",
    "title": "MODEL PAPER 4",
    "subtitle": "College Examination Practice Paper - Pattern Standard",
    "course": "Python Programming (BSC/BA/CSE/MD/5/DSC/301) - Semester V",
    "maxMarks": 35,
    "timeMinutes": 180,
    "instructions": [
        "Question 1 is COMPULSORY (7 Marks) containing 7 objective/short questions of 1 mark each.",
        "Answer ANY ONE question from UNIT-I (Question 2 OR Question 3) - 14 Marks.",
        "Answer ANY ONE question from UNIT-II (Question 4 OR Question 5) - 14 Marks.",
        "Total Marks: 35 | Examination Duration: 3 Hours (180 Minutes)."
    ],
    "q1": {
        "title": "QUESTION 1 (COMPULSORY) — 7 MARKS (1 Mark each)",
        "questions": [
            {
                "subId": "q1-1",
                "question": "Which function is used to take input from the keyboard in Python?",
                "type": "short",
                "modelAnswer": "input() function.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-2",
                "question": "What is the numeric value of Boolean True and False in arithmetic expressions?",
                "type": "short",
                "modelAnswer": "True = 1, False = 0.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-3",
                "question": "What will be the output of: print(2 ** 2 ** 3)?",
                "type": "short",
                "modelAnswer": "256 (Right-to-left associativity: 2 ** 3 = 8, then 2 ** 8 = 256).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-4",
                "question": "What punctuation mark must follow an 'if', 'else', or 'while' statement header?",
                "type": "short",
                "modelAnswer": "Colon (:).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-5",
                "question": "What values are generated by range(5)?",
                "type": "short",
                "modelAnswer": "0, 1, 2, 3, 4.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-6",
                "question": "What will be the output of: len([1, [2, 3], 4])?",
                "type": "short",
                "modelAnswer": "3 (The nested list [2, 3] counts as one single element).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-7",
                "question": "Which statement terminates a loop immediately?",
                "type": "short",
                "modelAnswer": "break statement.",
                "marking": "1 Mark."
            }
        ]
    },
    "unit1": {
        "title": "UNIT - I (Attempt ANY ONE: Question 2 OR Question 3 — 14 Marks)",
        "q2": {
            "title": "Question 2 (14 Marks)",
            "parts": [
                {
                    "part": "2(a)",
                    "marks": 7,
                    "question": "Explain Keywords and Identifiers in Python. List any 6 common keywords and explain the 4 rules for naming valid identifiers with examples.",
                    "modelAnswer": "1. Definitions (2 Marks):\n- Keywords: Predefined reserved words with fixed syntactical roles (e.g., if, elif, else, while, for, def, return, True, False, None).\n- Identifiers: Custom programmer-defined names for variables, functions, and objects.\n\n2. Four Identifier Rules (3 Marks):\n- 1. Characters: Letters (a-z, A-Z), digits (0-9), underscore (_).\n- 2. Starting Character: Must start with a letter or underscore (_). Cannot start with a digit (e.g. 1st is illegal).\n- 3. No Special Characters: Spaces, hyphens, and symbols (@, $, %) are strictly prohibited.\n- 4. No Keywords: Cannot use reserved words like 'while' as identifiers.\n\n3. Examples (2 Marks):\n- Valid: `student_name`, `_roll_no`, `score100`, `totalMarks`.\n- Invalid: `100score`, `student-name`, `my marks`, `for`."
                },
                {
                    "part": "2(b)",
                    "marks": 7,
                    "question": "Explain Number data types in Python: int, float, and complex. Show how .real and .imag attributes work and how user input is converted using int() and float().",
                    "modelAnswer": "1. Numeric Types (2 Marks):\n- int: Arbitrarily large whole numbers (e.g., 50, -1000).\n- float: Floating point numbers with decimal points (e.g., 3.14159).\n- complex: Represented as a + bj. Uses 'j' or 'J' as the imaginary unit.\n\n2. Complex Number Attributes (2 Marks):\n```python\nz = 4 + 7j\nprint(\"Real Part:\", z.real)       # 4.0\nprint(\"Imaginary Part:\", z.imag)  # 7.0\n```\n- Both attributes return float values.\n\n3. Reading and Typecasting Numeric Input (3 Marks):\n- input() returns a string; without typecasting, mathematical addition causes concatenation.\n- Syntax: `age = int(input(\"Enter age: \"))`; `cgpa = float(input(\"Enter CGPA: \"))`."
                }
            ]
        },
        "q3": {
            "title": "Question 3 (14 Marks)",
            "parts": [
                {
                    "part": "3(a)",
                    "marks": 7,
                    "question": "Explain Increment/Assignment Operators and Compound Assignment Operators in Python. Discuss why Python does not support '++' or '--' operators.",
                    "modelAnswer": "1. Simple & Compound Assignment (3 Marks):\n- Simple Assignment (=): Assigns right operand to left variable (x = 10).\n- Compound Assignment Operators combine arithmetic and assignment:\n  - `+=` (Add and assign: `x += 5` -> `x = x + 5`)\n  - `-=` (Subtract and assign: `x -= 2` -> `x = x - 2`)\n  - `*=` (Multiply and assign: `x *= 3` -> `x = x * 3`)\n  - `/=` (Divide and assign: `x /= 2` -> `x = x / 2`)\n  - `//=` (Floor divide and assign)\n  - `%=` (Modulus and assign)\n  - `**=` (Power and assign)\n\n2. Why Python Does Not Support '++' or '--' (4 Marks):\n- In Python, numeric objects like integers are IMMUTABLE. The expression `x = 10` binds `x` to an integer object 10.\n- In C, `x++` directly increments a mutable memory cell. In Python, modifying an integer requires binding the name to a brand-new integer object.\n- Furthermore, `+` is parsed as a unary sign in Python, so `++x` is parsed as `+(+x)`, returning positive `x` without modifying the variable! Therefore, `x += 1` is the standard Python approach."
                },
                {
                    "part": "3(b)",
                    "marks": 7,
                    "question": "Explain Logical Operators (and, or, not) and Identity Operators (is, is not) in Python with truth tables and code demonstrations.",
                    "modelAnswer": "1. Logical Operators & Truth Tables (3 Marks):\n- `and`: True only if both conditions are True.\n- `or`: True if at least one condition is True.\n- `not`: Inverts truth value.\n\n2. Identity Operators (2 Marks):\n- `is`: Evaluates to True if two variables refer to the exact same object in memory (`id(a) == id(b)`).\n- `is not`: True if they point to different memory locations.\n\n3. Code Demonstration (2 Marks):\n```python\nx = [1, 2]\ny = [1, 2]\nz = x\nprint(x == y)      # True (equal values)\nprint(x is y)      # False (distinct objects in memory)\nprint(x is z)      # True (refer to same object)\n```"
                }
            ]
        }
    },
    "unit2": {
        "title": "UNIT - II (Attempt ANY ONE: Question 4 OR Question 5 — 14 Marks)",
        "q4": {
            "title": "Question 4 (14 Marks)",
            "parts": [
                {
                    "part": "4(a)",
                    "marks": 7,
                    "question": "Explain the for loop and the range() function in Python. Discuss its 1-arg, 2-arg, and 3-arg forms, negative stepping, and loop iteration over strings and lists.",
                    "modelAnswer": "1. for Loop Sequence Traversal (2 Marks):\n- Python's for loop iterates over items of any sequence using the `in` keyword without requiring manual counter index manipulation.\n- Iterating over string: `for ch in \"EXAM\": print(ch)`.\n- Iterating over list: `for num in [10, 20, 30]: print(num)`.\n\n2. range() Function Variations (3 Marks):\n- 1-Arg: `range(stop)` -> `range(3)` produces 0, 1, 2.\n- 2-Arg: `range(start, stop)` -> `range(2, 6)` produces 2, 3, 4, 5.\n- 3-Arg: `range(start, stop, step)` -> `range(1, 8, 2)` produces 1, 3, 5, 7.\n- Negative Step: `range(5, 0, -1)` produces countdown 5, 4, 3, 2, 1.\n\n3. Essential Exam Rule (2 Marks):\n- The stop parameter is ALWAYS exclusive (stop - 1)."
                },
                {
                    "part": "4(b)",
                    "marks": 7,
                    "question": "What are Nested Loops in Python? Explain how outer and inner loops synchronize. Write a program to print a right-angled number triangle pattern with a dry-run table.",
                    "modelAnswer": "1. Concept of Nested Loops (2 Marks):\n- A loop inside the body of another loop. For every single cycle of the outer loop, the inner loop executes through all its iterations completely.\n\n2. Program Code (3 Marks):\n```python\nrows = 4\nfor i in range(1, rows + 1):\n    for j in range(1, i + 1):\n        print(j, end=\" \")\n    print()  # Moves to next line\n```\n\n3. Dry Run Table (2 Marks):\n| Outer (i) | Inner (j) | Output on Line |\n| 1         | 1         | 1              |\n| 2         | 1, 2      | 1 2            |\n| 3         | 1, 2, 3   | 1 2 3          |\n| 4         | 1, 2, 3, 4| 1 2 3 4        |\nTotal rows = 4."
                }
            ]
        },
        "q5": {
            "title": "Question 5 (14 Marks)",
            "parts": [
                {
                    "part": "5(a)",
                    "marks": 7,
                    "question": "What are Lists in Python? Explain list creation, positive & negative indexing, mutability, and built-in functions: len(), min(), max(), sum(), sorted().",
                    "modelAnswer": "1. List Characteristics (2 Marks):\n- Ordered, mutable, heterogeneous collection of items enclosed in square brackets [].\n- Positive index (0 to len-1); Negative index (-1 to -len).\n- Mutability: `L[0] = 99` alters list in-place without creating a new object.\n\n2. Built-in List Functions (3 Marks):\n- `len(L)`: Returns total count of items.\n- `min(L)`: Returns smallest element.\n- `max(L)`: Returns largest element.\n- `sum(L)`: Computes arithmetic total of numbers in list.\n- `sorted(L)`: Returns a new sorted list in ascending order without altering original list.\n\n3. Python Program Example (2 Marks):\n```python\nscores = [35, 75, 50, 90, 60]\nprint(\"Length:\", len(scores))     # 5\nprint(\"Min / Max:\", min(scores), max(scores)) # 35 90\nprint(\"Average:\", sum(scores) / len(scores))  # 62.0\nprint(\"Sorted:\", sorted(scores)) # [35, 50, 60, 75, 90]\n```"
                },
                {
                    "part": "5(b)",
                    "marks": 7,
                    "question": "Explain List Methods: append(), insert(), extend(), reverse(), count(), index(). Write a complete program demonstrating each method.",
                    "modelAnswer": "1. Method Definitions (3 Marks):\n- `append(item)`: Adds element at the end of list.\n- `insert(idx, item)`: Inserts element at specified index position.\n- `extend(iterable)`: Merges elements of another list into current list.\n- `reverse()`: Reverses list in-place (returns None).\n- `count(val)`: Returns frequency of val in list.\n- `index(val)`: Returns first zero-based index of val.\n\n2. Program Code & Output (4 Marks):\n```python\nitems = [\"Pen\", \"Book\", \"Pen\"]\nitems.append(\"Pencil\")        # ['Pen', 'Book', 'Pen', 'Pencil']\nitems.insert(1, \"Eraser\")     # ['Pen', 'Eraser', 'Book', 'Pen', 'Pencil']\nprint(\"Count:\", items.count(\"Pen\"))  # 2\nprint(\"Index:\", items.index(\"Pen\"))  # 0\nitems.extend([\"Scale\", \"Glue\"])\nitems.reverse()\nprint(\"Final List:\", items)\n```"
                }
            ]
        }
    }
}

# Build completely unique Model Paper 5
paper5 = {
    "id": "model-5",
    "title": "MODEL PAPER 5",
    "subtitle": "College Examination Practice Paper - Pattern Standard",
    "course": "Python Programming (BSC/BA/CSE/MD/5/DSC/301) - Semester V",
    "maxMarks": 35,
    "timeMinutes": 180,
    "instructions": [
        "Question 1 is COMPULSORY (7 Marks) containing 7 objective/short questions of 1 mark each.",
        "Answer ANY ONE question from UNIT-I (Question 2 OR Question 3) - 14 Marks.",
        "Answer ANY ONE question from UNIT-II (Question 4 OR Question 5) - 14 Marks.",
        "Total Marks: 35 | Examination Duration: 3 Hours (180 Minutes)."
    ],
    "q1": {
        "title": "QUESTION 1 (COMPULSORY) — 7 MARKS (1 Mark each)",
        "questions": [
            {
                "subId": "q1-1",
                "question": "Which of the following creates a multiline comment or docstring in Python?\n(A) /* ... */\n(B) // ... //\n(C) ''' ... '''\n(D) <!-- ... -->",
                "type": "objective",
                "options": ["/* ... */", "// ... //", "''' ... '''", "<!-- ... -->"],
                "modelAnswer": "(C) ''' ... '''. Triple quotes are used for multi-line comments and docstrings in Python.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-2",
                "question": "What is the return data type of the expression 10 / 2 in Python 3?",
                "type": "short",
                "modelAnswer": "float (evaluates to 5.0).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-3",
                "question": "What will be the output of: print(bool([]), bool([0]))?",
                "type": "short",
                "modelAnswer": "False True (Empty list evaluates to False; non-empty list [0] evaluates to True).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-4",
                "question": "Which statement acts as a syntactic placeholder that does nothing when executed?",
                "type": "short",
                "modelAnswer": "pass statement.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-5",
                "question": "What is the output of: 'COLLEGE'[1:5]?",
                "type": "short",
                "modelAnswer": "'OLLE' (Extracts indices 1, 2, 3, 4).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-6",
                "question": "What is the difference between list.remove(x) and list.pop()?",
                "type": "short",
                "modelAnswer": "remove(x) searches and deletes by value; pop() removes and returns by index.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-7",
                "question": "How can you reverse a Python list in a single slicing step?",
                "type": "short",
                "modelAnswer": "my_list[::-1]",
                "marking": "1 Mark."
            }
        ]
    },
    "unit1": {
        "title": "UNIT - I (Attempt ANY ONE: Question 2 OR Question 3 — 14 Marks)",
        "q2": {
            "title": "Question 2 (14 Marks)",
            "parts": [
                {
                    "part": "2(a)",
                    "marks": 7,
                    "question": "What are Comments in Python? Explain their purpose, single-line comments (#), inline comments, and multi-line comments/docstrings with syntax and examples.",
                    "modelAnswer": "1. Purpose of Comments (2 Marks):\n- Informative notes written in code for human understanding.\n- Ignored completely by interpreter during compilation/execution.\n- Essential for code documentation, team collaboration, and temporarily disabling lines during debugging.\n\n2. Single-line & Inline Comments (2 Marks):\n- Single-line: Begins with `#`. The interpreter ignores all text after `#` to the line's end.\n- Inline comment: Placed at the end of an executable statement: `rate = 7.5 # interest rate in percent`.\n\n3. Multi-line Comments & Triple Quotes (3 Marks):\n- Multi-line comments can use multiple `#` on consecutive lines or triple quotes (`'''` or `\"\"\"`).\n- When triple quotes are placed immediately after function/module definitions, they act as official docstrings accessible via `help()` or `.__doc__`:\n```python\n\"\"\"\nThis program calculates student pass percentage\nfor Semester V examinations.\n\"\"\"\nmarks = 45\nprint(\"Marks:\", marks)\n```"
                },
                {
                    "part": "2(b)",
                    "marks": 7,
                    "question": "What is a Variable in Python? Explain variable declaration, assignment, multiple assignments, naming restrictions, and reading numeric input with typecasting.",
                    "modelAnswer": "1. Variable Definition & Implicit Declaration (2 Marks):\n- Named memory location storing data. Python variables are created automatically upon value assignment without explicit data type declarations.\n- Multiple Assignment: `a = b = c = 100` or `x, y = 10, 20`.\n\n2. Variable Naming Restrictions (2 Marks):\n- Must begin with a letter or underscore (`_`).\n- Cannot begin with a number (e.g. `1val` is illegal).\n- No spaces or special symbols (`@`, `$`, `%`, `-`).\n- Cannot be a reserved keyword (e.g. `while = 5` is invalid).\n\n3. Reading User Input & Typecasting (3 Marks):\n```python\n# Reading user details for examination\nstudent_name = input(\"Enter Name: \")           # Reads string\nmaths = int(input(\"Enter Maths Marks: \"))     # Typecasts to int\nphysics = int(input(\"Enter Physics Marks: \")) # Typecasts to int\ntotal = maths + physics\nprint(f\"{student_name}'s Total Marks = {total}\")\n```"
                }
            ]
        },
        "q3": {
            "title": "Question 3 (14 Marks)",
            "parts": [
                {
                    "part": "3(a)",
                    "marks": 7,
                    "question": "Explain Identity Operators ('is' and 'is not') in Python and distinguish them from Equality Operator ('==') with memory diagrams and code examples.",
                    "modelAnswer": "1. Detailed Difference Table (3 Marks):\n- '==' (Equality): Checks whether the VALUES/contents of two objects are equal.\n- 'is' (Identity): Checks whether both variables point to the exact same memory location (`id(a) == id(b)`).\n- 'is not': Evaluates to True if variables point to different memory addresses.\n\n2. The id() Function (1 Mark):\n- Returns the unique integer memory address assigned to an object during its lifetime.\n\n3. Code Demonstration (3 Marks):\n```python\nlist1 = [1, 2, 3]\nlist2 = [1, 2, 3]\nlist3 = list1\n\nprint(\"list1 == list2:\", list1 == list2)     # True (identical content)\nprint(\"list1 is list2:\", list1 is list2)     # False (different memory addresses)\nprint(\"list1 is list3:\", list1 is list3)     # True (both point to same memory)\nprint(\"id(list1) == id(list3):\", id(list1) == id(list3)) # True\n```"
                },
                {
                    "part": "3(b)",
                    "marks": 7,
                    "question": "Write a complete Python program to read Principal amount, Rate of interest, and Time from the user and calculate Simple Interest and Total Amount. Explain all operators used.",
                    "modelAnswer": "1. Formula & Operator Analysis (2 Marks):\n- Formula: `SI = (P * R * T) / 100`, `Total = P + SI`.\n- Operators used: `*` (multiplication), `/` (float division), `+` (addition), `=` (assignment).\n\n2. Complete Python Program (3 Marks):\n```python\nP = float(input(\"Enter Principal amount: \"))\nR = float(input(\"Enter Rate of interest (%): \"))\nT = float(input(\"Enter Time period (years): \"))\n\n# Calculate Simple Interest\nSI = (P * R * T) / 100\ntotal_payable = P + SI\n\nprint(\"Simple Interest =\", SI)\nprint(\"Total Payable Amount =\", total_payable)\n```\n\n3. Dry Run Table (2 Marks):\n| Step | Variable State | Calculation | Result |\n| 1    | P=2000, R=5, T=2 | SI = (2000*5*2)/100 | SI = 200.0 |\n| 2    | P=2000, SI=200.0 | Total = 2000 + 200.0 | Total = 2200.0 |\nOutput: SI = 200.0, Total Payable = 2200.0"
                }
            ]
        }
    },
    "unit2": {
        "title": "UNIT - II (Attempt ANY ONE: Question 4 OR Question 5 — 14 Marks)",
        "q4": {
            "title": "Question 4 (14 Marks)",
            "parts": [
                {
                    "part": "4(a)",
                    "marks": 7,
                    "question": "Explain Branching Statements in Python loops: break, continue, and pass with syntax, differences, and practical code examples.",
                    "modelAnswer": "1. Definitions & Roles (3 Marks):\n- `break`: Immediately terminates the enclosing loop, transferring control to the statement directly following the loop.\n- `continue`: Abandons remaining statements of the current iteration and jumps directly to the next loop cycle.\n- `pass`: A null statement that serves as a syntactic placeholder where code is syntactically required but no action is needed.\n\n2. Differences Comparison (2 Marks):\n- break ends the entire loop permanently.\n- continue only skips the current iteration.\n- pass does nothing (NO-OP) and execution flows to next line.\n\n3. Code Example (2 Marks):\n```python\nprint(\"Testing break (stops at 3):\")\nfor i in range(1, 6):\n    if i == 3: break\n    print(i, end=\" \") # 1 2\n\nprint(\"\\nTesting continue (skips 3):\")\nfor i in range(1, 6):\n    if i == 3: continue\n    print(i, end=\" \") # 1 2 4 5\n```"
                },
                {
                    "part": "4(b)",
                    "marks": 7,
                    "question": "Write a complete Python program to find the Factorial of an entered positive integer using a for loop and range(). Provide algorithm, line-by-line explanation, and dry-run table.",
                    "modelAnswer": "1. Algorithm (2 Marks):\n- Read integer N.\n- If N < 0: report error. If N == 0: factorial is 1.\n- Else initialize `fact = 1`.\n- Loop `i` from 1 to N: `fact = fact * i`.\n- Output `fact`.\n\n2. Program Code (3 Marks):\n```python\nn = int(input(\"Enter positive integer: \"))\nif n < 0:\n    print(\"Factorial not defined for negative numbers\")\nelif n == 0:\n    print(\"Factorial of 0 is 1\")\nelse:\n    fact = 1\n    for i in range(1, n + 1):\n        fact *= i\n    print(f\"Factorial of {n} is: {fact}\")\n```\n\n3. Dry Run Table for N=4 (2 Marks):\n| Step | i | Calculation (fact *= i) | fact |\n| 1    | 1 | 1 * 1                   | 1    |\n| 2    | 2 | 1 * 2                   | 2    |\n| 3    | 3 | 2 * 3                   | 6    |\n| 4    | 4 | 6 * 4                   | 24   |\nFinal Output: Factorial of 4 is: 24."
                }
            ]
        },
        "q5": {
            "title": "Question 5 (14 Marks)",
            "parts": [
                {
                    "part": "5(a)",
                    "marks": 7,
                    "question": "Explain List Mutability and Slicing in Python. Contrast with String Immutability and show how elements can be updated, inserted, and sliced.",
                    "modelAnswer": "1. Mutability vs Immutability (3 Marks):\n- Mutable objects can have their contents altered in-place without changing their memory address (e.g. Lists).\n- Immutable objects cannot be altered once created (e.g. Strings, Tuples, Integers).\n- Example: `L = [1, 2]; L[0] = 99` succeeds; `s = 'hi'; s[0] = 'b'` raises TypeError.\n\n2. Slicing Syntax: `L[start : stop : step]` (2 Marks):\n- `nums = [10, 20, 30, 40, 50]`\n- `nums[1:4]` -> `[20, 30, 40]` (stop index 4 is excluded).\n- `nums[::-1]` -> `[50, 40, 30, 20, 10]` (reversal).\n\n3. Slice Assignment & Updating (2 Marks):\n```python\nletters = ['a', 'b', 'c', 'd']\nletters[1:3] = ['X', 'Y']\nprint(letters) # ['a', 'X', 'Y', 'd']\n```"
                },
                {
                    "part": "5(b)",
                    "marks": 7,
                    "question": "Explain the difference between append() and extend() methods in Python lists. Write a Python program to perform Linear Search on a list of numbers.",
                    "modelAnswer": "1. append() vs extend() Comparison (3 Marks):\n- `append(x)`: Adds `x` as a single object to the end of list. If `x` is a list, it becomes a nested element.\n- `extend(iterable)`: Iterates over the iterable and appends each element individually.\n- Example:\n```python\nL1 = [1, 2]; L1.append([3, 4]) # L1 is [1, 2, [3, 4]] (len 3)\nL2 = [1, 2]; L2.extend([3, 4]) # L2 is [1, 2, 3, 4]   (len 4)\n```\n\n2. Linear Search Implementation (4 Marks):\n```python\nnumbers = [45, 60, 25, 80, 35, 90]\ntarget = 80\nfound_at = -1\n\nfor i in range(len(numbers)):\n    if numbers[i] == target:\n        found_at = i\n        break\n\nif found_at != -1:\n    print(f\"Element {target} found at index: {found_at}\")\nelse:\n    print(f\"Element {target} not present in list\")\n```"
                }
            ]
        }
    }
}

# Update all 5 papers
all_five = [paper1, paper2, paper3, paper4, paper5]

with open("data/model-papers.json", "w", encoding="utf-8") as f:
    json.dump(all_five, f, indent=2)

print(f"Successfully saved all 5 comprehensive, unique model papers!")

