import json

papers = []

# Model Paper 1
papers.append({
    "id": "model-1",
    "title": "MODEL PAPER 1",
    "subtitle": "College Examination Practice Paper - Pattern Standard",
    "course": "Python Programming (BSC/BA/CSE/MD/5/DSC/301) - Semester V",
    "maxMarks": 35,
    "timeMinutes": 180,
    "instructions": [
        "Question 1 is COMPULSORY (7 Marks) containing 7 objective/short questions of 1 mark each.",
        "Answer ANY ONE question from UNIT-I (Question 2 OR Question 3) - 14 Marks.",
        "Answer ANY ONE question from UNIT-II (Question 4 OR Question 5) - 14 Marks.",
        "Total Marks: 35 | Examination Duration: 3 Hours (180 Minutes).",
        "Write neat and clean Python code with indentation and dry runs wherever required."
    ],
    "q1": {
        "title": "QUESTION 1 (COMPULSORY) — 7 MARKS (1 Mark each)",
        "questions": [
            {
                "subId": "q1-1",
                "question": "Which of the following is NOT a valid identifier in Python?\n(A) _test\n(B) test_1\n(C) 1_test\n(D) testOne",
                "type": "objective",
                "options": ["_test", "test_1", "1_test", "testOne"],
                "modelAnswer": "(C) 1_test. In Python, an identifier cannot start with a numeric digit.",
                "marking": "1 Mark for correct option with brief reason."
            },
            {
                "subId": "q1-2",
                "question": "Name the 3 reserved keywords in Python that start with a capital letter.",
                "type": "short",
                "modelAnswer": "True, False, and None.",
                "marking": "1 Mark for all three correct keywords."
            },
            {
                "subId": "q1-3",
                "question": "Which symbol is used for single-line comments in Python?",
                "type": "short",
                "modelAnswer": "The hash symbol (#).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-4",
                "question": "What is the return data type of Python's input() function by default?",
                "type": "short",
                "modelAnswer": "String (str).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-5",
                "question": "What will be the output of the expression: print(17 // 4, 17 % 4)?",
                "type": "short",
                "modelAnswer": "4 1 (17 // 4 gives integer quotient 4; 17 % 4 gives remainder 1).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-6",
                "question": "What is the difference between 'break' and 'continue' in Python loops?",
                "type": "short",
                "modelAnswer": "'break' terminates the loop completely; 'continue' skips the rest of the current iteration and jumps to the next iteration.",
                "marking": "1 Mark for clear distinction."
            },
            {
                "subId": "q1-7",
                "question": "Are Python lists mutable or immutable?",
                "type": "short",
                "modelAnswer": "Lists in Python are mutable (their elements can be modified in-place).",
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
                    "question": "What are Keywords and Identifiers in Python? State the four golden rules for naming identifiers with valid and invalid examples.",
                    "modelAnswer": "1. Introduction & Definitions (2 Marks):\n- Keywords: Reserved words in Python with fixed predefined meanings that cannot be used as variable names (e.g., if, for, True, None).\n- Identifiers: User-defined names given to variables, functions, or classes to identify them in memory.\n\n2. Naming Rules for Identifiers (3 Marks):\n- Rule 1: Can contain letters (a-z, A-Z), digits (0-9), and underscore (_).\n- Rule 2: Must begin with a letter or underscore (_). CAN NEVER start with a digit.\n- Rule 3: Special symbols (@, $, %, -, spaces) are strictly prohibited.\n- Rule 4: Reserved keywords cannot be used as identifiers.\n\n3. Examples (2 Marks):\n- Valid: student_age, _total, marks1, RollNo\n- Invalid: 1student (starts with digit), total-marks (contains hyphen), class (reserved keyword), my score (contains space)."
                },
                {
                    "part": "2(b)",
                    "marks": 7,
                    "question": "What is a Variable in Python? Explain variable declaration, assignment, dynamic typing, and how user input is read and typecasted with code examples.",
                    "modelAnswer": "1. Variable Definition & Dynamic Typing (2 Marks):\n- A variable is a named memory location that stores data values.\n- Python uses Implicit Declaration and Dynamic Typing: variables do not need explicit type keywords (like int, float). The type is determined automatically at runtime upon assignment.\n\n2. Syntax & Multiple Assignment (2 Marks):\n- x = 10\n- a, b = 20, 30 (Multiple assignment)\n\n3. Reading Input & Typecasting (3 Marks):\n- input() function reads keyboard input as a string.\n- To perform arithmetic calculations, we must typecast using int() or float():\n```python\n# Example Code\nname = input(\"Enter Student Name: \")\nmarks = int(input(\"Enter Marks: \"))\nprint(\"Student:\", name, \"| Score:\", marks)\n```\n- If typecasting is omitted, adding numbers causes string concatenation rather than mathematical addition."
                }
            ]
        },
        "q3": {
            "title": "Question 3 (14 Marks)",
            "parts": [
                {
                    "part": "3(a)",
                    "marks": 7,
                    "question": "Explain Arithmetic, Comparison, and Logical Operators in Python with their syntax and truth tables.",
                    "modelAnswer": "1. Arithmetic Operators (2 Marks):\n- +, -, *, / (float division), // (floor division), % (modulus), ** (power).\n- Example: 10 / 4 = 2.5, 10 // 4 = 2, 10 % 4 = 2, 2 ** 3 = 8.\n\n2. Comparison / Relational Operators (2 Marks):\n- ==, !=, >, <, >=, <=. Always return a Boolean value (True / False).\n- Difference between '=' (assignment) and '==' (equality comparison).\n\n3. Logical Operators & Truth Tables (3 Marks):\n- 'and': True only if both conditions are True.\n- 'or': True if at least one condition is True.\n- 'not': Inverts truth value (not True is False).\n- Truth Table:\n| A | B | A and B | A or B |\n| T | T |    T    |   T    |\n| T | F |    F    |   T    |\n| F | T |    F    |   T    |\n| F | F |    F    |   F    |"
                },
                {
                    "part": "3(b)",
                    "marks": 7,
                    "question": "What is Operator Precedence and Associativity? Explain with a precedence hierarchy table and evaluate the expression: 10 + 5 * 2 ** 2 - 8 // 2.",
                    "modelAnswer": "1. Definitions (2 Marks):\n- Precedence: Dictates the evaluation priority of operators in compound expressions.\n- Associativity: Defines evaluation direction (Left-to-Right or Right-to-Left) for operators of equal precedence.\n\n2. Hierarchy Table (2 Marks):\n- 1. () Parentheses (Highest)\n- 2. ** Exponentiation (Right-to-Left)\n- 3. *, /, //, % (Left-to-Right)\n- 4. +, - (Left-to-Right)\n- 5. Comparisons (==, !=, >, <)\n- 6. not, and, or\n- 7. Assignment (=, +=) (Lowest, Right-to-Left)\n\n3. Step-by-Step Expression Evaluation (3 Marks):\nExpression: 10 + 5 * 2 ** 2 - 8 // 2\n- Step 1: 2 ** 2 = 4 (Power first) -> 10 + 5 * 4 - 8 // 2\n- Step 2: 5 * 4 = 20 (Multiplication) -> 10 + 20 - 8 // 2\n- Step 3: 8 // 2 = 4 (Floor division) -> 10 + 20 - 4\n- Step 4: 10 + 20 = 30 (Addition) -> 30 - 4\n- Step 5: 30 - 4 = 26 (Subtraction)\nFinal Output = 26."
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
                    "question": "Explain Conditional Statements in Python: simple if, if-else, and if-elif ladder with syntax and flowcharts.",
                    "modelAnswer": "1. Introduction to Decision Making (1 Mark):\n- Python uses conditional statements to execute code blocks based on Boolean condition evaluation.\n- Requires uniform 4-space indentation and colon (:) syntax.\n\n2. Simple if & if-else (3 Marks):\n- Simple if: Executes block only if condition is True.\n- if-else: Two-way decision. if block executes on True, else block executes on False.\n- Syntax:\nif condition:\n    statements\nelse:\n    statements\n\n3. if-elif-else Ladder (3 Marks):\n- Used for multi-way decisions. Evaluates sequentially from top to bottom; stops at first True condition.\n- Real-world example (Grading system):\n```python\nmarks = 78\nif marks >= 90: grade = 'A+'\nelif marks >= 75: grade = 'A'\nelif marks >= 60: grade = 'B'\nelse: grade = 'Fail'\nprint('Grade:', grade)\n```"
                },
                {
                    "part": "4(b)",
                    "marks": 7,
                    "question": "Write a complete Python program using while loop to reverse an integer number (e.g. 1234 -> 4321) and check if it is a Palindrome. Provide line-by-line explanation and dry-run table.",
                    "modelAnswer": "1. Concept & Program Code (3 Marks):\n```python\nnum = int(input(\"Enter a number: \"))\noriginal = num\nrev = 0\n\nwhile num > 0:\n    rem = num % 10\n    rev = (rev * 10) + rem\n    num = num // 10\n\nprint(\"Reversed Number:\", rev)\nif original == rev:\n    print(original, \"is a Palindrome\")\nelse:\n    print(original, \"is NOT a Palindrome\")\n```\n\n2. Line-by-Line Explanation (2 Marks):\n- num % 10 extracts the last digit.\n- rev * 10 shifts existing digits left, adding the new digit.\n- num // 10 removes the last digit until num becomes 0.\n\n3. Dry Run Table for input 121 (2 Marks):\n| Step | num | rem (num%10) | rev ((rev*10)+rem) | num (num//10) |\n| 1    | 121 | 1            | 1                  | 12            |\n| 2    | 12  | 2            | 12                 | 1             |\n| 3    | 1   | 1            | 121                | 0             |\nLoop terminates. 121 == 121 -> Palindrome!"
                }
            ]
        },
        "q5": {
            "title": "Question 5 (14 Marks)",
            "parts": [
                {
                    "part": "5(a)",
                    "marks": 7,
                    "question": "What is a List in Python? Explain list creation, indexing, slicing, and mutability with code examples.",
                    "modelAnswer": "1. Definition & Characteristics (2 Marks):\n- A list is an ordered, mutable sequence of heterogeneous elements enclosed in square brackets [ ].\n- Lists can store mixed data types: [101, 'Anjali', 85.5, True].\n\n2. Indexing & Slicing (3 Marks):\n- Positive Indexing: 0 to len-1 (Left-to-right).\n- Negative Indexing: -1 to -len (Right-to-left, -1 is last item).\n- Slicing: list[start:stop:step] where stop is exclusive (stop-1).\n- Example: `nums = [10, 20, 30, 40, 50]`; `nums[1:4]` gives `[20, 30, 40]`.\n- Reversing list: `nums[::-1]`.\n\n3. Mutability (2 Marks):\n- Lists are mutable: elements can be modified in-place: `nums[0] = 99` changes the list directly without creating a new object in memory."
                },
                {
                    "part": "5(b)",
                    "marks": 7,
                    "question": "Explain list methods: append(), insert(), extend(), pop(), remove(), and how 1D arrays are implemented using lists with a search program.",
                    "modelAnswer": "1. List Methods (3 Marks):\n- append(x): Adds item x to the end of list.\n- insert(i, x): Inserts item x at index i.\n- extend(L2): Appends all items of list L2 to current list.\n- pop([i]): Removes and returns element at index i (default last item).\n- remove(x): Removes first occurrence of value x.\n\n2. Implementing 1D Array & Linear Search Program (4 Marks):\n```python\n# Array Implementation using List\narr = [25, 40, 15, 60, 35]\ntarget = 15\nfound_at = -1\n\nfor i in range(len(arr)):\n    if arr[i] == target:\n        found_at = i\n        break\n\nif found_at != -1:\n    print(f\"Element {target} found at index {found_at}\")\nelse:\n    print(\"Element not found\")\n```\n- Traverses through elements using zero-based indices just like arrays in C, demonstrating how Python lists serve as dynamic arrays."
                }
            ]
        }
    }
})

# Model Paper 2
papers.append({
    "id": "model-2",
    "title": "MODEL PAPER 2",
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
                "question": "Which of the following data types in Python is immutable?\n(A) list\n(B) str\n(C) array\n(D) none of these",
                "type": "objective",
                "options": ["list", "str", "array", "none of these"],
                "modelAnswer": "(B) str. Strings in Python are immutable and cannot be modified in-place.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-2",
                "question": "What is the output of the expression: bool(0) and bool(-5)?",
                "type": "short",
                "modelAnswer": "bool(0) is False; bool(-5) is True. (Any non-zero integer is True).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-3",
                "question": "What is the difference between '/' and '//' operators in Python?",
                "type": "short",
                "modelAnswer": "'/' performs float division returning a float (e.g. 5/2 = 2.5); '//' performs floor division returning integer quotient (5//2 = 2).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-4",
                "question": "What does the 'pass' statement do in a Python program?",
                "type": "short",
                "modelAnswer": "It is a null syntactic placeholder statement that performs no operation (NO-OP).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-5",
                "question": "What integer sequence is generated by range(2, 9, 3)?",
                "type": "short",
                "modelAnswer": "2, 5, 8. (Starts at 2, steps by 3, stops before 9).",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-6",
                "question": "What built-in function returns the number of elements in a Python list?",
                "type": "short",
                "modelAnswer": "len() function.",
                "marking": "1 Mark."
            },
            {
                "subId": "q1-7",
                "question": "What is the value of: [10, 20, 30].pop()?",
                "type": "short",
                "modelAnswer": "30 (pop without argument removes and returns the last element).",
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
                    "question": "Explain the Number data types supported by Python: int, float, and complex with their properties, attributes, and examples.",
                    "modelAnswer": "1. int: Whole numbers with unlimited precision in Python 3. Examples: 10, -50, 10000000000.\n2. float: Fractional/decimal numbers with 64-bit IEEE 754 precision. Examples: 3.14, -0.05.\n3. complex: Numbers represented as a + bj where 'a' is real and 'b' is imaginary part. Python uses 'j' (not 'i'). Attributes: .real and .imag return float values.\n```python\nz = 3 + 4j\nprint(z.real) # 3.0\nprint(z.imag) # 4.0\n```"
                },
                {
                    "part": "2(b)",
                    "marks": 7,
                    "question": "What are Comments in Python? Explain the purpose of comments, single-line comments, and multiline comments/docstrings with syntax.",
                    "modelAnswer": "1. Purpose of Comments:\n- Improves code readability for developers.\n- Explains logic and facilitates future maintenance.\n- Enables temporary disabling of code during debugging.\n- Skipped entirely by interpreter.\n\n2. Single-line Comments (#):\n- Starts with '#' symbol. E.g., `# this is a comment`.\n- Can be an inline comment at end of line: `x = 10 # storing age`.\n\n3. Multiline Comments:\n- Can be written using consecutive '#' on each line.\n- Or using triple quotes (''' or \"\"\") as docstrings / multiline string literals."
                }
            ]
        },
        "q3": {
            "title": "Question 3 (14 Marks)",
            "parts": [
                {
                    "part": "3(a)",
                    "marks": 7,
                    "question": "Explain Identity Operators ('is' and 'is not') and distinguish them thoroughly from Equality Operator ('==') with memory diagrams and code.",
                    "modelAnswer": "1. Difference Table:\n| Feature | '==' Operator | 'is' Operator |\n| Purpose | Compares value equality | Compares memory identity (references) |\n| Mechanism | Checks if contents are equal | Checks if id(a) == id(b) |\n\n2. Python Code Example:\n```python\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n\nprint(a == b)      # True (same values)\nprint(a is b)      # False (distinct objects in memory)\nprint(a is c)      # True (both refer to same address)\nprint(a is not b)  # True\n```"
                },
                {
                    "part": "3(b)",
                    "marks": 7,
                    "question": "Write a Python program to read Principal, Rate, and Time from user and calculate Compound Interest. Explain operator precedence involved.",
                    "modelAnswer": "1. Formula: A = P * (1 + R/100)**T, CI = A - P.\n2. Code:\n```python\nP = float(input(\"Principal: \"))\nR = float(input(\"Rate (%): \"))\nT = float(input(\"Time (years): \"))\n\namount = P * ((1 + (R / 100)) ** T)\nCI = amount - P\n\nprint(\"Total Maturity Amount:\", round(amount, 2))\nprint(\"Compound Interest:\", round(CI, 2))\n```\n3. Precedence: (R / 100) and (1 + ...) evaluated first due to parentheses, then ** exponentiation, then * multiplication, and - subtraction."
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
                    "question": "What is the range() function in Python? Explain its 1-argument, 2-argument, and 3-argument forms with examples.",
                    "modelAnswer": "1. Definition: Built-in type that generates an immutable arithmetic progression of integers.\n2. Forms:\n- 1-Arg: range(stop) -> range(4) generates 0, 1, 2, 3.\n- 2-Arg: range(start, stop) -> range(2, 6) generates 2, 3, 4, 5.\n- 3-Arg: range(start, stop, step) -> range(1, 10, 2) generates 1, 3, 5, 7, 9.\n- Negative Step: range(5, 0, -1) generates countdown 5, 4, 3, 2, 1.\n3. Exam Rule: The stop parameter is ALWAYS exclusive (ends at stop-1)."
                },
                {
                    "part": "4(b)",
                    "marks": 7,
                    "question": "Write a Python program to print the Fibonacci series up to N terms using a while loop. Show dry-run table.",
                    "modelAnswer": "1. Code:\n```python\nN = int(input(\"Enter number of terms: \"))\na, b = 0, 1\ncount = 0\n\nwhile count < N:\n    print(a, end=\" \")\n    c = a + b\n    a = b\n    b = c\n    count += 1\n```\n2. Dry run for N=5: \n- count=0: prints 0, next terms: a=1, b=1\n- count=1: prints 1, next terms: a=1, b=2\n- count=2: prints 1, next terms: a=2, b=3\n- count=3: prints 2, next terms: a=3, b=5\n- count=4: prints 3, next terms: a=5, b=8\nOutput: 0 1 1 2 3"
                }
            ]
        },
        "q5": {
            "title": "Question 5 (14 Marks)",
            "parts": [
                {
                    "part": "5(a)",
                    "marks": 7,
                    "question": "Explain built-in functions for lists: len(), min(), max(), sum(), and sorted() with code examples.",
                    "modelAnswer": "1. len(L): Returns total count of elements.\n2. min(L): Finds smallest value.\n3. max(L): Finds largest value.\n4. sum(L): Adds all numeric elements.\n5. sorted(L): Returns a new sorted list without changing the original list.\n```python\nmarks = [45, 90, 60, 30]\nprint(\"Count:\", len(marks))      # 4\nprint(\"Min:\", min(marks))        # 30\nprint(\"Max:\", max(marks))        # 90\nprint(\"Total:\", sum(marks))      # 225\nprint(\"Sorted:\", sorted(marks))  # [30, 45, 60, 90]\n```"
                },
                {
                    "part": "5(b)",
                    "marks": 7,
                    "question": "Explain the difference between append() and extend() methods of lists with memory representations and code demonstrations.",
                    "modelAnswer": "1. append(item): Adds its argument as a SINGLE element at the end of the list. If a list is appended, it becomes a nested list.\n2. extend(iterable): Iterates over the argument and appends each element individually to the list.\n3. Example Code:\n```python\nL1 = [1, 2]\nL1.append([3, 4])\nprint(L1) # [1, 2, [3, 4]] (length is 3)\n\nL2 = [1, 2]\nL2.extend([3, 4])\nprint(L2) # [1, 2, 3, 4] (length is 4)\n```"
                }
            ]
        }
    }
})

# Model Papers 3, 4, 5 templates
for i in [3, 4, 5]:
    papers.append({
        "id": f"model-{i}",
        "title": f"MODEL PAPER {i}",
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
                    "question": "What is the result of 2 ** 3 ** 2 in Python?",
                    "type": "short",
                    "modelAnswer": "512 (Right-to-left associativity: 3**2=9, then 2**9=512).",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-2",
                    "question": "Can a Python variable hold different data types at different times?",
                    "type": "short",
                    "modelAnswer": "Yes, because Python supports dynamic typing.",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-3",
                    "question": "Which operator is used for exponentiation in Python?",
                    "type": "short",
                    "modelAnswer": "** (double asterisk).",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-4",
                    "question": "What is the role of indentation in Python conditional statements?",
                    "type": "short",
                    "modelAnswer": "Indentation defines blocks of code, replacing curly braces {} used in C/Java.",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-5",
                    "question": "What is the output of len('Python 3')?",
                    "type": "short",
                    "modelAnswer": "8 (including the space).",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-6",
                    "question": "Which method removes and returns an element at a given index from a list?",
                    "type": "short",
                    "modelAnswer": "pop([index]) method.",
                    "marking": "1 Mark."
                },
                {
                    "subId": "q1-7",
                    "question": "What is the output of [1, 2, 3] * 2?",
                    "type": "short",
                    "modelAnswer": "[1, 2, 3, 1, 2, 3] (List repetition operator).",
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
                        "question": "Explain Implicit Declaration and Dynamic Typing in Python with suitable program examples and comparison with traditional static typed languages.",
                        "modelAnswer": "In Python, variable types are inferred automatically at runtime upon assignment. No 'int x;' keywords are used. Demonstrates type(val) changing from int to str dynamically."
                    },
                    {
                        "part": "2(b)",
                        "marks": 7,
                        "question": "Explain all Comparison / Relational Operators in Python with code examples and explain why '=' cannot be used in if conditions.",
                        "modelAnswer": "Covers ==, !=, >, <, >=, <= with boolean return values. Explains '=' is assignment while '==' is equality check."
                    }
                ]
            },
            "q3": {
                "title": "Question 3 (14 Marks)",
                "parts": [
                    {
                        "part": "3(a)",
                        "marks": 7,
                        "question": "Explain String creation, positive & negative indexing, and immutability with code examples and memory illustrations.",
                        "modelAnswer": "Strings are immutable sequences in quotes. Positive indexing starts at 0, negative at -1. Illustrates TypeError when attempting s[0]='X'."
                    },
                    {
                        "part": "3(b)",
                        "marks": 7,
                        "question": "Explain Increment/Assignment operators and compound operators in Python. Why does Python not support '++'?",
                        "modelAnswer": "Covers =, +=, -=, *=, /=. Explains that ++ does not exist because integers are immutable objects in Python and + is just a unary sign."
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
                        "question": "What are branching statements? Explain break, continue, and pass in Python loops with syntax, differences, and practical code examples.",
                        "modelAnswer": "break terminates loop immediately; continue skips current iteration; pass is a null placeholder statement. Demonstrates with for loop dry runs."
                    },
                    {
                        "part": "4(b)",
                        "marks": 7,
                        "question": "Write a Python program to calculate the factorial of a given integer using for loop and range(). Provide algorithm, code, and dry-run table.",
                        "modelAnswer": "Explains fact = 1, loop for i in range(1, n+1): fact *= i, handles n=0 and negative error condition with dry-run table."
                    }
                ]
            },
            "q5": {
                "title": "Question 5 (14 Marks)",
                "parts": [
                    {
                        "part": "5(a)",
                        "marks": 7,
                        "question": "Explain how 1D arrays are implemented using lists in Python. Write programs for array traversal, insertion, and deletion.",
                        "modelAnswer": "Explains homogeneous list concept. Implements traversal using for i in range(len(arr)), insertion via insert(), deletion via pop() and remove()."
                    },
                    {
                        "part": "5(b)",
                        "marks": 7,
                        "question": "Write a Python program to implement Linear Search on an array represented as a list. Explain the step-by-step search logic.",
                        "modelAnswer": "Implements linear search loop comparing arr[i] == target. Returns index if found or prints 'not found' with break statement."
                    }
                ]
            }
        }
    })

with open("data/model-papers.json", "w", encoding="utf-8") as f:
    json.dump(papers, f, indent=2)

print(f"Generated {len(papers)} full 35-mark model examination papers successfully.")

