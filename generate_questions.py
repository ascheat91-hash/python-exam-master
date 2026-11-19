import json

questions = []

# Helper to add question
def add_q(topic_id, unit, category, level, question, options, correct, explanation):
    questions.append({
        "id": f"q-{len(questions)+1}",
        "topicId": topic_id,
        "unit": unit,
        "category": category, # MCQ, FillBlank, TrueFalse, PredictOutput, ShortAnswer, Descriptive
        "level": level,       # Level 0, Level 1, Level 2, Level 3
        "question": question,
        "options": options,   # list or None
        "correct": correct,
        "explanation": explanation
    })

# UNIT-I: Chapter 1 Questions
add_q("u1-t1", "Unit-I", "MCQ", "Level 0", "Who is the creator of the Python programming language?", ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"], "Guido van Rossum", "Python was designed and created by Guido van Rossum and released in 1991.")
add_q("u1-t1", "Unit-I", "TrueFalse", "Level 0", "Python is an interpreted language that executes statements line-by-line.", ["True", "False"], "True", "Python translates and executes source code line-by-line using an interpreter.")
add_q("u1-t1", "Unit-I", "PredictOutput", "Level 1", "What will be the output of:\nprint('Python')\nprint('301')", None, "Python\n301", "Each print() statement by default ends with a newline character, displaying output on separate lines.")

add_q("u1-t2", "Unit-I", "MCQ", "Level 1", "Which of the following is a valid identifier name in Python?", ["2nd_score", "total-marks", "_student_age", "for"], "_student_age", "Identifiers can contain letters, numbers, and underscores, but cannot start with a digit, cannot contain hyphens, and cannot be keywords.")
add_q("u1-t2", "Unit-I", "MCQ", "Level 2", "Which 3 Python keywords start with a Capital letter?", ["if, else, while", "True, False, None", "int, float, str", "def, return, pass"], "True, False, None", "In Python 3, all reserved keywords are in lowercase except True, False, and None.")
add_q("u1-t2", "Unit-I", "FillBlank", "Level 1", "An identifier in Python cannot begin with a ________.", None, "digit", "Identifiers must begin with an alphabetic letter (a-z, A-Z) or an underscore (_).")

add_q("u1-t3", "Unit-I", "MCQ", "Level 0", "Which character is used to write a single-line comment in Python?", ["//", "/*", "#", "--"], "#", "Python uses the hash symbol (#) for single-line comments. (// is floor division in Python).")
add_q("u1-t3", "Unit-I", "TrueFalse", "Level 1", "Comments in Python are executed by the interpreter and affect the final program output.", ["True", "False"], "False", "Comments are non-executable statements completely ignored by the Python interpreter.")
add_q("u1-t3", "Unit-I", "PredictOutput", "Level 1", "What is the output of:\n# print('Hello')\nprint('Exam')\n# print('Python')", None, "Exam", "Lines beginning with '#' are ignored, so only 'Exam' is printed.")

add_q("u1-t4", "Unit-I", "MCQ", "Level 1", "What is the return data type of the input() function in Python?", ["int", "float", "str", "bool"], "str", "The input() function always reads and returns user input as a string (str).")
add_q("u1-t4", "Unit-I", "PredictOutput", "Level 2", "What is the output of:\nx = 10\ny = 20\nx, y = y, x\nprint(x, y)", None, "20 10", "Python supports tuple unpacking for swapping variables directly without a temporary variable.")
add_q("u1-t4", "Unit-I", "MCQ", "Level 2", "To read an integer from user in Python, which function call is used?", ["int(input())", "readInt()", "input.integer()", "cin >> x"], "int(input())", "int(input()) converts the string returned by input() into an integer.")

# UNIT-I: Chapter 2 Questions (Data Types)
add_q("u1-t5", "Unit-I", "MCQ", "Level 0", "Which built-in function is used to find the data type of an object in Python?", ["typeof()", "type()", "dataType()", "check()"], "type()", "The type() function returns the class type of an object.")
add_q("u1-t5", "Unit-I", "TrueFalse", "Level 1", "Python requires you to declare the data type of a variable before assigning a value to it.", ["True", "False"], "False", "Python is dynamically typed; data types are inferred implicitly upon assignment.")

add_q("u1-t6", "Unit-I", "MCQ", "Level 1", "What is the data type of the result of the expression: 10 / 2?", ["int", "float", "complex", "number"], "float", "In Python 3, the float division operator '/' always returns a float (5.0), even for exact divisions.")
add_q("u1-t6", "Unit-I", "PredictOutput", "Level 2", "What is the output of:\nz = 3 + 4j\nprint(z.imag)", None, "4.0", "The .imag attribute extracts the imaginary component of a complex number as a float (4.0).")
add_q("u1-t6", "Unit-I", "MCQ", "Level 1", "Which symbol represents the imaginary part in Python complex numbers?", ["i", "j", "k", "img"], "j", "Python uses 'j' or 'J' for the imaginary unit (e.g., 2 + 3j).")

add_q("u1-t7", "Unit-I", "MCQ", "Level 1", "What will be the output of: 'COLLEGE'[-1]?", ["C", "E", "G", "Error"], "E", "Negative index -1 accesses the very last character of a string, which is 'E'.")
add_q("u1-t7", "Unit-I", "TrueFalse", "Level 1", "Strings in Python are mutable and can be changed using s[0] = 'A'.", ["True", "False"], "False", "Strings are immutable. Trying to reassign a character raises a TypeError.")
add_q("u1-t7", "Unit-I", "PredictOutput", "Level 2", "What is the output of:\ns = 'PYTHON'\nprint(s[1:4])", None, "YTH", "Slicing s[1:4] extracts characters at indices 1, 2, and 3 ('Y', 'T', 'H'). Stop index 4 is excluded.")

add_q("u1-t8", "Unit-I", "MCQ", "Level 1", "What is the output of the arithmetic expression: True + True + False?", ["2", "1", "True", "Error"], "2", "In Python, True has integer value 1 and False has integer value 0. 1 + 1 + 0 = 2.")
add_q("u1-t8", "Unit-I", "MCQ", "Level 2", "What does bool(0) and bool(15) return in Python?", ["False, True", "True, False", "0, 15", "Error"], "False, True", "Numeric 0 evaluates to False; any non-zero number evaluates to True.")

# UNIT-I: Chapter 3 Questions (Operators)
add_q("u1-t9", "Unit-I", "PredictOutput", "Level 1", "What is the output of: print(11 // 3, 11 % 3)?", None, "3 2", "11 // 3 is floor division giving quotient 3; 11 % 3 gives remainder 2.")
add_q("u1-t9", "Unit-I", "PredictOutput", "Level 1", "What is the output of: print(2 ** 4)?", None, "16", "2 ** 4 means 2 raised to the power 4 (2*2*2*2 = 16).")
add_q("u1-t9", "Unit-I", "MCQ", "Level 2", "What is the result of 15 / 3 in Python 3?", ["5", "5.0", "3", "Error"], "5.0", "Division operator '/' always returns a floating point number in Python 3.")

add_q("u1-t10", "Unit-I", "MCQ", "Level 0", "Which operator is used to test for equality of two values?", ["=", "==", "===", "equals"], "==", "'==' compares two values. Single '=' is the assignment operator.")
add_q("u1-t10", "Unit-I", "PredictOutput", "Level 1", "What is the output of: print(10 >= 10)?", None, "True", "10 is equal to 10, so >= evaluates to True.")

add_q("u1-t11", "Unit-I", "MCQ", "Level 1", "Which of the following is NOT valid Python syntax?", ["x += 1", "x = x + 1", "x++", "x -= 1"], "x++", "Python does NOT have pre-increment or post-increment (++) operators.")
add_q("u1-t11", "Unit-I", "PredictOutput", "Level 2", "What is the output of:\na = 12\na //= 5\nprint(a)", None, "2", "a //= 5 is equivalent to a = 12 // 5, which results in integer 2.")

add_q("u1-t12", "Unit-I", "MCQ", "Level 1", "Which logical operator in Python returns True if at least one operand is True?", ["and", "or", "not", "xor"], "or", "The 'or' operator evaluates to True if any one operand is True.")
add_q("u1-t12", "Unit-I", "PredictOutput", "Level 2", "What is the output of: print(not (5 > 2 and 3 < 1))?", None, "True", "5 > 2 is True, 3 < 1 is False. True and False = False. not False = True.")

add_q("u1-t13", "Unit-I", "MCQ", "Level 2", "What do identity operators (is, is not) compare?", ["Values of operands", "Memory addresses of operands", "Data types only", "Variable names"], "Memory addresses of operands", "'is' checks whether two variables refer to the exact same memory location (id).")
add_q("u1-t13", "Unit-I", "PredictOutput", "Level 3", "What is the output of:\na = [1, 2]\nb = [1, 2]\nprint(a == b, a is b)", None, "True False", "a == b is True because values are identical; a is b is False because they are two distinct objects in memory.")

add_q("u1-t14", "Unit-I", "PredictOutput", "Level 2", "What is the output of: print(2 ** 3 ** 2)?", None, "512", "Exponentiation ** has right-to-left associativity: 3 ** 2 = 9, then 2 ** 9 = 512.")
add_q("u1-t14", "Unit-I", "PredictOutput", "Level 2", "What is the output of: print(10 + 4 * 2)?", None, "18", "Multiplication (*) has higher precedence than addition (+): 4 * 2 = 8; 10 + 8 = 18.")

# UNIT-II: Chapter 4 Questions (Conditionals)
add_q("u2-t1", "Unit-II", "MCQ", "Level 0", "In Python, which symbol is required at the end of an if condition header?", [";", ":", "{", "then"], ":", "Every compound header in Python (if, else, elif, while, for) must terminate with a colon (:).")
add_q("u2-t1", "Unit-II", "MCQ", "Level 1", "How does Python define a block of statements inside a condition?", ["Curly braces {}", "Parentheses ()", "Indentation (whitespace)", "Begin and End keywords"], "Indentation (whitespace)", "Python uses consistent indentation (usually 4 spaces) instead of brackets to delimit blocks.")

add_q("u2-t2", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\nx = 5\nif x < 10:\n    print('A')\nprint('B')", None, "A\nB", "5 < 10 is True, so 'A' prints. Then sequential statement 'B' prints.")

add_q("u2-t3", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\nnum = 9\nif num % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')", None, "Odd", "9 % 2 is 1 (not 0), so the condition is False and the else block executes.")
add_q("u2-t3", "Unit-II", "MCQ", "Level 1", "Can an 'else' statement have a test condition directly written with it?", ["Yes", "No", "Only if followed by 'if'", "Depends on Python version"], "No", "An 'else' statement never takes a condition. Use 'elif' if a condition is required.")

add_q("u2-t4", "Unit-II", "MCQ", "Level 1", "What is the keyword for 'else if' in Python?", ["elseif", "else if", "elif", "elsif"], "elif", "Python uses 'elif' as the keyword for else if.")
add_q("u2-t4", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nmarks = 75\nif marks > 90:\n    print('A')\nelif marks > 70:\n    print('B')\nelif marks > 60:\n    print('C')\nelse:\n    print('D')", None, "B", "The first condition evaluating to True is marks > 70, so 'B' prints and the remaining ladder is skipped.")

add_q("u2-t5", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\na, b = 10, 20\nif a > 5:\n    if b < 15:\n        print('One')\n    else:\n        print('Two')", None, "Two", "a > 5 is True, so execution enters inner if. b < 15 (20 < 15) is False, so inner else prints 'Two'.")

# UNIT-II: Chapter 5 Questions (Loops)
add_q("u2-t6", "Unit-II", "MCQ", "Level 1", "Why is the while loop referred to as an entry-controlled loop?", ["It controls program entry", "Condition is checked before executing loop body", "It can never be infinite", "It only executes once"], "Condition is checked before executing loop body", "In while loops, the condition is evaluated at the entry point before each execution.")
add_q("u2-t6", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\ni = 1\nwhile i < 4:\n    print(i, end=' ')\n    i += 1", None, "1 2 3 ", "i starts at 1, prints 1 2 3; when i becomes 4, condition 4 < 4 is False and loop terminates.")

add_q("u2-t7", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\ncount = 0\nfor x in 'EXAM':\n    count += 1\nprint(count)", None, "4", "The for loop iterates once for each character in 'EXAM' (4 iterations).")
add_q("u2-t7", "Unit-II", "MCQ", "Level 1", "Which keyword is used in Python to iterate through sequence members in a for loop?", ["in", "of", "range", "from"], "in", "The 'in' keyword connects the iteration variable to the sequence.")

add_q("u2-t8", "Unit-II", "MCQ", "Level 1", "What values are produced by the call range(1, 6)?", ["[1, 2, 3, 4, 5, 6]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4, 5]", "[2, 3, 4, 5, 6]"], "[1, 2, 3, 4, 5]", "The stop value in range() is always exclusive (stop-1), so range(1, 6) ends at 5.")
add_q("u2-t8", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nfor i in range(10, 0, -3):\n    print(i, end=' ')", None, "10 7 4 1 ", "Starts at 10, decreases by 3 each step: 10, 7, 4, 1 (next would be -2, which is <= 0 stop limit).")

add_q("u2-t9", "Unit-II", "PredictOutput", "Level 2", "How many total stars are printed by:\nfor i in range(2):\n    for j in range(3):\n        print('*', end='')", None, "******", "Outer loop runs 2 times, inner runs 3 times. Total stars = 2 * 3 = 6 stars.")

add_q("u2-t10", "Unit-II", "MCQ", "Level 1", "Which statement is used to terminate a loop completely and immediately?", ["continue", "break", "pass", "exit"], "break", "The 'break' statement terminates the enclosing loop immediately.")
add_q("u2-t10", "Unit-II", "MCQ", "Level 1", "Which statement skips only the current iteration of a loop and moves to the next?", ["continue", "break", "pass", "skip"], "continue", "The 'continue' statement bypasses remaining statements in the current iteration and begins the next.")
add_q("u2-t10", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nfor i in range(1, 6):\n    if i == 3:\n        continue\n    print(i, end=' ')", None, "1 2 4 5 ", "When i == 3, continue skips printing 3. All other values (1, 2, 4, 5) print normally.")
add_q("u2-t10", "Unit-II", "MCQ", "Level 1", "What is the function of the 'pass' statement in Python?", ["Skips to next iteration", "Exits the program", "Null statement that does nothing", "Terminates loop"], "Null statement that does nothing", "pass is a syntactic placeholder used when code is required syntactically but no action is needed.")

# UNIT-II: Chapter 6 Questions (Lists & Arrays)
add_q("u2-t11", "Unit-II", "MCQ", "Level 0", "Which brackets are used to create a list in Python?", ["()", "{}", "[]", "<>"], "[]", "Lists are defined using square brackets []. (Parentheses () are tuples, {} are dicts/sets).")
add_q("u2-t11", "Unit-II", "TrueFalse", "Level 0", "A Python list can hold items of different data types (heterogeneous).", ["True", "False"], "True", "Python lists can store integers, floats, strings, and booleans together in the same list.")

add_q("u2-t12", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\nnums = [10, 20, 30, 40, 50]\nprint(nums[1:4])", None, "[20, 30, 40]", "Slice nums[1:4] extracts elements from index 1 up to index 3 (stop index 4 is excluded).")
add_q("u2-t12", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\narr = [1, 2, 3, 4]\nprint(arr[::-1])", None, "[4, 3, 2, 1]", "Slice [::-1] with step -1 reverses the list.")

add_q("u2-t13", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\nx = [10, 20, 30]\nx[1] = 99\nprint(x)", None, "[10, 99, 30]", "Lists are mutable, so assigning to index 1 replaces 20 with 99.")
add_q("u2-t13", "Unit-II", "TrueFalse", "Level 1", "Python lists are immutable objects.", ["True", "False"], "False", "Lists are mutable; elements can be modified, appended, and deleted in place.")

add_q("u2-t14", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nitems = ['A', 'B', 'C']\nval = items.pop()\nprint(val, items)", None, "C ['A', 'B']", "pop() with no arguments removes and returns the last element ('C'), leaving ['A', 'B'].")
add_q("u2-t14", "Unit-II", "MCQ", "Level 2", "What is the difference between remove() and pop() for Python lists?", ["remove takes value, pop takes index", "remove takes index, pop takes value", "Both are identical", "pop cannot remove elements"], "remove takes value, pop takes index", "remove(x) searches and removes the first occurrence of value x; pop([i]) removes by index and returns it.")

add_q("u2-t15", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\nvals = [10, 5, 20]\nprint(min(vals), max(vals), sum(vals))", None, "5 20 35", "min() gives 5, max() gives 20, sum() calculates 10+5+20=35.")
add_q("u2-t15", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nscores = [40, 60]\nprint(sum(scores) / len(scores))", None, "50.0", "sum(scores) is 100, len is 2. 100 / 2 = 50.0 (float division).")

add_q("u2-t16", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nL = [1, 2]\nL.append([3, 4])\nprint(len(L))", None, "3", "append() adds its argument as a single element, so L becomes [1, 2, [3, 4]] with length 3.")
add_q("u2-t16", "Unit-II", "PredictOutput", "Level 2", "What is the output of:\nL = [1, 2]\nL.extend([3, 4])\nprint(len(L))", None, "4", "extend() iterates through [3, 4] and appends each element individually, making L = [1, 2, 3, 4] with length 4.")
add_q("u2-t16", "Unit-II", "PredictOutput", "Level 1", "What is the output of:\narr = [10, 20, 10, 30, 10]\nprint(arr.count(10))", None, "3", "count(10) returns the frequency of 10 in the list, which is 3.")

add_q("u2-t17", "Unit-II", "MCQ", "Level 1", "How are 1D arrays implemented in standard Python without external libraries?", ["Using linked lists", "Using Python lists", "Using tuples", "Using strings"], "Using Python lists", "Standard Python implements arrays conceptually using homogeneous lists.")

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Generated {len(questions)} comprehensive practice questions successfully.")

