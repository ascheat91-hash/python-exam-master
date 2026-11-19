import json
import os

notes = []

# ==========================================
# UNIT - I : CHAPTER 1
# ==========================================

# u1-t1: Introduction to Python
notes.append({
    "id": "u1-t1",
    "unit": "Unit-I",
    "chapter": "Chapter 1: Introduction, Keywords, Comments & Variables",
    "title": "Introduction to Python & Features",
    "partA_intro": "Python is a popular, high-level, interpreted programming language created by Guido van Rossum and released in 1991. It is designed to be extremely easy to read, write, and learn, making it the ideal first language for students with zero coding background.",
    "partB_realLife": "Think of English as a language we speak every day. Traditional programming languages like C or C++ are like legal court documents with complex rules and punctuation everywhere. Python is like speaking plain, simple English with a friend—concise, clear, and direct.",
    "partC_hinglish": "Agar aapne pehle kabhi programming nahi seekhi hai, toh tension lene ki bilkul zaroorat nahi hai! Python ko aise banaya gaya hai ki iska code lagbhag aam English jaisa lagta hai. C ya Java mein jo kaam 10 lines mein hota hai, Python mein wahi kaam sirf 1 ya 2 lines mein ho jata hai. Isko sikhna aur exam mein likhna dono bahut aasan hai.",
    "partD_examDef": "Python is a high-level, interpreted, dynamically-typed, and general-purpose programming language that emphasizes code readability with its notable use of significant whitespace/indentation.",
    "partE_points": [
        "Easy to Learn & Read: Syntax is clean, simple, and resembles plain English.",
        "Interpreted Language: Python code is executed line-by-line, which makes debugging and finding errors easy.",
        "Dynamically Typed: You do NOT need to declare data types (e.g., int, float) before using a variable; Python detects it automatically.",
        "Platform Independent / Portable: Write once, run on Windows, Mac, Linux, or Android without code changes.",
        "Free and Open Source: Free to use and distribute."
    ],
    "partF_syntax": "# Simple Python Output Syntax\nprint(\"Your message here\")",
    "partG_example": "# Program to display a welcome message for college exam\nprint(\"Welcome to Python Programming\")\nprint(\"Course: BSC/BA/CSE/MD/5/DSC/301\")",
    "partH_lineByLine": [
        "Line 1: # Program... is a comment, Python ignores it completely.",
        "Line 2: print(\"Welcome...\") outputs the greeting text to the user's screen.",
        "Line 3: print(\"Course...\") outputs the exact course code on the next line."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "print(\"Welcome...\")", "action": "Outputs text to screen", "value": "Welcome to Python Programming"},
        {"step": 2, "statement": "print(\"Course...\")", "action": "Outputs course text", "value": "Course: BSC/BA/CSE/MD/5/DSC/301"}
    ],
    "partJ_output": "Welcome to Python Programming\nCourse: BSC/BA/CSE/MD/5/DSC/301",
    "partK_mistakes": [
        "Writing 'Print' instead of 'print'. Python is strictly case-sensitive; function names are lowercase.",
        "Forgetting double or single quotes around text inside print(). e.g., print(Hello) will cause NameError."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Who developed Python and in which year?", "a": "Guido van Rossum in 1991."},
            {"q": "Is Python a compiled or interpreted language?", "a": "Python is an interpreted language (code executes line-by-line)."}
        ],
        "shortAnswer": "Q: Mention four salient features of Python.\nAns: 1. Easy to learn and read, 2. Interpreted nature, 3. Dynamically typed, 4. Free and platform-independent.",
        "fourteenMark": "Q: Explain the history, features, and advantages of Python in detail with suitable examples."
    },
    "partM_revision": "Python was created by Guido van Rossum (1991). Key features: Interpreted, High-level, Dynamically typed, Simple English-like syntax, Case-sensitive."
})

# u1-t2: Keywords & Identifiers
notes.append({
    "id": "u1-t2",
    "unit": "Unit-I",
    "chapter": "Chapter 1: Introduction, Keywords, Comments & Variables",
    "title": "Keywords & Identifiers (Naming Rules)",
    "partA_intro": "Keywords are special words already booked by Python for internal commands. Identifiers are custom names given by the programmer to variables, functions, and lists.",
    "partB_realLife": "Consider traffic rules. Words like 'STOP' and 'ONE-WAY' have fixed meanings for drivers (Keywords). But your own name, roll number, or locker number are custom labels you choose (Identifiers). You cannot name a child 'STOP' in a traffic book!",
    "partC_hinglish": "Keywords wo words hain jo Python ne apne system ke liye pehle se reserve kar rakhe hain (jaise if, else, while, for). Aap inka naam kisi variable ya program ko nahi de sakte. Identifiers wo naam hain jo aap khud decide karte hain (jaise student_name, age, marks). Identifiers rakhne ke kuch pakke rules hote hain jo exam mein har saal aate hain.",
    "partD_examDef": "Keywords are reserved words in Python with predefined syntactic meanings that cannot be used as identifiers. Identifiers are user-defined names given to variables, functions, or classes to uniquely identify them in memory.",
    "partE_points": [
        "Total Keywords: Around 35 keywords in Python 3 (e.g., if, elif, else, while, for, in, is, def, return, True, False, None).",
        "Golden Exam Fact: All keywords are lowercase EXCEPT THREE: True, False, None.",
        "Rule 1 for Identifiers: Can contain letters (a-z, A-Z), digits (0-9), and underscore (_).",
        "Rule 2 for Identifiers: MUST start with a letter or underscore (_). CAN NEVER start with a digit! (e.g., 1st_rank is ILLEGAL).",
        "Rule 3 for Identifiers: Special characters (@, $, %, -, spaces) are strictly PROHIBITED.",
        "Rule 4 for Identifiers: Keywords cannot be used as identifiers."
    ],
    "partF_syntax": "# Valid Identifiers:\nage = 20\n_total_marks = 85\nstudent1 = \"Priya\"\n\n# Invalid Identifiers:\n# 1student = \"Priya\"  (Error: Starts with digit)\n# total marks = 85    (Error: Contains space)\n# class = 5           (Error: 'class' is a keyword)",
    "partG_example": "# Demonstration of Valid Identifiers\nroll_no = 101\nstudent_name = \"Anjali\"\n_marks_sem5 = 32.5\n\nprint(\"Roll Number:\", roll_no)\nprint(\"Student Name:\", student_name)\nprint(\"Marks:\", _marks_sem5)",
    "partH_lineByLine": [
        "Line 1: roll_no is a valid identifier using letters and underscore.",
        "Line 2: student_name stores string value \"Anjali\".",
        "Line 3: _marks_sem5 starts with an underscore, which is completely valid.",
        "Lines 4-6: print() displays the labels and variable contents."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "roll_no = 101", "action": "Memory allocated for roll_no", "value": "101"},
        {"step": 2, "statement": "student_name = 'Anjali'", "action": "Memory allocated for student_name", "value": "'Anjali'"},
        {"step": 3, "statement": "_marks_sem5 = 32.5", "action": "Memory allocated for _marks_sem5", "value": "32.5"}
    ],
    "partJ_output": "Roll Number: 101\nStudent Name: Anjali\nMarks: 32.5",
    "partK_mistakes": [
        "Starting identifier with a number: e.g., 2nd_num = 50 gives SyntaxError.",
        "Using hyphens instead of underscores: roll-no gives SyntaxError because '-' is treated as subtraction operator.",
        "Confusing True/False capitalization: writing true = 5 (lowercase is technically allowed as identifier, but highly discouraged and confusing; True is the keyword)."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which 3 Python keywords start with a capital letter?", "a": "True, False, None."},
            {"q": "Is '2var' a valid identifier in Python? Give reason.", "a": "No, because identifiers cannot begin with a numeric digit."}
        ],
        "shortAnswer": "Q: State the 4 rules for naming identifiers in Python.\nAns: 1. Can contain a-z, A-Z, 0-9, and _. 2. Must begin with a letter or underscore. 3. Cannot contain spaces or special symbols. 4. Cannot be a reserved keyword.",
        "fourteenMark": "Q: What are keywords and identifiers? Explain the rules for naming identifiers with valid and invalid examples."
    },
    "partM_revision": "Keywords = Python's reserved words (if, for, True). Identifiers = User's custom variable/function names. Never start an identifier with a digit or include spaces!"
})

# u1-t3: Comments
notes.append({
    "id": "u1-t3",
    "unit": "Unit-I",
    "chapter": "Chapter 1: Introduction, Keywords, Comments & Variables",
    "title": "Comments (Single-line & Multiline)",
    "partA_intro": "Comments are informative notes written inside the program code to explain what the code does. The Python interpreter completely skips them during execution.",
    "partB_realLife": "Think of a sticky note pasted on a textbook page. When the teacher reads the main book, your sticky note is just for your own memory and understanding; it is not part of the exam question paper.",
    "partC_hinglish": "Jab hum code likhte hain, toh kuch mahino baad hum khud bhool sakte hain ki humne ye line kyu likhi thi. Comments wahi notes hain jo hum apne ya doosre programmers ke samajhne ke liye likhte hain. Python in lines ko bilkul ignore (skip) kar deta hai, iska output par koi asar nahi padta.",
    "partD_examDef": "Comments are non-executable statements in Python source code used to provide explanatory documentation for humans. They are completely ignored by the Python interpreter during program translation.",
    "partE_points": [
        "Purpose: Enhances code readability, simplifies maintenance, and helps in debugging by temporarily disabling code lines.",
        "Single-line Comment: Uses the hash symbol (#). Everything from # to the end of that line is ignored.",
        "Inline Comment: A comment placed at the end of an executable statement (e.g., x = 10 # storing age).",
        "Multiline Comment: Can be created by placing # at the beginning of each line, or using triple quotes (''' or \"\"\") as docstrings/multi-line string blocks."
    ],
    "partF_syntax": "# Single line comment\n\n# Line 1 of comment\n# Line 2 of comment\n\n\"\"\"\nThis is a multiline comment / docstring\nwritten inside triple quotes.\n\"\"\"",
    "partG_example": "# Program to demonstrate single-line and multiline comments\n\n# Initializing student marks\nmarks = 45  # Pass marks threshold is 35\n\n\"\"\"\nNext we check if marks are passing.\nThis part is completely documentation.\n\"\"\"\nprint(\"Final Student Marks:\", marks)",
    "partH_lineByLine": [
        "Line 1: # Program... Python sees # and ignores the whole line.",
        "Line 3: # Initializing... Ignored by interpreter.",
        "Line 4: marks = 45 is executed; # Pass marks... at the end is ignored.",
        "Lines 6-9: Triple quotes contain multi-line text, not assigned to any variable, so treated as comment/docstring.",
        "Line 10: print() executes normally."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "marks = 45", "action": "Assigns integer 45 to variable marks", "value": "45"},
        {"step": 2, "statement": "print(\"Final...\", marks)", "action": "Prints label and marks", "value": "Final Student Marks: 45"}
    ],
    "partJ_output": "Final Student Marks: 45",
    "partK_mistakes": [
        "Using // for comments. // is single-line comment in C/C++/Java, but in Python // is the floor division operator!",
        "Using /* ... */ for comments. Python does not support C-style block comments."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which symbol is used for single-line comments in Python?", "a": "Hash symbol (#)."},
            {"q": "Does Python execute comments during program runtime?", "a": "No, comments are non-executable and ignored by the interpreter."}
        ],
        "shortAnswer": "Q: What is the purpose of comments in Python? How are single-line and multiline comments created?\nAns: Purpose: Code readability and debugging. Single-line: Using '#' symbol. Multiline: Using consecutive '#' symbols or triple quotes (''' or \"\"\").",
        "fourteenMark": "Q: What are comments? Explain their purpose, types (single-line and multiline) with syntax and practical Python examples."
    },
    "partM_revision": "Comments are ignored by Python. Single line = #. Multi-line = multiple # or triple quotes (''' or \"\"\"). Never use // (that is floor division in Python)."
})

# u1-t4: Variables
notes.append({
    "id": "u1-t4",
    "unit": "Unit-I",
    "chapter": "Chapter 1: Introduction, Keywords, Comments & Variables",
    "title": "Variables: Declaration, Assignment, Reading Input & Naming Restrictions",
    "partA_intro": "A variable is a named storage location in computer memory that holds data. When you want to store a number, name, or score in your program so that you can use it later, you store it in a variable.",
    "partB_realLife": "Think of labelled plastic containers in your kitchen. One jar has a sticker 'Sugar', another says 'Salt'. The sticker name is the variable name, and whatever you pour inside is the value. You can change what's inside anytime!",
    "partC_hinglish": "Variable ek memory box (dabba) jaisa hota hai jisme hum apna data store karte hain. Jaise marks = 80. Yahan 'marks' variable ka naam hai aur '80' uski value hai. Python mein aapko pehle se batane ki zaroorat nahi hoti ki dabba integer ka hai ya string ka; aap jo value dalenge, Python automatic samajh jayega. User se value lene ke liye hum input() function use karte hain.",
    "partD_examDef": "A variable is a symbolic name that refers to a specific memory location holding a data value. In Python, variables are dynamically created upon value assignment using the assignment operator (=).",
    "partE_points": [
        "No Explicit Declaration Needed: Unlike C/C++ (e.g., int x;), Python creates a variable automatically the moment you assign a value (e.g., x = 10).",
        "Dynamic Typing: The same variable can hold an integer first, and later hold a string.",
        "Assignment Operator (=): Used to assign the value on the right-hand side to the variable name on the left-hand side.",
        "Multiple Assignment: Python allows a = b = c = 50 or x, y = 10, 20 in a single line.",
        "Reading User Input: input() function reads input from the user. IMPORTANT: input() ALWAYS returns data as a STRING! To get a number, we must typecast it using int() or float().",
        "Naming Restrictions: Same as identifier rules (must begin with a letter or _, no spaces, no special symbols, no keywords)."
    ],
    "partF_syntax": "# Variable Assignment\nvariable_name = value\n\n# Reading String Input\nname = input(\"Enter your name: \")\n\n# Reading Integer Input (Typecasting)\nage = int(input(\"Enter your age: \"))",
    "partG_example": "# Program to take student input and calculate total marks\nname = \"Simran\"\nmaths = 40\npython = 48\n\ntotal = maths + python\nprint(\"Student Name:\", name)\nprint(\"Total Marks:\", total)",
    "partH_lineByLine": [
        "Line 1: name = \"Simran\" creates variable 'name' with string value \"Simran\".",
        "Line 2: maths = 40 creates variable 'maths' holding integer 40.",
        "Line 3: python = 48 creates variable 'python' holding integer 48.",
        "Line 4: total = maths + python adds 40 and 48, storing 88 in 'total'.",
        "Lines 5-6: print() displays the results."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "name = 'Simran'", "action": "Memory box 'name' stores 'Simran'", "value": "'Simran'"},
        {"step": 2, "statement": "maths = 40", "action": "Memory box 'maths' stores 40", "value": "40"},
        {"step": 3, "statement": "python = 48", "action": "Memory box 'python' stores 48", "value": "48"},
        {"step": 4, "statement": "total = maths + python", "action": "40 + 48 = 88 stored in total", "value": "88"}
    ],
    "partJ_output": "Student Name: Simran\nTotal Marks: 88",
    "partK_mistakes": [
        "Forgetting to typecast input(): e.g., age = input() gives string. If user enters 10 and you do age + 5, Python throws TypeError: can only concatenate str to str.",
        "Writing value on left side: 10 = x is ILLEGAL. Variable name must always be on the left side of '='.",
        "Using spaces in variable names: total marks = 100 causes SyntaxError."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the return type of Python's input() function by default?", "a": "String (str)."},
            {"q": "Can a variable hold different data types at different times in Python?", "a": "Yes, because Python is dynamically typed."}
        ],
        "shortAnswer": "Q: How do you read an integer from the user in Python?\nAns: Using int(input(\"prompt\")). The input() function reads the input as a string, and int() converts (typecasts) it into an integer.",
        "fourteenMark": "Q: What is a variable? Explain variable initialization, assignment, naming restrictions, and how user input is read and typecasted in Python with examples."
    },
    "partM_revision": "Variable = named memory box. '=' assigns values. No data type declaration needed. input() always gives string; wrap in int() or float() for numbers."
})

# ==========================================
# UNIT - I : CHAPTER 2: DATA TYPES
# ==========================================

# u1-t5: Implicit Declaration & Dynamic Typing
notes.append({
    "id": "u1-t5",
    "unit": "Unit-I",
    "chapter": "Chapter 2: Data Types",
    "title": "Implicit Declaration & Dynamic Typing",
    "partA_intro": "In programming, declaring a variable means telling the computer what type of data it will store. Python uses 'Implicit Declaration', meaning you do not have to specify the type manually; Python determines it automatically based on the assigned value.",
    "partB_realLife": "Imagine walking into a shoe store. If you hand the shopkeeper a coin, he knows it's money. If you hand him a coupon, he knows it's a coupon. You don't have to shout 'This is a coin!' before handing it over. He implicitly knows by seeing the object.",
    "partC_hinglish": "C ya Java mein agar hume koi number store karna hota tha, toh hume pehle 'int x = 10;' likhna padta tha. Lekin Python itna smart hai ki agar aap sirf 'x = 10' likhenge, toh Python khud samajh jayega ki x integer hai. Ise 'Implicit Declaration' aur 'Dynamic Typing' kehte hain. type() function se hum kisi bhi variable ka type check kar sakte hain.",
    "partD_examDef": "Implicit declaration is a feature of Python where variable data types are automatically determined by the interpreter at runtime based on the assigned value, without any explicit type declaration keywords.",
    "partE_points": [
        "Dynamic Typing: Variables are not bound to a fixed data type; their type changes dynamically if a new value of another type is assigned.",
        "No Type Keywords: Python does not use 'int x;', 'float y;', etc.",
        "type() Function: Built-in function used to inspect the data type of any variable or value.",
        "Memory Efficiency: Python handles memory allocation and garbage collection automatically."
    ],
    "partF_syntax": "# Checking data type:\ntype(variable_name)",
    "partG_example": "# Demonstration of Implicit Declaration and Dynamic Typing\nval = 100\nprint(type(val))  # Integer\n\nval = \"Now I am a string\"\nprint(type(val))  # String dynamically changed",
    "partH_lineByLine": [
        "Line 1: val = 100 assigns integer 100 to val. Python implicitly types val as int.",
        "Line 2: print(type(val)) prints <class 'int'>.",
        "Line 4: val = \"Now I am a string\" reassigns a string to the same variable val.",
        "Line 5: print(type(val)) prints <class 'str'>, showing dynamic typing in action."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "val = 100", "action": "val points to integer object 100", "value": "100 (<class 'int'>)"},
        {"step": 2, "statement": "val = 'Now I am...'", "action": "val re-points to string object", "value": "'Now I am...' (<class 'str'>)"}
    ],
    "partJ_output": "<class 'int'>\n<class 'str'>",
    "partK_mistakes": [
        "Writing 'int x = 10'. In Python, this will throw a SyntaxError because 'int' is a type constructor, not a declaration keyword.",
        "Assuming a variable is locked to one type forever. In Python, variable types are fully dynamic."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which function is used to find the data type of a variable in Python?", "a": "type() function."},
            {"q": "What is meant by dynamic typing in Python?", "a": "Variables can hold values of different data types during execution without explicit declaration."}
        ],
        "shortAnswer": "Q: Differentiate between static typing and dynamic typing.\nAns: In static typing (like C/Java), variable types must be declared explicitly before use and cannot change. In dynamic typing (Python), types are inferred automatically at runtime and can change dynamically.",
        "fourteenMark": "Q: Explain the concept of implicit declaration and dynamic typing in Python with suitable program examples and comparison with traditional languages."
    },
    "partM_revision": "Implicit declaration = Python detects type automatically. Dynamic typing = variable type can change at runtime. Use type(x) to inspect type."
})

# u1-t6: Number Data Types
notes.append({
    "id": "u1-t6",
    "unit": "Unit-I",
    "chapter": "Chapter 2: Data Types",
    "title": "Number Data Types: int, float, complex",
    "partA_intro": "Numbers are fundamental data types in Python used to perform mathematical calculations. Python provides three core numeric types: int (whole numbers), float (decimal numbers), and complex (numbers with real and imaginary parts).",
    "partB_realLife": "1. int: Counting students in a classroom (e.g., 45 students, cannot be 45.5).\n2. float: Weighing flour or sugar (e.g., 2.75 kg).\n3. complex: Advanced electrical engineering calculations involving AC current alternating phases.",
    "partC_hinglish": "Python mein numbers 3 tarah ke hote hain:\n1. int: Bina point wale poore number, jaise 10, -5, 1000. Python 3 mein int ki koi size limit nahi hoti!\n2. float: Point (decimal) wale number, jaise 3.14, 99.9, -0.5.\n3. complex: Jisme ek real part hota hai aur ek imaginary part jisme 'j' lagta hai, jaise 3 + 4j. Exam ke liye dhyan rakhe ki Python mein 'i' nahi, 'j' use hota hai!",
    "partD_examDef": "Python supports three built-in numeric data types: int for arbitrarily large integers, float for double-precision floating-point numbers, and complex for numbers having a real and imaginary part (represented as a + bj).",
    "partE_points": [
        "int: Whole numbers (positive, negative, zero) with unlimited precision in Python 3.",
        "float: Fractional or decimal numbers represented with 64-bit IEEE 754 precision.",
        "complex: Numbers represented as a + bj, where a is real part and b is imaginary part. Python uses 'j' or 'J' for the imaginary unit (NOT 'i').",
        "Accessing complex components: num.real gives the real part, and num.imag gives the imaginary part (both as floats)."
    ],
    "partF_syntax": "a = 15          # int\nb = 12.75       # float\nc = 4 + 3j      # complex",
    "partG_example": "# Program illustrating int, float, and complex numbers\nx = 25\ny = 14.5\nz = 2 + 5j\n\nprint(\"Value of x:\", x, \"Type:\", type(x))\nprint(\"Value of y:\", y, \"Type:\", type(y))\nprint(\"Value of z:\", z, \"Type:\", type(z))\nprint(\"Real part of z:\", z.real)\nprint(\"Imaginary part of z:\", z.imag)",
    "partH_lineByLine": [
        "Line 1: x = 25 stores an integer.",
        "Line 2: y = 14.5 stores a floating-point number.",
        "Line 3: z = 2 + 5j stores a complex number with real=2 and imaginary=5.",
        "Lines 4-6: Prints values and verified types using type().",
        "Lines 7-8: z.real extracts 2.0 and z.imag extracts 5.0."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "x = 25", "action": "x becomes int", "value": "25"},
        {"step": 2, "statement": "y = 14.5", "action": "y becomes float", "value": "14.5"},
        {"step": 3, "statement": "z = 2 + 5j", "action": "z becomes complex", "value": "(2+5j)"},
        {"step": 4, "statement": "z.real / z.imag", "action": "Extract parts", "value": "2.0, 5.0"}
    ],
    "partJ_output": "Value of x: 25 Type: <class 'int'>\nValue of y: 14.5 Type: <class 'float'>\nValue of z: (2+5j) Type: <class 'complex'>\nReal part of z: 2.0\nImaginary part of z: 5.0",
    "partK_mistakes": [
        "Using 'i' for complex numbers: 3 + 4i causes SyntaxError. In Python, you must use 'j' (e.g., 3 + 4j).",
        "Writing 4j as 4 * j without defining j: Always write the number directly attached to j, e.g., 5j."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which symbol represents the imaginary component of a complex number in Python?", "a": "'j' or 'J'."},
            {"q": "What is the data type of the expression 5 / 2 in Python 3?", "a": "float (result is 2.5)."}
        ],
        "shortAnswer": "Q: Explain the numeric data types available in Python with examples.\nAns: 1. int (e.g., 100), 2. float (e.g., 45.8), 3. complex (e.g., 3 + 4j where .real=3.0 and .imag=4.0).",
        "fourteenMark": "Q: Describe in detail the numeric data types supported by Python. Explain int, float, and complex numbers with their properties, attributes, and practical examples."
    },
    "partM_revision": "int = whole numbers, float = decimals, complex = real + imaginary with 'j' (e.g. 2 + 3j). Attributes: .real and .imag."
})

# u1-t7: Strings
notes.append({
    "id": "u1-t7",
    "unit": "Unit-I",
    "chapter": "Chapter 2: Data Types",
    "title": "Strings (Creation, Indexing & Immutability)",
    "partA_intro": "A String is an ordered sequence of characters enclosed within quotation marks. It is used to store text such as words, sentences, roll numbers, or addresses.",
    "partB_realLife": "Think of a pearl necklace where each pearl represents a letter. You can point to the first pearl (index 0), second pearl (index 1), or the last pearl (index -1). But you cannot swap a pearl without making a whole new necklace (Strings are immutable).",
    "partC_hinglish": "String ka matlab hota hai text (akshar ya shabd). Python mein string ko single quote ('...') ya double quote (\"...\") mein likhte hain. String ke har character ka ek number hota hai jise 'Index' kehte hain. Index hamesha 0 se start hota hai. Python mein 'Negative Indexing' bhi hoti hai jisme -1 ka matlab aakhiri character hota hai. Ek important exam point: Strings 'Immutable' hoti hain, yaani ek baar banne ke baad unka koi character badla nahi ja sakta.",
    "partD_examDef": "A string in Python is an immutable sequence of Unicode characters enclosed in single quotes (' '), double quotes (\" \"), or triple quotes (''' ''').",
    "partE_points": [
        "Creation: s = 'Hello' or s = \"Hello\" or s = \"\"\"Hello\"\"\".",
        "Positive Indexing: Starts from 0 (left-to-right, 0, 1, 2, ...).",
        "Negative Indexing: Starts from -1 (right-to-left, -1, -2, -3, ...).",
        "Immutability: You cannot change individual characters in a string. s[0] = 'M' will raise a TypeError.",
        "String Length: len(s) returns the total number of characters in the string."
    ],
    "partF_syntax": "s = \"Python\"\nfirst_char = s[0]    # 'P'\nlast_char = s[-1]    # 'n'\nlength = len(s)      # 6",
    "partG_example": "# Program demonstrating string indexing and immutability\nsubject = \"PYTHON\"\n\nprint(\"Original String:\", subject)\nprint(\"First character (index 0):\", subject[0])\nprint(\"Third character (index 2):\", subject[2])\nprint(\"Last character (index -1):\", subject[-1])\nprint(\"Total length:\", len(subject))",
    "partH_lineByLine": [
        "Line 1: subject = \"PYTHON\" stores 6 characters: P(0), Y(1), T(2), H(3), O(4), N(5).",
        "Line 3: prints the full string.",
        "Line 4: subject[0] accesses the 0th index ('P').",
        "Line 5: subject[2] accesses the 2nd index ('T').",
        "Line 6: subject[-1] accesses the rightmost character ('N').",
        "Line 7: len(subject) calculates count of characters, which is 6."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "subject = 'PYTHON'", "action": "String allocated", "value": "'PYTHON'"},
        {"step": 2, "statement": "subject[0]", "action": "Lookup index 0", "value": "'P'"},
        {"step": 3, "statement": "subject[2]", "action": "Lookup index 2", "value": "'T'"},
        {"step": 4, "statement": "subject[-1]", "action": "Lookup index -1", "value": "'N'"},
        {"step": 5, "statement": "len(subject)", "action": "Calculates length", "value": "6"}
    ],
    "partJ_output": "Original String: PYTHON\nFirst character (index 0): P\nThird character (index 2): T\nLast character (index -1): N\nTotal length: 6",
    "partK_mistakes": [
        "Attempting to modify a string: subject[0] = 'J' throws TypeError: 'str' object does not support item assignment.",
        "Index out of range: For a string of length 6, accessing subject[6] throws IndexError because valid indices are 0 to 5."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Are Python strings mutable or immutable?", "a": "Immutable."},
            {"q": "What is the index of the last character in any non-empty Python string?", "a": "-1 (negative index) or len(s) - 1."}
        ],
        "shortAnswer": "Q: What is negative indexing in Python strings? Explain with an example.\nAns: Negative indexing counts characters from right to left, starting at -1 for the last character, -2 for second-to-last, etc. Example: s = 'EXAM', s[-1] is 'M'.",
        "fourteenMark": "Q: What is a String in Python? Explain string creation, positive and negative indexing, immutability, and built-in string functions with detailed examples."
    },
    "partM_revision": "Strings = sequence of characters. Immutable (cannot change in-place). Left-to-right index begins at 0; Right-to-left index begins at -1. len(s) gives total characters."
})

# u1-t8: Boolean Data Type
notes.append({
    "id": "u1-t8",
    "unit": "Unit-I",
    "chapter": "Chapter 2: Data Types",
    "title": "Boolean Data Type (True / False)",
    "partA_intro": "The Boolean data type represents one of two possible values: True or False. It is predominantly used in conditional statements, decision making, and logical evaluations.",
    "partB_realLife": "Think of a light switch on a wall. It can only be in one of two states: ON (True) or OFF (False). There is no third state. Similarly, an exam question is either correct or incorrect.",
    "partC_hinglish": "Boolean data type mein sirf 2 hi values ho sakti hain: True (sach/haan) ya False (jhooth/naa). Jab bhi hum do numbers ki tulna (comparison) karte hain, jaise 10 > 5, toh Python answer deta hai 'True'. Agar 5 > 10 poochenge toh answer aayega 'False'. Yaad rakhein: True aur False ka 'T' aur 'F' hamesha Capital hota hai!",
    "partD_examDef": "Boolean (bool) is a built-in Python data type that can take one of two truth values: True or False. In Python, bool is a subclass of int, where True is equal to 1 and False is equal to 0.",
    "partE_points": [
        "Keywords: True and False are reserved keywords in Python.",
        "Capitalization Rule: Must be capitalized (True, False). Writing 'true' or 'false' will result in NameError.",
        "Numeric Equivalence: In arithmetic operations, True acts as 1 and False acts as 0. (e.g., True + True = 2).",
        "bool() Function: Evaluates truth value of any object. Numbers other than 0 are True; 0, empty string \"\", empty list [] evaluate to False."
    ],
    "partF_syntax": "is_passed = True\nis_failed = False\nresult = 10 > 5  # Evaluates to True",
    "partG_example": "# Program to demonstrate Boolean values and evaluation\nis_student = True\nmarks = 72\nis_passed = marks >= 35\n\nprint(\"Is Student:\", is_student)\nprint(\"Passed Exam:\", is_passed)\nprint(\"Boolean as integer (True + 5):\", True + 5)",
    "partH_lineByLine": [
        "Line 1: is_student is assigned boolean literal True.",
        "Line 2: marks is set to 72.",
        "Line 3: marks >= 35 checks if 72 is greater than or equal to 35, evaluating to True.",
        "Lines 4-5: Prints boolean values.",
        "Line 6: True + 5 treats True as 1, so 1 + 5 = 6."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "is_student = True", "action": "Boolean assigned", "value": "True"},
        {"step": 2, "statement": "marks = 72", "action": "Integer assigned", "value": "72"},
        {"step": 3, "statement": "is_passed = 72 >= 35", "action": "Comparison evaluation", "value": "True"},
        {"step": 4, "statement": "True + 5", "action": "Arithmetic with bool (1 + 5)", "value": "6"}
    ],
    "partJ_output": "Is Student: True\nPassed Exam: True\nBoolean as integer (True + 5): 6",
    "partK_mistakes": [
        "Writing true or false with lowercase: x = true causes NameError: name 'true' is not defined.",
        "Wrapping True in quotes: x = \"True\" creates a String (str), NOT a Boolean!"
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the numeric value of True and False in Python?", "a": "True = 1, False = 0."},
            {"q": "What will be the output of bool(0) and bool(10)?", "a": "bool(0) is False; bool(10) is True."}
        ],
        "shortAnswer": "Q: Explain the Boolean data type in Python with its integer relation.\nAns: The bool data type has two values: True and False. Both are keywords. Internally, True is represented as 1 and False as 0, allowing them to be used in arithmetic operations.",
        "fourteenMark": "Q: What are basic data types in Python? Explain Numbers, Strings, and Booleans with examples, syntax, memory characteristics, and type conversion."
    },
    "partM_revision": "Boolean has only 2 values: True and False (first letter capital). True == 1, False == 0. bool(0) is False, bool(any_number) is True."
})

# ==========================================
# UNIT - I : CHAPTER 3: OPERATORS
# ==========================================

# u1-t9: Arithmetic Operators
notes.append({
    "id": "u1-t9",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Arithmetic Operators (+, -, *, /, //, %, **)",
    "partA_intro": "Arithmetic operators are used to perform common mathematical operations such as addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.",
    "partB_realLife": "Think of a standard pocket calculator. When you press '+' to add prices or '×' to calculate total cost, you are using arithmetic operators.",
    "partC_hinglish": "Arithmetic operators ka use basic maths karne ke liye hota hai. Python mein regular operators (+, -, *) ke alawa 3 bahut important special operators hote hain jo exam mein zaroor aate hain:\n1. / (Division): Hamesha float (decimal) answer deta hai (10 / 2 = 5.0).\n2. // (Floor Division): Point ke baad ki value ko hata deta hai (10 // 3 = 3).\n3. % (Modulus): Bhaag karne ke baad bacha hua 'Remainder' (sheshphal) deta hai (10 % 3 = 1).\n4. ** (Exponent/Power): Power nikalne ke liye (2 ** 3 = 8).",
    "partD_examDef": "Arithmetic operators are binary operators used to perform standard arithmetic computations between two numeric operands in Python.",
    "partE_points": [
        "+ (Addition): Adds two values (e.g., 5 + 3 = 8). Also concatenates strings.",
        "- (Subtraction): Subtracts right operand from left operand (e.g., 10 - 4 = 6).",
        "* (Multiplication): Multiplies numbers (e.g., 4 * 3 = 12). Also repeats strings.",
        "/ (Float Division): Always returns a float result (e.g., 7 / 2 = 3.5).",
        "// (Floor Division): Returns the integer quotient rounded down towards minus infinity (e.g., 7 // 2 = 3).",
        "% (Modulus / Remainder): Returns the remainder of division (e.g., 7 % 2 = 1).",
        "** (Exponentiation / Power): Raises left operand to power of right operand (e.g., 2 ** 4 = 16)."
    ],
    "partF_syntax": "a = 15\nb = 4\nadd = a + b\nfloor_div = a // b\nrem = a % b\npower = 2 ** 3",
    "partG_example": "# Program demonstrating all 7 arithmetic operators\na = 17\nb = 5\n\nprint(\"Addition (a + b):\", a + b)\nprint(\"Subtraction (a - b):\", a - b)\nprint(\"Multiplication (a * b):\", a * b)\nprint(\"Float Division (a / b):\", a / b)\nprint(\"Floor Division (a // b):\", a // b)\nprint(\"Modulus/Remainder (a % b):\", a % b)\nprint(\"Exponentiation (2 ** 3):\", 2 ** 3)",
    "partH_lineByLine": [
        "Line 1-2: a is 17 and b is 5.",
        "Line 4: 17 + 5 evaluates to 22.",
        "Line 5: 17 - 5 evaluates to 12.",
        "Line 6: 17 * 5 evaluates to 85.",
        "Line 7: 17 / 5 evaluates to 3.4 (always float).",
        "Line 8: 17 // 5 evaluates to 3 (drops decimal).",
        "Line 9: 17 % 5 evaluates to 2 (17 = 5 * 3 + 2).",
        "Line 10: 2 ** 3 calculates 2 cubed = 8."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "17 / 5", "action": "Float division", "value": "3.4"},
        {"step": 2, "statement": "17 // 5", "action": "Floor division (quotient)", "value": "3"},
        {"step": 3, "statement": "17 % 5", "action": "Modulus (remainder)", "value": "2"},
        {"step": 4, "statement": "2 ** 3", "action": "2 * 2 * 2", "value": "8"}
    ],
    "partJ_output": "Addition (a + b): 22\nSubtraction (a - b): 12\nMultiplication (a * b): 85\nFloat Division (a / b): 3.4\nFloor Division (a // b): 3\nModulus/Remainder (a % b): 2\nExponentiation (2 ** 3): 8",
    "partK_mistakes": [
        "Confusing / and //: 10 / 2 returns 5.0 (float), whereas 10 // 2 returns 5 (int).",
        "Division by zero: 10 / 0 or 10 % 0 causes ZeroDivisionError."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the difference between '/' and '//' operators in Python?", "a": "'/' returns float quotient (e.g. 5/2 = 2.5); '//' returns integer floor quotient (5//2 = 2)."},
            {"q": "What will be the output of 7 % 3 and 2 ** 3?", "a": "7 % 3 is 1; 2 ** 3 is 8."}
        ],
        "shortAnswer": "Q: Explain the modulus (%) and exponentiation (**) operators with examples.\nAns: Modulus (%) returns remainder: 14 % 4 = 2. Exponentiation (**) raises base to power: 3 ** 2 = 9.",
        "fourteenMark": "Q: What are Arithmetic operators in Python? Explain each operator with purpose, syntax, examples, dry run, and difference between division and floor division."
    },
    "partM_revision": "+, -, *, / (gives float), // (floor/int quotient), % (remainder), ** (power). Zero division raises ZeroDivisionError."
})

# u1-t10: Comparison / Relational Operators
notes.append({
    "id": "u1-t10",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Comparison / Relational Operators (==, !=, >, <, >=, <=)",
    "partA_intro": "Comparison or relational operators are used to compare the values of two operands. The result of a comparison is always a Boolean value: either True or False.",
    "partB_realLife": "Think of a security guard checking heights at a rollercoaster ride. If height >= 4.5 feet, you can enter; otherwise you cannot. He compares your height against the cutoff.",
    "partC_hinglish": "Relational operators do values ki tulna karne ke kaam aate hain. Inka jawab hamesha sirf 'True' ya 'False' mein aata hai. Sabse zaroori baat: Python mein Barabar (Equal to) check karne ke liye double equal to '==' lagaya jata hai, single '=' nahi! Single '=' value assign karta hai, aur '==' value compare karta hai.",
    "partD_examDef": "Comparison (relational) operators compare the values of two operands and evaluate to a Boolean truth value (True or False) based on whether the condition holds.",
    "partE_points": [
        "== (Equal to): Returns True if both operands are equal (e.g., 5 == 5 is True).",
        "!= (Not Equal to): Returns True if operands are NOT equal (e.g., 5 != 3 is True).",
        "> (Greater than): Returns True if left operand is strictly greater than right operand.",
        "< (Less than): Returns True if left operand is strictly less than right operand.",
        ">= (Greater than or equal to): Returns True if left operand is greater than or equal to right operand.",
        "<= (Less than or equal to): Returns True if left operand is less than or equal to right operand.",
        "Exam Trap: = is assignment, while == is comparison!"
    ],
    "partF_syntax": "a == b\na != b\na > b\na <= b",
    "partG_example": "# Program demonstrating comparison operators\nx = 20\ny = 15\n\nprint(\"x == y:\", x == y)   # False\nprint(\"x != y:\", x != y)   # True\nprint(\"x > y:\", x > y)     # True\nprint(\"x < y:\", x < y)     # False\nprint(\"x >= 20:\", x >= 20) # True\nprint(\"y <= 10:\", y <= 10) # False",
    "partH_lineByLine": [
        "Line 1-2: x is 20, y is 15.",
        "Line 4: 20 == 15 is False.",
        "Line 5: 20 != 15 is True.",
        "Line 6: 20 > 15 is True.",
        "Line 7: 20 < 15 is False.",
        "Line 8: 20 >= 20 is True (since 20 equals 20).",
        "Line 9: 15 <= 10 is False."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "20 == 15", "action": "Equality test", "value": "False"},
        {"step": 2, "statement": "20 != 15", "action": "Inequality test", "value": "True"},
        {"step": 3, "statement": "20 >= 20", "action": "Greater or equal", "value": "True"}
    ],
    "partJ_output": "x == y: False\nx != y: True\nx > y: True\nx < y: False\nx >= 20: True\ny <= 10: False",
    "partK_mistakes": [
        "Using single '=' in conditions: if x = 10: causes SyntaxError. You must write if x == 10:.",
        "Writing =< or =>: Invalid syntax! Always put the angle bracket first (<=, >=)."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the difference between '=' and '==' in Python?", "a": "'=' is the assignment operator; '==' is the relational comparison operator."},
            {"q": "What will be the output of: 10 >= 10?", "a": "True."}
        ],
        "shortAnswer": "Q: List all comparison operators in Python and their return type.\nAns: ==, !=, >, <, >=, <=. Their return type is always Boolean (True or False).",
        "fourteenMark": "Q: Explain relational/comparison operators in Python. Differentiate between assignment and comparison with code examples, truth tables, and common errors."
    },
    "partM_revision": "Comparison operators return True or False. == (equal), != (not equal), >, <, >=, <=. Never write = inside condition checks."
})

# u1-t11: Increment / Assignment Operators
notes.append({
    "id": "u1-t11",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Increment / Assignment Operators (=, +=, -=, etc.)",
    "partA_intro": "Assignment operators are used to store values into variables. Compound (augmented) assignment operators perform an arithmetic operation and assign the result in a single step.",
    "partB_realLife": "Think of your piggy bank. If you already have ₹50 and add ₹20 more, you do: Total = Total + 20. In Python shorthand, you simply write: Total += 20.",
    "partC_hinglish": "Python mein value store karne ke liye '=' use hota hai. Agar hume kisi variable ki purani value mein hi kuch jodna ya ghatana ho, toh hum short-cut (Compound Assignment) use karte hain. Jaise 'x = x + 5' ko hum 'x += 5' likh sakte hain. Ek zaroori exam point: Python mein C/C++ ki tarah '++' ya '--' operator NAHI hota hai! Python mein increment karne ke liye sirf '+= 1' likhte hain.",
    "partD_examDef": "Assignment operators store values into variables. Compound assignment operators (e.g., +=, -=, *=, /=) combine an arithmetic operation with assignment into a single shorthand expression.",
    "partE_points": [
        "= (Simple Assignment): Assigns right value to left variable (x = 10).",
        "+= (Add and Assign): x += 5 is equivalent to x = x + 5.",
        "-= (Subtract and Assign): x -= 3 is equivalent to x = x - 3.",
        "*= (Multiply and Assign): x *= 2 is equivalent to x = x * 2.",
        "/= (Divide and Assign): x /= 4 is equivalent to x = x / 4.",
        "//=: Floor divide and assign.",
        "%=: Modulus and assign.",
        "**=: Power and assign.",
        "IMPORTANT EXAM FACT: Python does NOT have pre/post increment operators (x++ or ++x do not exist in Python!)."
    ],
    "partF_syntax": "x = 10\nx += 5   # x is now 15\nx *= 2   # x is now 30",
    "partG_example": "# Program demonstrating compound assignment operators\na = 20\nprint(\"Initial value of a:\", a)\n\na += 10  # a = a + 10\nprint(\"After a += 10:\", a)\n\na -= 5   # a = a - 5\nprint(\"After a -= 5:\", a)\n\na *= 2   # a = a * 2\nprint(\"After a *= 2:\", a)\n\na //= 4  # a = a // 4\nprint(\"After a //= 4:\", a)",
    "partH_lineByLine": [
        "Line 1: a is initialized to 20.",
        "Line 4: a += 10 adds 10 to 20, making a = 30.",
        "Line 7: a -= 5 subtracts 5 from 30, making a = 25.",
        "Line 10: a *= 2 multiplies 25 by 2, making a = 50.",
        "Line 13: a //= 4 divides 50 by 4, dropping decimals, making a = 12."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "a = 20", "action": "Initialization", "value": "20"},
        {"step": 2, "statement": "a += 10", "action": "20 + 10", "value": "30"},
        {"step": 3, "statement": "a -= 5", "action": "30 - 5", "value": "25"},
        {"step": 4, "statement": "a *= 2", "action": "25 * 2", "value": "50"},
        {"step": 5, "statement": "a //= 4", "action": "50 // 4", "value": "12"}
    ],
    "partJ_output": "Initial value of a: 20\nAfter a += 10: 30\nAfter a -= 5: 25\nAfter a *= 2: 50\nAfter a //= 4: 12",
    "partK_mistakes": [
        "Attempting to use x++: In Python, x++ gives SyntaxError. You must write x += 1.",
        "Writing =+ instead of +=: a =+ 5 assigns positive 5 to a, it does NOT increment!"
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Does Python support the '++' increment operator?", "a": "No, Python does not support '++'. We use '+= 1' instead."},
            {"q": "What is the equivalent expression for: x %= 4?", "a": "x = x % 4."}
        ],
        "shortAnswer": "Q: What are compound assignment operators? Give two examples.\nAns: Compound operators combine arithmetic and assignment into one step. Examples: a += b (a = a + b) and a *= b (a = a * b).",
        "fourteenMark": "Q: What are assignment and compound assignment operators in Python? Explain each operator with shorthand equivalents, examples, and explain why ++ is not supported in Python."
    },
    "partM_revision": "Assignment: =. Compound: +=, -=, *=, /=, //=, %=, **=. Python has NO ++ or --. Always use x += 1."
})

# u1-t12: Logical Operators
notes.append({
    "id": "u1-t12",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Logical Operators (and, or, not)",
    "partA_intro": "Logical operators are used to combine multiple conditional expressions or invert the truth value of a condition. They are essential for building complex decision-making logic.",
    "partB_realLife": "Think of exam eligibility: To sit in the exam, you need (Admit Card == True) AND (Attendance >= 75). If either is missing, you cannot sit. But for ID proof, you can show (Aadhar Card OR Voter ID).",
    "partC_hinglish": "Logical operators ka use multiple conditions ko ek sath check karne ke liye hota hai. Python mein teen logical operators hote hain:\n1. and: Jab dono conditions True hongi, tabhi result True aayega. Agar ek bhi False hui toh result False.\n2. or: Agar dono mein se koi bhi EK condition True ho gayi, toh result True aa jayega.\n3. not: Ye ulta (reverse) kar deta hai. True ko False aur False ko True bana deta hai.\nDhyan de: Python mein symbols (&&, ||, !) nahi, seedha English words (and, or, not) use hote hain!",
    "partD_examDef": "Logical operators in Python are used to perform logical conjunction (and), disjunction (or), and negation (not) on Boolean expressions.",
    "partE_points": [
        "and operator: Evaluates to True only if BOTH operands/conditions are True.",
        "or operator: Evaluates to True if AT LEAST ONE operand/condition is True.",
        "not operator: Unary operator that inverts the Boolean truth value (not True is False).",
        "English words: Python uses lowercase words: 'and', 'or', 'not' (NOT &&, ||, !).",
        "Short-Circuit Evaluation: In 'A and B', if A is False, B is not evaluated. In 'A or B', if A is True, B is not evaluated."
    ],
    "partF_syntax": "condition1 and condition2\ncondition1 or condition2\nnot condition",
    "partG_example": "# Program demonstrating logical operators\nage = 22\nhas_license = True\n\ncan_drive = (age >= 18) and has_license\nprint(\"Can Drive (and):\", can_drive)\n\nhas_cash = False\nhas_upi = True\ncan_pay = has_cash or has_upi\nprint(\"Can Pay (or):\", can_pay)\n\nprint(\"Negation of True (not True):\", not True)",
    "partH_lineByLine": [
        "Line 1-2: age is 22, has_license is True.",
        "Line 4: age >= 18 is True, and has_license is True. True and True evaluates to True.",
        "Line 7-8: has_cash is False, has_upi is True. False or True evaluates to True.",
        "Line 11: not True flips the boolean to False."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "True and True", "action": "and operation", "value": "True"},
        {"step": 2, "statement": "False or True", "action": "or operation", "value": "True"},
        {"step": 3, "statement": "not True", "action": "not operation", "value": "False"}
    ],
    "partJ_output": "Can Drive (and): True\nCan Pay (or): True\nNegation of True (not True): False",
    "partK_mistakes": [
        "Using && or ||: In Python, using && or || results in SyntaxError. Use 'and' and 'or'.",
        "Confusing and / or behavior when combining conditions."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What will be the result of: (5 > 2) and (10 < 3)?", "a": "False (since True and False is False)."},
            {"q": "What will be the result of: not (10 == 10)?", "a": "False (since not True is False)."}
        ],
        "shortAnswer": "Q: Draw the truth table for the 'and' and 'or' operators in Python.\nAns: \nand: T and T = T; T and F = F; F and T = F; F and F = F.\nor: T or T = T; T or F = T; F or T = T; F or F = F.",
        "fourteenMark": "Q: Explain logical operators in Python with their complete truth tables, short-circuit evaluation mechanism, and practical programming examples."
    },
    "partM_revision": "and = True only if all are True. or = True if any one is True. not = reverses the value. Use words: and, or, not."
})

# u1-t13: Identity Operators
notes.append({
    "id": "u1-t13",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Identity Operators (is, is not)",
    "partA_intro": "Identity operators are used to compare the memory locations (identity) of two objects, determining whether both variables point to the exact same object in memory, not merely having equal values.",
    "partB_realLife": "Suppose you and your friend both have the exact same book (same title, same pages, same price). Their contents are equal (==), but they are two separate physical copies in reality. If you both share one single book, then the book has the same identity ('is').",
    "partC_hinglish": "Ye exam ka ek favourite 1-mark question hai! '==' operator do variables ki VALUE check karta hai ki kya dono ke andar ek jaisi cheez hai. Jabki 'is' operator check karta hai ki kya dono variables memory mein EK HI OBJECT ko point kar rahe hain ya nahi. Python mein memory address dekhne ke liye id() function use hota hai.",
    "partD_examDef": "Identity operators (is and is not) compare the memory locations (object identity) of two objects to verify whether they point to the exact same memory address returned by id().",
    "partE_points": [
        "is: Returns True if both variables point to the same object in memory (id(a) == id(b)).",
        "is not: Returns True if both variables point to different objects in memory (id(a) != id(b)).",
        "id() function: Returns the unique integer memory address of an object.",
        "Difference from ==: '==' compares values/equality; 'is' compares memory references/identity."
    ],
    "partF_syntax": "x is y\nx is not y",
    "partG_example": "# Program demonstrating difference between '==' and 'is'\nlist1 = [1, 2, 3]\nlist2 = [1, 2, 3]\nlist3 = list1\n\nprint(\"list1 == list2:\", list1 == list2)     # True (same values)\nprint(\"list1 is list2:\", list1 is list2)     # False (different objects in memory)\nprint(\"list1 is list3:\", list1 is list3)     # True (both point to same memory)\nprint(\"list1 is not list2:\", list1 is not list2) # True",
    "partH_lineByLine": [
        "Line 1-2: list1 and list2 are created separately. Both have contents [1, 2, 3] but reside at different memory addresses.",
        "Line 3: list3 = list1 makes list3 refer directly to the existing list1 memory address.",
        "Line 5: list1 == list2 is True because contents are identical.",
        "Line 6: list1 is list2 is False because id(list1) != id(list2).",
        "Line 7: list1 is list3 is True because both point to the same memory location."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "list1 == list2", "action": "Compares [1,2,3] with [1,2,3]", "value": "True"},
        {"step": 2, "statement": "list1 is list2", "action": "Compares id(list1) with id(list2)", "value": "False"},
        {"step": 3, "statement": "list1 is list3", "action": "Compares same reference", "value": "True"}
    ],
    "partJ_output": "list1 == list2: True\nlist1 is list2: False\nlist1 is list3: True\nlist1 is not list2: True",
    "partK_mistakes": [
        "Assuming 'is' and '==' are identical. They are fundamentally different!",
        "Using 'is' to compare numbers or user input strings. Use '==' for value equality."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the difference between '==' and 'is' operator in Python?", "a": "'==' checks for value equality; 'is' checks whether two variables refer to the same object in memory."},
            {"q": "Which built-in function returns the memory address of an object?", "a": "id() function."}
        ],
        "shortAnswer": "Q: Explain identity operators with an example.\nAns: The identity operators are 'is' and 'is not'. They compare memory addresses: 'a is b' returns True if id(a) == id(b). Example: [1,2] is [1,2] evaluates to False.",
        "fourteenMark": "Q: What are Identity Operators in Python? Distinguish between identity and equality with diagrams, the role of id() function, and Python code examples."
    },
    "partM_revision": "is = True if same memory location (id(a) == id(b)). == = True if same value. is not = True if different memory locations."
})

# u1-t14: Operator Precedence & Associativity
notes.append({
    "id": "u1-t14",
    "unit": "Unit-I",
    "chapter": "Chapter 3: Operators",
    "title": "Operator Precedence & Associativity",
    "partA_intro": "When a single mathematical expression contains multiple operators (e.g., 10 + 2 * 3), operator precedence determines which operation is evaluated first. Associativity decides the order of evaluation when operators have the same precedence.",
    "partB_realLife": "Think of the BODMAS rule taught in school maths. Brackets are solved first, then Division, Multiplication, Addition, and Subtraction. Python follows a similar strict priority list.",
    "partC_hinglish": "Agar ek hi line mein plus, minus, multiply sab aa jaye, toh pehle kaun solve hoga? Ise 'Operator Precedence' kehte hain. Jaise '10 + 2 * 3' mein pehle 2 * 3 = 6 hoga, fir 10 + 6 = 16 banega (na ki 12 * 3 = 36). Python mein sabse zyada priority Parentheses (brackets) ki hoti hai. Jab do operators ki priority barabar hoti hai, toh unhe Left-to-Right solve karte hain (lekin Exponentiation ** Right-to-Left solve hota hai!).",
    "partD_examDef": "Operator precedence determines the order in which operators are evaluated in a compound expression. Operator associativity defines the direction (Left-to-Right or Right-to-Left) of evaluation when operators share equal precedence.",
    "partE_points": [
        "1. Parentheses (): Highest precedence of all. Always evaluated first.",
        "2. Exponentiation **: Second highest, evaluated Right-to-Left (e.g., 2 ** 3 ** 2 = 2 ** 9 = 512).",
        "3. Unary operators: +x, -x, ~x.",
        "4. Multiplication, Division, Floor Div, Modulus: *, /, //, % (Left-to-Right).",
        "5. Addition and Subtraction: +, - (Left-to-Right).",
        "6. Comparison operators: ==, !=, >, <, >=, <=, is, in.",
        "7. Logical not.",
        "8. Logical and.",
        "9. Logical or: Lowest precedence among logical operators.",
        "10. Assignment operators: =, +=, -=, etc. (Evaluated last, Right-to-Left)."
    ],
    "partF_syntax": "# Changing precedence using parentheses:\nresult1 = 10 + 5 * 2    # 20\nresult2 = (10 + 5) * 2  # 30",
    "partG_example": "# Program demonstrating operator precedence\nval1 = 10 + 2 * 5\nval2 = (10 + 2) * 5\nval3 = 2 ** 3 ** 2  # Evaluates as 2 ** (3 ** 2) = 2 ** 9\nval4 = 10 > 5 and 3 < 1 or 4 == 4\n\nprint(\"10 + 2 * 5 =\", val1)\nprint(\"(10 + 2) * 5 =\", val2)\nprint(\"2 ** 3 ** 2 =\", val3)\nprint(\"Logical evaluation =\", val4)",
    "partH_lineByLine": [
        "Line 1: * has higher precedence than +, so 2 * 5 = 10, then 10 + 10 = 20.",
        "Line 2: Parentheses () have highest precedence, so (10 + 2) = 12, then 12 * 5 = 60.",
        "Line 3: ** is right-associative, so 3 ** 2 = 9 first, then 2 ** 9 = 512.",
        "Line 4: Comparison first, then 'and', then 'or'. Result evaluates to True."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "10 + 2 * 5", "action": "Multiply 2*5=10, then add 10+10", "value": "20"},
        {"step": 2, "statement": "(10 + 2) * 5", "action": "Parentheses 12, then 12*5", "value": "60"},
        {"step": 3, "statement": "2 ** 3 ** 2", "action": "Right-to-left: 3**2=9, then 2**9", "value": "512"}
    ],
    "partJ_output": "10 + 2 * 5 = 20\n(10 + 2) * 5 = 60\n2 ** 3 ** 2 = 512\nLogical evaluation = True",
    "partK_mistakes": [
        "Assuming Left-to-Right for **: Calculating (2 ** 3) ** 2 = 64 instead of 2 ** (3 ** 2) = 512.",
        "Forgetting that 'and' has higher precedence than 'or'."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which operator has the highest precedence in Python?", "a": "Parentheses ()"},
            {"q": "What is the associativity of the exponentiation (**) operator?", "a": "Right-to-Left."}
        ],
        "shortAnswer": "Q: Evaluate the expression: 5 + 3 * 2 ** 2.\nAns: 1. 2 ** 2 = 4 (power first), 2. 3 * 4 = 12 (multiply next), 3. 5 + 12 = 17 (addition last). Result = 17.",
        "fourteenMark": "Q: What is operator precedence and associativity? Provide a complete hierarchy table of Python operators and evaluate three complex sample expressions step-by-step."
    },
    "partM_revision": "Precedence: () > ** > *, /, //, % > +, - > comparisons > not > and > or > assignment. ** is right-associative; most others are left-associative."
})

# Save Unit-I
os.makedirs("data", exist_ok=True)
with open("data/notes.json", "w", encoding="utf-8") as f:
    json.dump(notes, f, indent=2)

print(f"Generated {len(notes)} notes successfully.")

