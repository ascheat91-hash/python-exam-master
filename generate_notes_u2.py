import json

with open("data/notes.json", "r", encoding="utf-8") as f:
    notes = json.load(f)

# ==========================================
# UNIT - II : CHAPTER 4: CONDITIONAL STATEMENTS
# ==========================================

# u2-t1: Control Flow & Decision Making Concept
notes.append({
    "id": "u2-t1",
    "unit": "Unit-II",
    "chapter": "Chapter 4: Conditional Statements & Decision Making",
    "title": "Control Flow & Decision Making Concept",
    "partA_intro": "Control flow refers to the order in which individual statements or instructions in a program are executed. By default, programs execute sequentially line-by-line. Decision making (branching) allows a program to choose different paths of execution based on whether a condition is True or False.",
    "partB_realLife": "Imagine arriving at a road intersection. If the traffic light is GREEN, you drive forward. If the traffic light is RED, you stop. Your physical action depends on evaluating the real-world condition.",
    "partC_hinglish": "Normal code mein computer line 1, line 2, line 3 karke ek ke baad ek chalta hai (Sequential Flow). Lekin aisi situations hoti hain jahan hum chahte hain ki agar koi shart (condition) poori ho, tabhi koi line chale, warna skip ho jaye. Ise 'Decision Making' ya 'Control Flow' kehte hain. Python mein decision making ke liye 'Indentation' (spaces) ka sabse bada role hota hai.",
    "partD_examDef": "Control flow defines the sequential or conditional order in which programming statements are evaluated. Decision making statements alter this default linear execution by evaluating conditional Boolean expressions.",
    "partE_points": [
        "Sequential Flow: Default top-to-bottom line execution.",
        "Conditional Flow: Executing blocks of code only if a specific condition evaluates to True.",
        "Python Indentation: Unlike C/C++/Java that use curly braces '{ }', Python uses whitespace INDENTATION (typically 4 spaces) to define code blocks.",
        "Colon (:) Requirement: Every conditional header (if, else, elif) must end with a colon (:)."
    ],
    "partF_syntax": "if condition:\n    # Indented block executed when condition is True\n    statement_1\n    statement_2",
    "partG_example": "# Demonstration of conditional control flow\ntemp = 38\nprint(\"Checking temperature...\")\nif temp > 30:\n    print(\"It is a hot day!\")\nprint(\"Check completed.\")",
    "partH_lineByLine": [
        "Line 1: temp = 38 initializes temperature variable.",
        "Line 2: Prints 'Checking temperature...'.",
        "Line 3: if temp > 30: tests if 38 > 30 (True).",
        "Line 4: Because condition is True, indented line prints 'It is a hot day!'.",
        "Line 5: Unindented line runs regardless of the condition."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "temp = 38", "action": "Assigns 38", "value": "38"},
        {"step": 2, "statement": "temp > 30", "action": "38 > 30 evaluates to True", "value": "True"},
        {"step": 3, "statement": "print('It is a hot day!')", "action": "Executes indented block", "value": "Output printed"},
        {"step": 4, "statement": "print('Check completed.')", "action": "Executes sequential code", "value": "Output printed"}
    ],
    "partJ_output": "Checking temperature...\nIt is a hot day!\nCheck completed.",
    "partK_mistakes": [
        "Forgetting colon (:) at end of if statement: if x > 5 causes SyntaxError: expected ':'.",
        "Inconsistent Indentation: Mixing tabs and spaces or not indenting causes IndentationError."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What character is used in Python to indicate the start of an indented block?", "a": "Colon (:)."},
            {"q": "What does Python use instead of curly braces {} to define code blocks?", "a": "Indentation (whitespace)." }
        ],
        "shortAnswer": "Q: What is control flow? Explain the role of indentation in Python.\nAns: Control flow is the execution order of program instructions. Python uses uniform whitespace indentation to delimit blocks of statements following compound statements like if, while, and def.",
        "fourteenMark": "Q: What is control flow and decision making in Python? Explain the significance of indentation, relational conditions, and types of conditional statements with detailed flowcharts and examples."
    },
    "partM_revision": "Control flow = order of execution. Python uses 4-space indentation instead of {}. Always put a colon ':' after if/else/elif headers."
})

# u2-t2: Simple if Statement
notes.append({
    "id": "u2-t2",
    "unit": "Unit-II",
    "chapter": "Chapter 4: Conditional Statements & Decision Making",
    "title": "Simple if Statement",
    "partA_intro": "The simple if statement is the most basic decision-making construct. It executes an indented block of code only if a specified test condition evaluates to True. If the condition is False, the block is bypassed.",
    "partB_realLife": "Think of an umbrella rule: IF it is raining outside, open your umbrella. If it is not raining, do nothing and just keep walking.",
    "partC_hinglish": "Simple if statement sabse aasan hota hai. Ye kehta hai: 'Agar ye shart sach hai, toh ye kaam karo. Agar sach nahi hai, toh aage badh jao'. Agar condition False ho jati hai, toh if ke andar ka code chalta hi nahi hai aur program normal agli line par chala jata hai.",
    "partD_examDef": "The simple if statement evaluates a test expression. If the expression resolves to True, the statements inside the if block are executed; otherwise, they are skipped entirely.",
    "partE_points": [
        "Keywords: Uses the reserved keyword 'if'.",
        "Syntax format: if condition: followed by an indented block.",
        "One-way decision: It only specifies what to do when condition is True. It has no alternate branch if condition is False.",
        "Non-zero values in condition evaluate as True; 0 or None evaluate as False."
    ],
    "partF_syntax": "if condition:\n    statement_1\n    statement_2",
    "partG_example": "# Program to check if a student has passing marks\nmarks = 65\n\nif marks >= 35:\n    print(\"Congratulations!\")\n    print(\"You have passed the examination.\")\n\nprint(\"Evaluation complete.\")",
    "partH_lineByLine": [
        "Line 1: marks = 65 initializes the marks variable.",
        "Line 3: if marks >= 35: checks 65 >= 35 (evaluates to True).",
        "Line 4-5: Both indented lines execute because condition is True.",
        "Line 7: Out-of-block print executes sequentially."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "marks = 65", "action": "Assigns 65 to marks", "value": "65"},
        {"step": 2, "statement": "marks >= 35", "action": "65 >= 35 is True", "value": "True"},
        {"step": 3, "statement": "print('Congratulations!')", "action": "Executes inside if", "value": "Congratulations!"},
        {"step": 4, "statement": "print('You have passed...')", "action": "Executes inside if", "value": "You have passed..."},
        {"step": 5, "statement": "print('Evaluation complete.')", "action": "Next statement outside", "value": "Evaluation complete."}
    ],
    "partJ_output": "Congratulations!\nYou have passed the examination.\nEvaluation complete.",
    "partK_mistakes": [
        "Leaving the if block empty without a pass statement causes IndentationError: expected an indented block.",
        "Putting condition inside unnecessary brackets or forgetting the colon (:)."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What happens in a simple if statement when the condition is False?", "a": "The indented block is skipped and program execution continues with the next statement."},
            {"q": "Is the condition in an if statement required to be enclosed in parentheses in Python?", "a": "No, parentheses are optional."}
        ],
        "shortAnswer": "Q: Write the syntax and draw the flowchart for a simple if statement in Python.\nAns: Syntax: `if condition:` indented statements. Flowchart shows condition box branching to 'True -> Statement Block' and 'False -> Next Statement'.",
        "fourteenMark": "Q: Explain the simple if statement in Python with syntax, flowchart, dry-run table, and practical program examples."
    },
    "partM_revision": "if condition: runs code only when condition is True. If False, skips it. Indentation is mandatory."
})

# u2-t3: if-else Statement
notes.append({
    "id": "u2-t3",
    "unit": "Unit-II",
    "chapter": "Chapter 4: Conditional Statements & Decision Making",
    "title": "if-else Statement",
    "partA_intro": "The if-else statement provides a two-way decision branch. It executes one block of code if the test condition is True, and an alternative block of code under 'else' if the condition evaluates to False.",
    "partB_realLife": "Think of a coin toss: If it is HEADS, Team A bats. ELSE, Team B bats. Exactly one of the two outcomes will happen; you can never have both or neither.",
    "partC_hinglish": "if-else do-tarfa (two-way) decision ke liye hota hai: 'Agar condition sach hai toh if wala dabba chalao, WARNA (else) doosra dabba chalao'. if aur else dono mein se koi EK hi block hamesha chalega, dono kabhi ek sath nahi chal sakte. Exam ke liye note karein: else ke sath koi condition nahi likhi jati, sirf colon (:) lagta hai.",
    "partD_examDef": "The if-else statement evaluates a condition and executes the if block when True, or transfers control to the else block when False, ensuring one of two code blocks is always executed.",
    "partE_points": [
        "Two-way Branching: Guarantees execution of exactly one block.",
        "Keyword else: Must be written at the exact same indentation level as the corresponding if.",
        "No Condition for else: An else statement does NOT take a condition (e.g., else x < 10: is a SyntaxError).",
        "Colon Required: Both 'if condition:' and 'else:' must end with a colon (:)."
    ],
    "partF_syntax": "if condition:\n    # Executes if condition is True\n    statement_1\nelse:\n    # Executes if condition is False\n    statement_2",
    "partG_example": "# Program to check whether an entered number is Even or Odd\nnum = 17\n\nif num % 2 == 0:\n    print(num, \"is an EVEN number\")\nelse:\n    print(num, \"is an ODD number\")",
    "partH_lineByLine": [
        "Line 1: num = 17 stores 17.",
        "Line 3: num % 2 calculates remainder of 17 / 2, which is 1. 1 == 0 is False.",
        "Line 4: if block is skipped because condition was False.",
        "Line 5: else: is triggered.",
        "Line 6: Executes indented else block: prints '17 is an ODD number'."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "num = 17", "action": "Assigns 17", "value": "17"},
        {"step": 2, "statement": "17 % 2 == 0", "action": "1 == 0 evaluates to False", "value": "False"},
        {"step": 3, "statement": "else block", "action": "Executes else branch", "value": "Prints 17 is an ODD number"}
    ],
    "partJ_output": "17 is an ODD number",
    "partK_mistakes": [
        "Adding condition to else: writing 'else num < 10:' causes SyntaxError. (Use elif if you have a condition!).",
        "Mismatched Indentation: Putting 'else' at a different indentation level than its 'if'."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Can an 'else' block exist without a preceding 'if' statement?", "a": "No, an 'else' block must always follow an 'if' (or 'elif') statement."},
            {"q": "What will be the output if num = 10 for: if num > 10: print('A') else: print('B')?", "a": "B (since 10 > 10 is False)." }
        ],
        "shortAnswer": "Q: Write a Python program using if-else to find whether a student passed or failed (pass marks = 35).\nAns:\nmarks = int(input())\nif marks >= 35:\n    print('Pass')\nelse:\n    print('Fail')",
        "fourteenMark": "Q: Explain the if-else conditional statement in Python with syntax, flowchart, dry-run, and write a program to check whether a given year is a leap year."
    },
    "partM_revision": "if-else = two-way decision. If condition is True -> if block runs; if False -> else block runs. Never put a condition in else!"
})

# u2-t4: if-elif-else Ladder
notes.append({
    "id": "u2-t4",
    "unit": "Unit-II",
    "chapter": "Chapter 4: Conditional Statements & Decision Making",
    "title": "if-elif-else Ladder",
    "partA_intro": "The if-elif-else statement is a multi-way decision branch used when a program needs to test multiple conditions sequentially. 'elif' is Python's short form for 'else if'.",
    "partB_realLife": "Think of college grading: If marks >= 75 -> Distinction; Elif marks >= 60 -> First Division; Elif marks >= 50 -> Second Division; Elif marks >= 35 -> Third Division; Else -> Fail.",
    "partC_hinglish": "Jab hamare paas sirf do raste nahi, balki 3 ya usse zyada options hote hain (multi-way branching), tab hum 'elif' ladder ka use karte hain. Python mein 'else if' ko chhota karke 'elif' likha jata hai. Interpreter upar se pehli condition check karta hai; jo pehli condition True milti hai, sirf uska code chalata hai aur baaki poori ladder ko chhod kar bahar aa jata hai.",
    "partD_examDef": "The if-elif-else ladder evaluates multiple conditional expressions in top-down sequential order. As soon as one condition evaluates to True, its corresponding block executes and the rest of the ladder is bypassed.",
    "partE_points": [
        "Keyword elif: Python's unique contraction for 'else if'.",
        "Multi-way Decision: Allows testing as many conditions as needed.",
        "Short-circuit Exit: Only the first matching True block executes; subsequent elif conditions are not even evaluated.",
        "Optional Final else: Catches any cases where none of the if or elif conditions evaluated to True."
    ],
    "partF_syntax": "if condition_1:\n    block_1\nelif condition_2:\n    block_2\nelif condition_3:\n    block_3\nelse:\n    default_block",
    "partG_example": "# Program to assign student grade based on percentage\nmarks = 82\n\nif marks >= 90:\n    grade = \"A+\"\nelif marks >= 75:\n    grade = \"A\"\nelif marks >= 60:\n    grade = \"B\"\nelif marks >= 35:\n    grade = \"C\"\nelse:\n    grade = \"Fail\"\n\nprint(\"Marks:\", marks, \"| Grade:\", grade)",
    "partH_lineByLine": [
        "Line 1: marks = 82.",
        "Line 3: if marks >= 90: 82 >= 90 is False, moves to next elif.",
        "Line 5: elif marks >= 75: 82 >= 75 is True! grade = 'A' executes.",
        "Lines 7-11: All remaining elif and else blocks are skipped automatically.",
        "Line 13: Prints marks and calculated grade."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "marks >= 90", "action": "82 >= 90 is False", "value": "False"},
        {"step": 2, "statement": "marks >= 75", "action": "82 >= 75 is True (Match found)", "value": "True"},
        {"step": 3, "statement": "grade = 'A'", "action": "Executes matching elif", "value": "grade = 'A'"},
        {"step": 4, "statement": "Ladder skipped", "action": "Jumps to end of construct", "value": "Prints Result"}
    ],
    "partJ_output": "Marks: 82 | Grade: A",
    "partK_mistakes": [
        "Writing 'else if' instead of 'elif': Python does not recognize 'else if' as two words; you must write 'elif'.",
        "Wrong order of conditions: Testing marks >= 35 before marks >= 75 would make all students get 'C' grade because the first matching condition stops the ladder!"
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the keyword used in Python for 'else if'?", "a": "elif."},
            {"q": "Can an if-elif ladder have multiple elif blocks?", "a": "Yes, any number of elif blocks can be used."}
        ],
        "shortAnswer": "Q: Write the syntax of the if-elif-else ladder in Python.\nAns: \nif cond1:\n    stmt\nelif cond2:\n    stmt\nelse:\n    stmt",
        "fourteenMark": "Q: What is multi-way branching in Python? Explain the if-elif-else construct with a complete real-world marks-to-grade program, flowchart, and detailed execution dry run."
    },
    "partM_revision": "elif = else if in Python. Evaluates from top to bottom. As soon as one condition is True, executes it and ignores the rest."
})

# u2-t5: Nested if Statement
notes.append({
    "id": "u2-t5",
    "unit": "Unit-II",
    "chapter": "Chapter 4: Conditional Statements & Decision Making",
    "title": "Nested if Statement",
    "partA_intro": "A nested if statement is an if statement placed inside the body of another if (or else) statement. It is used when an action depends on multiple levels of sequential criteria.",
    "partB_realLife": "Think of an ATM machine: 1st condition: Is the ATM PIN correct? IF yes, only then 2nd condition is checked: Is Account Balance sufficient? If PIN itself is wrong, balance check never happens.",
    "partC_hinglish": "Nested if ka matlab hota hai 'ek if ke pet (body) ke andar doosra if rakhna'. Pehle bahar wala if check hoga. Agar bahar wala if True hoga, tabhi computer andar wale if ko check karega. Agar bahar wala hi False ho gaya, toh andar wale if ka darwaza khulega hi nahi! Isme indentation ka khaas khayal rakhna hota hai.",
    "partD_examDef": "A nested if statement occurs when an if, if-else, or if-elif block is placed within the body of another if or else block to evaluate hierarchical conditions.",
    "partE_points": [
        "Hierarchical Decisions: Handles multi-level dependent conditions.",
        "Deep Indentation: The inner if block is indented one level further inside the outer if block.",
        "Execution Rule: Inner condition is only tested if the outer condition evaluates to True.",
        "Can nest within both 'if' and 'else' blocks."
    ],
    "partF_syntax": "if outer_condition:\n    # Level 1\n    if inner_condition:\n        # Level 2\n        statement_inner\n    else:\n        statement_inner_else\nelse:\n    statement_outer_else",
    "partG_example": "# Program to check blood donation eligibility using nested if\nage = 21\nweight = 52\n\nif age >= 18:\n    if weight >= 50:\n        print(\"Eligible to donate blood.\")\n    else:\n        print(\"Not eligible: Weight must be at least 50 kg.\")\nelse:\n    print(\"Not eligible: Age must be at least 18 years.\")",
    "partH_lineByLine": [
        "Line 1-2: age = 21, weight = 52.",
        "Line 4: if age >= 18: 21 >= 18 is True, so execution enters the outer block.",
        "Line 5: Inner check if weight >= 50: 52 >= 50 is True.",
        "Line 6: Executes inner print: 'Eligible to donate blood.'.",
        "Lines 7-10: Respective inner and outer else blocks are ignored."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "age >= 18", "action": "21 >= 18 is True", "value": "Outer True"},
        {"step": 2, "statement": "weight >= 50", "action": "52 >= 50 is True", "value": "Inner True"},
        {"step": 3, "statement": "print('Eligible...')", "action": "Executes inner statement", "value": "Eligible to donate blood."}
    ],
    "partJ_output": "Eligible to donate blood.",
    "partK_mistakes": [
        "Indentation mismatch: If the inner if is not properly indented, Python treats it as a sequential statement outside the outer if.",
        "Excessive nesting: Nesting too deeply makes code difficult to read (often replaceable with logical 'and' operators)."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is meant by a 'nested' statement in Python?", "a": "A statement placed inside the body of another statement of the same kind."},
            {"q": "When does the inner if statement execute in a nested if block?", "a": "Only when the outer if condition evaluates to True."}
        ],
        "shortAnswer": "Q: Write a Python program using nested if to find the largest of three numbers (a, b, c).\nAns:\nif a >= b:\n    if a >= c:\n        largest = a\n    else:\n        largest = c\nelse:\n    if b >= c:\n        largest = b\n    else:\n        largest = c",
        "fourteenMark": "Q: What is nested if statement? Explain its syntax, indentation hierarchy, and write a complete program to find the greatest among three distinct numbers using nested if."
    },
    "partM_revision": "Nested if = an if inside another if. Inner if only evaluates if outer if is True. Keep indentation consistent."
})

# ==========================================
# UNIT - II : CHAPTER 5: LOOP STATEMENTS
# ==========================================

# u2-t6: while Loop with Counter & Condition
notes.append({
    "id": "u2-t6",
    "unit": "Unit-II",
    "chapter": "Chapter 5: Loop Statements & Branching",
    "title": "while Loop with Counter & Condition",
    "partA_intro": "A loop is used to execute a block of statements repeatedly as long as a specified condition remains True. The while loop is known as an 'entry-controlled loop' because the condition is checked at the very beginning before executing the loop body.",
    "partB_realLife": "Think of a tea vendor filling cups: WHILE there are empty cups on the tray, pour tea into the next cup. Stop pouring when there are no empty cups left.",
    "partC_hinglish": "Loop ka matlab hota hai kisi kaam ko baar-baar repeat karna. Agar aapko 1 se 100 tak ginti print karni hai, toh aap 100 baar print() nahi likhenge, balki ek loop chala denge. while loop tab tak chalta rehta hai jab tak uski condition True rehti hai. Isme 3 cheezein zaroori hoti hain:\n1. Initialization: Counter kahaan se shuru hoga (i = 1).\n2. Condition: Kahaan tak chalega (i <= 10).\n3. Increment/Update: Har round ke baad counter kitna badhega (i += 1). Agar update karna bhool gaye toh loop kabhi rukega hi nahi (Infinite Loop ban jayega!).",
    "partD_examDef": "A while loop is an entry-controlled iterative control structure in Python that repeatedly executes a target block of statements as long as the governing test condition evaluates to True.",
    "partE_points": [
        "Entry-Controlled: Condition is checked at the top before loop execution. If condition is False initially, loop body executes 0 times.",
        "Three Essential Parts: 1. Initialization (i = 1), 2. Condition (while i <= n:), 3. Update/Increment (i += 1).",
        "Infinite Loop Warning: If the condition never becomes False, the loop runs endlessly until memory runs out or user forces termination.",
        "Optional else with while: An else block attached to a while loop executes once when the loop condition becomes False naturally (not via break)."
    ],
    "partF_syntax": "counter = initial_value\nwhile condition:\n    # Loop body\n    statements\n    counter += step_value",
    "partG_example": "# Program to print numbers 1 to 5 and their sum using while loop\ni = 1\ntotal = 0\n\nwhile i <= 5:\n    print(\"Current number:\", i)\n    total += i\n    i += 1  # Increment counter\n\nprint(\"Final Sum:\", total)",
    "partH_lineByLine": [
        "Line 1-2: i is initialized to 1, total to 0.",
        "Line 4: while i <= 5 checks: 1 <= 5 (True).",
        "Line 5-7: Prints 1, adds to total (total=1), increments i to 2.",
        "Loop repeats for i = 2, 3, 4, 5.",
        "When i becomes 6, 6 <= 5 evaluates to False. Loop terminates.",
        "Line 9: Prints final sum (15)."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "i=1, total=0", "action": "1 <= 5 is True -> print 1, total=1, i=2", "value": "total=1, i=2"},
        {"step": 2, "statement": "i=2", "action": "2 <= 5 is True -> print 2, total=3, i=3", "value": "total=3, i=3"},
        {"step": 3, "statement": "i=3", "action": "3 <= 5 is True -> print 3, total=6, i=4", "value": "total=6, i=4"},
        {"step": 4, "statement": "i=4", "action": "4 <= 5 is True -> print 4, total=10, i=5", "value": "total=10, i=5"},
        {"step": 5, "statement": "i=5", "action": "5 <= 5 is True -> print 5, total=15, i=6", "value": "total=15, i=6"},
        {"step": 6, "statement": "i=6", "action": "6 <= 5 is False -> Loop terminates", "value": "Exits loop"}
    ],
    "partJ_output": "Current number: 1\nCurrent number: 2\nCurrent number: 3\nCurrent number: 4\nCurrent number: 5\nFinal Sum: 15",
    "partK_mistakes": [
        "Forgetting to increment the loop counter (e.g. leaving out i += 1): Causes an infinite loop that hangs the system.",
        "Off-by-one errors: Writing while i < 5 instead of while i <= 5 stops at 4 instead of 5."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Why is the while loop called an entry-controlled loop?", "a": "Because its condition is tested at the entry (beginning) before executing the loop body."},
            {"q": "What happens if the condition of a while loop is False at the very start?", "a": "The loop body is not executed even once (0 times)."}
        ],
        "shortAnswer": "Q: What is an infinite loop? Give an example using while loop.\nAns: An infinite loop never terminates because its condition always remains True. Example: while True: print('Hello').",
        "fourteenMark": "Q: What is a while loop in Python? Explain its components, syntax, flowchart, dry-run, and write a program to reverse a given integer number (e.g., 1234 -> 4321)."
    },
    "partM_revision": "while condition: checks condition before every turn. Requires initialization, condition, and increment (i += 1) to avoid infinite loop."
})

# u2-t7: for Loop & Iteration
notes.append({
    "id": "u2-t7",
    "unit": "Unit-II",
    "chapter": "Chapter 5: Loop Statements & Branching",
    "title": "for Loop & Iteration",
    "partA_intro": "The for loop in Python is used to iterate over the elements of any sequence (such as a string, list, tuple, or range). It automatically visits each element in order from start to finish without needing manual counter incrementation.",
    "partB_realLife": "Think of a postman delivering letters from his bag. He reaches into the bag, takes out letter #1 and delivers it, takes letter #2 and delivers it, and continues until the bag is empty. He doesn't need to manually count; the contents of the bag guide him.",
    "partC_hinglish": "C ya Java mein for loop mein teen cheezein likhni padti thi. Lekin Python ka for loop bilkul alag aur bahut aasan hai! Python ka for loop kisi sequence (jaise String, List, ya range) ke har item par ek-ek karke ghoomta hai. Isme aapko alag se 'i += 1' likhne ki zaroorat nahi hoti; Python apne aap agle item par badh jata hai. Isme 'in' keyword ka use hota hai.",
    "partD_examDef": "A for loop in Python is a collection-controlled iteration statement that traverses each item in any iterable sequence (such as a list, string, or range) in sequential order.",
    "partE_points": [
        "Sequence Traversal: Iterates through lists, strings, tuples, and ranges.",
        "Keyword 'in': Connects the iteration variable to the target sequence.",
        "Automatic Progression: Automatically moves to the next element on each iteration.",
        "No Index Out of Range: Eliminates off-by-one errors commonly associated with manual indexing.",
        "Optional else: Python's for loop can have an 'else' block that runs when the sequence is exhausted."
    ],
    "partF_syntax": "for variable in sequence:\n    # Indented loop body\n    statements",
    "partG_example": "# Program iterating over a string and a list using for loop\nprint(\"Iterating over String:\")\nfor ch in \"PY\":\n    print(\"Character:\", ch)\n\nprint(\"Iterating over List:\")\nmarks = [35, 42, 48]\nfor m in marks:\n    print(\"Mark:\", m)",
    "partH_lineByLine": [
        "Line 2: for ch in \"PY\": assigns 'P' to ch in round 1, then 'Y' in round 2.",
        "Line 3: Prints each character.",
        "Line 6: marks = [35, 42, 48] defines a list of 3 items.",
        "Line 7: for m in marks: sets m = 35, then m = 42, then m = 48.",
        "Line 8: Prints each mark sequentially."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "ch = 'P'", "action": "First character of 'PY'", "value": "'P' printed"},
        {"step": 2, "statement": "ch = 'Y'", "action": "Second character of 'PY'", "value": "'Y' printed"},
        {"step": 3, "statement": "m = 35", "action": "First element of marks", "value": "35 printed"},
        {"step": 4, "statement": "m = 42", "action": "Second element of marks", "value": "42 printed"},
        {"step": 5, "statement": "m = 48", "action": "Third element of marks", "value": "48 printed"}
    ],
    "partJ_output": "Iterating over String:\nCharacter: P\nCharacter: Y\nIterating over List:\nMark: 35\nMark: 42\nMark: 48",
    "partK_mistakes": [
        "Using a non-iterable with for loop: for i in 10: raises TypeError: 'int' object is not iterable (use range(10) instead).",
        "Modifying a list while iterating over it with a for loop can cause unexpected skipped items."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which keyword is used to iterate over a sequence in a for loop?", "a": "The 'in' keyword."},
            {"q": "Can a Python for loop iterate directly over characters in a string?", "a": "Yes, strings are iterable sequences."}
        ],
        "shortAnswer": "Q: Differentiate between while loop and for loop in Python.\nAns: while loop is condition-controlled (repeats while condition is True). for loop is collection-controlled (iterates through elements of a sequence/range).",
        "fourteenMark": "Q: What is a for loop in Python? Explain sequence iteration with strings and lists, comparison with while loop, syntax, dry-run, and write a program to count vowels in a given string."
    },
    "partM_revision": "for item in sequence: automatically visits every element. Works with strings, lists, range(). No manual i += 1 required."
})

# u2-t8: range() Function
notes.append({
    "id": "u2-t8",
    "unit": "Unit-II",
    "chapter": "Chapter 5: Loop Statements & Branching",
    "title": "range() Function (start, stop, step)",
    "partA_intro": "The range() function is a built-in Python function that generates an immutable sequence of integers. It is the most commonly used tool for controlling how many times a for loop runs.",
    "partB_realLife": "Think of buying bus tickets numbered 1 to 10. You start at seat 1, finish before seat 11, and advance 1 seat at a time. If you only want odd seats, you step by 2 (1, 3, 5, 7, 9).",
    "partC_hinglish": "range() function numbers ki ek series (ginti) generate karta hai. Isme 3 parameters ho sakte hain: range(start, stop, step).\n1. start: Kahaan se shuru karna hai (Default = 0).\n2. stop: Kahaan RUKNA hai. SABSE BADA EXAM RULE: range hamesha 'stop - 1' tak hi chalta hai! Agar aapne range(1, 5) likha hai, toh ye 1, 2, 3, 4 tak hi chalega, 5 ko touch nahi karega.\n3. step: Kitne ka gap (jump) lena hai (Default = 1). Agar step -1 ho toh ulta (reverse) ginti chalti hai.",
    "partD_examDef": "The range() function is a built-in Python type that generates an immutable arithmetic progression of integers defined by three parameters: start, stop (exclusive), and step.",
    "partE_points": [
        "1 Argument: range(stop) -> starts at 0, steps by 1, ends at stop-1. E.g., range(4) generates 0, 1, 2, 3.",
        "2 Arguments: range(start, stop) -> starts at start, ends at stop-1. E.g., range(2, 6) generates 2, 3, 4, 5.",
        "3 Arguments: range(start, stop, step) -> steps by specified increment. E.g., range(1, 10, 2) generates 1, 3, 5, 7, 9.",
        "Negative Step: range(5, 0, -1) generates countdown: 5, 4, 3, 2, 1.",
        "Memory Efficient: Generates numbers on demand (lazy evaluation), saving memory."
    ],
    "partF_syntax": "range(stop)\nrange(start, stop)\nrange(start, stop, step)",
    "partG_example": "# Demonstration of 1, 2, and 3 argument forms of range()\nprint(\"1-arg range(3):\")\nfor i in range(3):\n    print(i, end=\" \")\n\nprint(\"\n2-arg range(2, 6):\")\nfor i in range(2, 6):\n    print(i, end=\" \")\n\nprint(\"\n3-arg range(10, 0, -2):\")\nfor i in range(10, 0, -2):\n    print(i, end=\" \")",
    "partH_lineByLine": [
        "Line 2-4: range(3) produces 0, 1, 2 (stop is 3, so ends at 3-1=2).",
        "Line 6-8: range(2, 6) starts at 2 and produces 2, 3, 4, 5.",
        "Line 10-12: range(10, 0, -2) starts at 10, decreases by 2 each round: 10, 8, 6, 4, 2."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "range(3)", "action": "Generates sequence", "value": "0, 1, 2"},
        {"step": 2, "statement": "range(2, 6)", "action": "Starts at 2, ends at 5", "value": "2, 3, 4, 5"},
        {"step": 3, "statement": "range(10, 0, -2)", "action": "Steps backwards by 2", "value": "10, 8, 6, 4, 2"}
    ],
    "partJ_output": "1-arg range(3):\n0 1 2 \n2-arg range(2, 6):\n2 3 4 5 \n3-arg range(10, 0, -2):\n10 8 6 4 2 ",
    "partK_mistakes": [
        "Expecting range(1, 5) to include 5: Stop value is ALWAYS exclusive (n-1).",
        "Providing step 0: range(1, 5, 0) raises ValueError: range() arg 3 must not be zero."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What integers are generated by range(2, 7)?", "a": "2, 3, 4, 5, 6."},
            {"q": "What is the default start value and step value of range() if omitted?", "a": "Default start = 0, default step = 1."}
        ],
        "shortAnswer": "Q: Explain the three parameters of the range() function in Python.\nAns: 1. start (inclusive initial value), 2. stop (exclusive upper/lower limit), 3. step (difference between consecutive values)." ,
        "fourteenMark": "Q: Explain the range() function in Python with all three variations of syntax. Discuss negative stepping, memory advantages, and write a program to calculate the factorial of a number using for loop and range()."
    },
    "partM_revision": "range(start, stop, step) generates integer sequences. Stop value is EXCLUDED (runs up to stop-1). Default start = 0, default step = 1."
})

# u2-t9: Nested Loops
notes.append({
    "id": "u2-t9",
    "unit": "Unit-II",
    "chapter": "Chapter 5: Loop Statements & Branching",
    "title": "Nested Loops",
    "partA_intro": "A nested loop is a loop inside the body of another loop. The 'outer loop' controls the number of complete cycles, and for each single iteration of the outer loop, the 'inner loop' executes completely from start to finish.",
    "partB_realLife": "Think of an analog wall clock: For every single hour that passes (outer loop), the minute hand must complete a full 60-minute circle (inner loop).",
    "partC_hinglish": "Nested loop ka matlab hota hai 'loop ke andar doosra loop'. Bahar wale loop ko 'Outer Loop' aur andar wale ko 'Inner Loop' kehte hain. Rule ye hai ki jab bahar wala loop 1 baar chalta hai, toh andar wala loop apni poori ginti khatam karta hai. College exam mein 'Pattern printing' (jaise stars * ya numbers ke triangle) ke 14-marks ke question nested loop se hi aate hain!",
    "partD_examDef": "A nested loop is a loop structure where one loop (inner loop) is contained entirely inside the body of another loop (outer loop). The inner loop completes all its iterations for each single iteration of the outer loop.",
    "partE_points": [
        "Total Iterations: Equal to (Outer loop iterations) * (Inner loop iterations).",
        "Common Use: Matrix operations, multi-dimensional lists, and geometric/star pattern printing.",
        "Indentation Hierarchy: Inner loop must be indented inside the outer loop body.",
        "Any combination: Can nest for inside for, while inside while, or while inside for."
    ],
    "partF_syntax": "for i in range(outer_limit):\n    for j in range(inner_limit):\n        # Inner loop statements\n        statements",
    "partG_example": "# Program to print a right-angled star pattern using nested for loops\nrows = 4\n\nfor i in range(1, rows + 1):\n    for j in range(1, i + 1):\n        print(\"*\", end=\" \")\n    print()  # Newline after inner loop completes",
    "partH_lineByLine": [
        "Line 1: rows = 4 sets 4 rows to print.",
        "Line 3: for i in range(1, 5): outer loop runs for i = 1, 2, 3, 4.",
        "Line 4: for j in range(1, i + 1): inner loop runs from 1 to i stars.",
        "Line 5: print(\"*\", end=\" \") prints star on the same line.",
        "Line 6: print() drops down to the next row after inner loop finishes."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "i = 1", "action": "Inner loop j runs 1 to 1 -> prints 1 star", "value": "*"},
        {"step": 2, "statement": "i = 2", "action": "Inner loop j runs 1 to 2 -> prints 2 stars", "value": "* *"},
        {"step": 3, "statement": "i = 3", "action": "Inner loop j runs 1 to 3 -> prints 3 stars", "value": "* * *"},
        {"step": 4, "statement": "i = 4", "action": "Inner loop j runs 1 to 4 -> prints 4 stars", "value": "* * * *"}
    ],
    "partJ_output": "* \n* * \n* * * \n* * * * ",
    "partK_mistakes": [
        "Using the same loop variable name for both outer and inner loops (e.g. for i in ... inside for i in ... overrides the outer counter).",
        "Forgetting print() at the end of outer loop causing all output to print on one horizontal line."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "If an outer loop runs 3 times and an inner loop runs 4 times, how many total times does the inner loop body execute?", "a": "12 times (3 * 4 = 12)."},
            {"q": "Can a while loop be nested inside a for loop in Python?", "a": "Yes, loops of different types can be freely nested."}
        ],
        "shortAnswer": "Q: What is a nested loop? Give an example of a 2x2 grid output.\nAns: A loop inside another loop. Example:\nfor i in range(2):\n    for j in range(2):\n        print(i, j)",
        "fourteenMark": "Q: What is a nested loop in Python? Explain how outer and inner loops synchronize. Write Python programs to print: (a) a number triangle pattern and (b) a multiplication table from 1 to 5."
    },
    "partM_revision": "Nested loop = loop inside a loop. For each 1 step of outer loop, inner loop runs completely. Essential for pattern printing."
})

# u2-t10: Branching Statements: break, continue, pass
notes.append({
    "id": "u2-t10",
    "unit": "Unit-II",
    "chapter": "Chapter 5: Loop Statements & Branching",
    "title": "Branching Statements: break, continue, pass",
    "partA_intro": "Branching (jump) statements are used to alter the standard execution flow of loops. Python provides three key jump statements: break (terminates loop), continue (skips to next iteration), and pass (null placeholder).",
    "partB_realLife": "1. break: Emergency brake on a train. When pulled, train stops immediately.\n2. continue: Skipping a song in a playlist you dislike to go directly to the next song.\n3. pass: An empty cardboard box reserved on a shelf to put items into later.",
    "partC_hinglish": "Exam ke 1-mark aur short notes ke liye ye teen statements SABSE IMPORTANT hain:\n1. break: Loop ko TURANT KHATAM kar deta hai aur loop ke bahar fek deta hai.\n2. continue: Sirf CURRENT round (iteration) ko wahi chhod deta hai aur TURANT AGLI round par chala jata hai (loop khatam nahi hota, bas wo ek round skip hota hai).\n3. pass: Ye ek 'khali' (null) statement hai. Python mein code blocks ko khali nahi chhod sakte warna error aata hai. Agar aapko koi loop ya if baad mein likhna hai, toh aap wahan 'pass' likh dete hain taaki koi error na aaye.",
    "partD_examDef": "Branching statements alter loop execution: 'break' terminates the nearest enclosing loop immediately; 'continue' abandons the current iteration and jumps to the next; 'pass' is a null syntactic placeholder that performs no operation.",
    "partE_points": [
        "break: Immediately exits the loop, transferring control to the statement directly after the loop block.",
        "continue: Bypasses remaining statements in current loop cycle and advances to the next iteration.",
        "pass: Null statement; executed by interpreter as a NO-OP (no operation). Used to prevent IndentationError on empty blocks.",
        "break and else: When a loop terminates via 'break', its optional 'else' block is NOT executed."
    ],
    "partF_syntax": "# break\nwhile condition:\n    if stop_cond:\n        break\n\n# continue\nfor i in seq:\n    if skip_cond:\n        continue\n\n# pass\ndef future_code():\n    pass",
    "partG_example": "# Program demonstrating break, continue, and pass\nprint(\"Demonstrating break (stops at 3):\")\nfor i in range(1, 6):\n    if i == 3:\n        break\n    print(i, end=\" \")\n\nprint(\"\n\nDemonstrating continue (skips 3):\")\nfor i in range(1, 6):\n    if i == 3:\n        continue\n    print(i, end=\" \")\n\nprint(\"\n\nDemonstrating pass:\")\nfor i in range(1, 4):\n    if i == 2:\n        pass  # Placeholder, does nothing\n    print(i, end=\" \")",
    "partH_lineByLine": [
        "Line 3-6: When i == 3, break executes. Loop immediately terminates. Only 1, 2 are printed.",
        "Line 9-12: When i == 3, continue executes. print(i) is skipped for 3, and loop moves to 4. Prints 1 2 4 5.",
        "Line 15-18: When i == 2, pass runs (does nothing). All 1 2 3 are printed."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "break at i=3", "action": "Immediately stops loop", "value": "1 2"},
        {"step": 2, "statement": "continue at i=3", "action": "Skips i=3, resumes at i=4", "value": "1 2 4 5"},
        {"step": 3, "statement": "pass at i=2", "action": "Executes NO-OP", "value": "1 2 3"}
    ],
    "partJ_output": "Demonstrating break (stops at 3):\n1 2 \n\nDemonstrating continue (skips 3):\n1 2 4 5 \n\nDemonstrating pass:\n1 2 3 ",
    "partK_mistakes": [
        "Confusing break with continue: break KILLS the entire loop; continue only SKIPS the current turn.",
        "Assuming pass skips to the next iteration: pass does NOT skip anything! It simply does nothing and moves to the next line."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which statement is used to terminate a loop completely in Python?", "a": "The 'break' statement."},
            {"q": "What is the purpose of the 'pass' statement in Python?", "a": "It acts as a syntactic placeholder that performs no operation (null statement)."}
        ],
        "shortAnswer": "Q: Distinguish between 'break' and 'continue' statements with examples.\nAns: 'break' terminates loop completely, jumping outside. 'continue' skips remaining lines of current iteration and proceeds to next iteration.",
        "fourteenMark": "Q: What are jump/branching statements in Python? Explain break, continue, and pass in detail with syntax, flowcharts, difference table, and practical code examples."
    },
    "partM_revision": "break = exit loop immediately. continue = skip current turn and start next turn. pass = empty placeholder (does nothing)."
})

# ==========================================
# UNIT - II : CHAPTER 6: LISTS & ARRAYS
# ==========================================

# u2-t11: Creating Lists & Memory Representation
notes.append({
    "id": "u2-t11",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Creating Lists & Memory Representation",
    "partA_intro": "A list in Python is an ordered, mutable (changeable) collection of items enclosed in square brackets [ ]. Lists can store elements of mixed data types (integers, strings, floats, booleans) together.",
    "partB_realLife": "Think of a student's pencil pouch. It contains a pen, pencil, eraser, sharpener, and scale. You can add new stationery, remove an eraser, or replace a blue pen with a black pen anytime.",
    "partC_hinglish": "List Python ka sabse popular aur powerful data type hai. Isko Square Brackets [ ] ke andar comma laga kar likha jata hai. Jaise: marks = [40, 55, 62]. C language ke arrays mein sirf ek hi type ka data aa sakta tha, lekin Python ki List itni versatile hai ki isme ek sath number, string, float sab kuch store ho sakta hai (jaise: [101, 'Neha', 82.5, True]). Ek aur khaas baat: List 'Mutable' hoti hai, yaani banne ke baad iski values ko badla ja sakta hai.",
    "partD_examDef": "A list is an ordered, mutable sequence of heterogeneous elements enclosed in square brackets [ ], separated by commas. It supports dynamic resizing and element modification in place.",
    "partE_points": [
        "Enclosed in Square Brackets [ ]: e.g., numbers = [10, 20, 30].",
        "Heterogeneous: Can contain items of different data types together in one list.",
        "Ordered Sequence: Elements maintain the exact order in which they were inserted.",
        "Mutable: You can modify, add, or delete elements in-place without creating a new list.",
        "list() Constructor: Can also create lists using list() function (e.g., list('ABC') -> ['A', 'B', 'C'])."
    ],
    "partF_syntax": "empty_list = []\nhomogeneous_list = [1, 2, 3, 4, 5]\nmixed_list = [101, \"Rohan\", 78.5, True]",
    "partG_example": "# Program to demonstrate creating various types of lists\nempty = []\nintegers = [10, 20, 30]\nstudent = [101, \"Simran\", 89.5, True]\n\nprint(\"Empty list:\", empty)\nprint(\"Integer list:\", integers)\nprint(\"Heterogeneous list:\", student)\nprint(\"Type of student:\", type(student))\nprint(\"Total elements:\", len(student))",
    "partH_lineByLine": [
        "Line 1: Creates an empty list [].",
        "Line 2: Creates a list of integers.",
        "Line 3: Creates a list containing an int, string, float, and boolean.",
        "Lines 5-7: Displays the lists.",
        "Line 8: type(student) confirms <class 'list'>.",
        "Line 9: len(student) returns 4 items."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "empty = []", "action": "Creates list with 0 elements", "value": "[]"},
        {"step": 2, "statement": "student = [101, 'Simran', 89.5, True]", "action": "Creates heterogeneous list", "value": "List of 4 elements"},
        {"step": 3, "statement": "len(student)", "action": "Calculates total items", "value": "4"}
    ],
    "partJ_output": "Empty list: []\nInteger list: [10, 20, 30]\nHeterogeneous list: [101, 'Simran', 89.5, True]\nType of student: <class 'list'>\nTotal elements: 4",
    "partK_mistakes": [
        "Using round brackets instead of square brackets: (1, 2, 3) creates a TUPLE, not a list!",
        "Confusing Lists with C arrays: Assuming lists can only store one data type."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Which brackets are used to define a list in Python?", "a": "Square brackets [ ]."},
            {"q": "Are Python lists mutable or immutable?", "a": "Mutable (can be modified in-place)."}
        ],
        "shortAnswer": "Q: What is a heterogeneous list in Python? Give an example.\nAns: A list containing elements of different data types. Example: data = [1, 'Amit', 75.6, True].",
        "fourteenMark": "Q: What is a List in Python? Explain list creation, characteristics, memory representation of references, and differentiate between Python lists and traditional C arrays."
    },
    "partM_revision": "List = ordered, mutable sequence in square brackets []. Can hold mixed types (heterogeneous). len(L) gives count."
})

# u2-t12: Accessing Elements (Indexing & Slicing)
notes.append({
    "id": "u2-t12",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Accessing Elements (Positive & Negative Indexing, Slicing)",
    "partA_intro": "Individual elements in a list are accessed using their numeric position called an index. Python supports both Positive Indexing (0, 1, 2...) from the left and Negative Indexing (-1, -2...) from the right. Slicing extracts a subset of elements.",
    "partB_realLife": "Think of numbered lockers in a bank. Locker 0 is the first locker, Locker 1 is the second. If you stand at the very end of the row, the last locker is -1.",
    "partC_hinglish": "List ke items ko nikalne ke liye unka Index use karte hain. Index hamesha 0 se start hota hai. Python mein Negative indexing bhi hoti hai: list[-1] ka matlab aakhiri element. Agar ek sath kayi items ka tukda nikalna ho, toh 'Slicing' use karte hain: list[start : stop]. Yaad rakhein ki Slicing mein bhi 'stop' index shamil nahi hota, stop-1 tak hi nikalta hai!",
    "partD_examDef": "List elements are accessed using zero-based positive indexing from left to right, or negative indexing starting at -1 from right to left. Slicing retrieves a sub-list using the syntax list[start:stop:step].",
    "partE_points": [
        "Positive Index: 0 to len-1 (Left-to-right).",
        "Negative Index: -1 to -len (Right-to-left, -1 is last element).",
        "Slicing Syntax: list[start : stop : step] where stop is EXCLUSIVE.",
        "Omitting start: list[:3] extracts from beginning up to index 2.",
        "Omitting stop: list[2:] extracts from index 2 to the very end.",
        "Reverse slicing: list[::-1] reverses the entire list in one step!"
    ],
    "partF_syntax": "element = my_list[index]\nsub_list = my_list[start : stop : step]",
    "partG_example": "# Program demonstrating indexing and slicing in lists\ncolors = [\"Red\", \"Green\", \"Blue\", \"Yellow\", \"Orange\"]\n\nprint(\"First color (index 0):\", colors[0])\nprint(\"Last color (index -1):\", colors[-1])\nprint(\"Slice [1:4]:\", colors[1:4])\nprint(\"Slice from start [:3]:\", colors[:3])\nprint(\"Reversed list [::-1]:\", colors[::-1])",
    "partH_lineByLine": [
        "Line 1: colors has 5 items at indices 0, 1, 2, 3, 4.",
        "Line 3: colors[0] accesses 'Red'.",
        "Line 4: colors[-1] accesses rightmost 'Orange'.",
        "Line 5: colors[1:4] extracts indices 1, 2, 3 (['Green', 'Blue', 'Yellow']).",
        "Line 6: colors[:3] extracts indices 0, 1, 2 (['Red', 'Green', 'Blue']).",
        "Line 7: colors[::-1] steps backwards, reversing the entire list."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "colors[0]", "action": "Lookup index 0", "value": "'Red'"},
        {"step": 2, "statement": "colors[-1]", "action": "Lookup index -1", "value": "'Orange'"},
        {"step": 3, "statement": "colors[1:4]", "action": "Indices 1, 2, 3", "value": "['Green', 'Blue', 'Yellow']"},
        {"step": 4, "statement": "colors[::-1]", "action": "Full reverse slice", "value": "['Orange', 'Yellow', 'Blue', 'Green', 'Red']"}
    ],
    "partJ_output": "First color (index 0): Red\nLast color (index -1): Orange\nSlice [1:4]: ['Green', 'Blue', 'Yellow']\nSlice from start [:3]: ['Red', 'Green', 'Blue']\nReversed list [::-1]: ['Orange', 'Yellow', 'Blue', 'Green', 'Red']",
    "partK_mistakes": [
        "Index out of range: Accessing colors[5] when length is 5 causes IndexError: list index out of range.",
        "Expecting stop index to be included: colors[1:3] only gives indices 1 and 2, NOT 3."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the index of the first and last elements in a Python list of size N?", "a": "First element = 0; Last element = N-1 (or -1 using negative indexing)."},
            {"q": "What will be the output of: [10, 20, 30, 40][1:3]?", "a": "[20, 30]."}
        ],
        "shortAnswer": "Q: Explain list slicing with the syntax list[start:stop:step] and an example.\nAns: Slicing extracts a sublist. `nums = [1, 2, 3, 4, 5]`; `nums[1:4]` returns `[2, 3, 4]` (from index 1 up to index 4-1=3).",
        "fourteenMark": "Q: Explain indexing and slicing mechanisms in Python lists with diagrams. Provide examples of positive indexing, negative indexing, step slicing, and reversing lists."
    },
    "partM_revision": "Index 0 = first item. Index -1 = last item. Slicing: L[start:stop] stops at stop-1. L[::-1] reverses list."
})

# u2-t13: Updating Elements & List Mutability
notes.append({
    "id": "u2-t13",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Updating Elements & List Mutability",
    "partA_intro": "Mutability means that an object's contents can be changed in-place after creation without changing its memory address. Lists in Python are mutable, meaning you can update existing items by assigning new values to specific indices.",
    "partB_realLife": "Think of a whiteboard in a classroom. If a teacher writes 'Maths Period 1', she can wipe off 'Maths' and write 'Science' on the exact same board without buying a new whiteboard.",
    "partC_hinglish": "String immutable thi (badal nahi sakti thi), lekin List 'Mutable' hoti hai. Iska matlab hai ki aap list ke kisi bhi item ko direct update kar sakte hain, jaise: marks[0] = 95. Aisa karne se purani value hat kar nayi value aa jati hai aur list ka memory address wahi rehta hai. Aap ek sath kayi items ko slice ke zariye bhi update kar sakte hain.",
    "partD_examDef": "List mutability is the capability of list objects to have their elements modified, replaced, or updated in place through index assignment without creating a new list object in memory.",
    "partE_points": [
        "In-place Modification: Modifies the original list directly (id(list) remains identical).",
        "Index Assignment: list[index] = new_value.",
        "Slice Assignment: Can replace multiple elements at once: list[1:3] = [50, 60].",
        "Difference from Strings: Strings are immutable (s[0]='A' raises error); Lists are mutable (L[0]='A' succeeds)."
    ],
    "partF_syntax": "my_list[index] = new_value\nmy_list[start:stop] = [val1, val2]",
    "partG_example": "# Program demonstrating list updating and mutability\nfruits = [\"Apple\", \"Banana\", \"Cherry\"]\nprint(\"Before update:\", fruits)\n\n# Updating single element at index 1\nfruits[1] = \"Mango\"\nprint(\"After single update:\", fruits)\n\n# Updating via slice\nfruits[0:2] = [\"Orange\", \"Grapes\"]\nprint(\"After slice update:\", fruits)",
    "partH_lineByLine": [
        "Line 1: fruits = [\"Apple\", \"Banana\", \"Cherry\"].",
        "Line 4: fruits[1] = \"Mango\" overwrites 'Banana' with 'Mango'.",
        "Line 7: fruits[0:2] = [\"Orange\", \"Grapes\"] replaces first two elements."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "fruits = ['Apple', 'Banana', 'Cherry']", "action": "Initial list", "value": "['Apple', 'Banana', 'Cherry']"},
        {"step": 2, "statement": "fruits[1] = 'Mango'", "action": "Replaces index 1", "value": "['Apple', 'Mango', 'Cherry']"},
        {"step": 3, "statement": "fruits[0:2] = ['Orange', 'Grapes']", "action": "Replaces slice 0:2", "value": "['Orange', 'Grapes', 'Cherry']"}
    ],
    "partJ_output": "Before update: ['Apple', 'Banana', 'Cherry']\nAfter single update: ['Apple', 'Mango', 'Cherry']\nAfter slice update: ['Orange', 'Grapes', 'Cherry']",
    "partK_mistakes": [
        "Trying to add a new item by assigning to a non-existent index: e.g. L = [1, 2]; L[2] = 3 raises IndexError. (Use append() to add new elements!).",
        "Confusing mutability with variable reassignment."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "Can list elements be changed in-place in Python?", "a": "Yes, because lists are mutable."},
            {"q": "What error occurs when executing: a = [1, 2]; a[5] = 10?", "a": "IndexError: list assignment index out of range."}
        ],
        "shortAnswer": "Q: Differentiate between mutable and immutable data types in Python with examples.\nAns: Mutable types can be altered in place (e.g. Lists, Dictionaries). Immutable types cannot be changed once created (e.g. Strings, Tuples, Integers).",
        "fourteenMark": "Q: What is list mutability? Explain element updating, slice replacement, in-place modifications, and contrast with string immutability with code and memory diagrams."
    },
    "partM_revision": "Lists are mutable. L[index] = new_value changes elements in-place. Cannot assign to out-of-range index (use append() instead)."
})

# u2-t14: Deleting Elements (del, pop, remove, clear)
notes.append({
    "id": "u2-t14",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Deleting Elements (del, pop, remove, clear)",
    "partA_intro": "Python provides multiple ways to delete elements from a list depending on whether you want to delete by index position, by element value, or empty the entire list.",
    "partB_realLife": "1. del: Tearing a page out of a register by its page number.\n2. pop: Taking a plate off the top of a stack to use it (returns the plate).\n3. remove: Erasing a specific misspelled student name from attendance list without knowing their roll number.\n4. clear: Rubbing the entire blackboard clean.",
    "partC_hinglish": "Exam mein list se item delete karne ke 4 tareeqe pooche jaate hain:\n1. del statement: Index ke hisaab se delete karta hai (jaise: del list[0]). Ye koi value wapas nahi deta.\n2. pop() method: Index ke hisaab se delete karta hai AUR delete hui value ko wapas (return) bhi karta hai. Agar bracket khali ho (pop()), toh aakhiri element delete karta hai.\n3. remove(value): Value ke hisaab se delete karta hai (jaise: list.remove('Apple')). Agar value list mein nahi hai, toh ValueError deta hai.\n4. clear(): Poori list ke saare items ek jhatke mein uda deta hai aur list ko khali [] bana deta hai.",
    "partD_examDef": "Python supports multiple deletion mechanisms for lists: 'del' statement removes items or slices by index; 'pop()' removes and returns an element at an index (defaulting to last); 'remove()' removes the first occurrence of a specified value; 'clear()' empties the list.",
    "partE_points": [
        "del keyword: del list[index] or del list[start:stop]. Not a method, it is a Python keyword statement.",
        "pop([index]) method: Removes and returns element. Default index is -1 (last element).",
        "remove(value) method: Searches for and removes first matching element by value. Raises ValueError if not found.",
        "clear() method: Removes all elements from the list, leaving it as an empty list []."
    ],
    "partF_syntax": "del my_list[index]\npopped_item = my_list.pop(index)\nmy_list.remove(value)\nmy_list.clear()",
    "partG_example": "# Program demonstrating all 4 methods of deleting elements from a list\nnums = [10, 20, 30, 40, 50, 60]\nprint(\"Original:\", nums)\n\n# 1. Using del statement\ndel nums[0]  # Deletes 10\nprint(\"After del nums[0]:\", nums)\n\n# 2. Using pop() method\nremoved_item = nums.pop()  # Removes and returns 60\nprint(\"After pop():\", nums, \"| Popped item:\", removed_item)\n\n# 3. Using remove() method\nnums.remove(30)  # Removes value 30\nprint(\"After remove(30):\", nums)\n\n# 4. Using clear() method\nnums.clear()\nprint(\"After clear():\", nums)",
    "partH_lineByLine": [
        "Line 1: nums = [10, 20, 30, 40, 50, 60].",
        "Line 5: del nums[0] deletes first element 10.",
        "Line 9: nums.pop() removes rightmost item 60 and returns it into removed_item.",
        "Line 13: nums.remove(30) searches for value 30 and deletes it.",
        "Line 17: nums.clear() wipes out all items, leaving []."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "del nums[0]", "action": "Deletes index 0 (10)", "value": "[20, 30, 40, 50, 60]"},
        {"step": 2, "statement": "nums.pop()", "action": "Removes last item 60", "value": "[20, 30, 40, 50]"},
        {"step": 3, "statement": "nums.remove(30)", "action": "Removes value 30", "value": "[20, 40, 50]"},
        {"step": 4, "statement": "nums.clear()", "action": "Empties list", "value": "[]"}
    ],
    "partJ_output": "Original: [10, 20, 30, 40, 50, 60]\nAfter del nums[0]: [20, 30, 40, 50, 60]\nAfter pop(): [20, 30, 40, 50] | Popped item: 60\nAfter remove(30): [20, 40, 50]\nAfter clear(): []",
    "partK_mistakes": [
        "Calling remove() with an element that doesn't exist: [1, 2].remove(5) raises ValueError: list.remove(x): x not in list.",
        "Calling pop() on an empty list: [].pop() raises IndexError: pop from empty list."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the difference between del and pop() in Python?", "a": "del only removes the item; pop() removes the item AND returns it."},
            {"q": "What happens when you execute pop() without passing an index argument?", "a": "It removes and returns the last element of the list."}
        ],
        "shortAnswer": "Q: Differentiate between remove() and pop() methods with examples.\nAns: remove(val) removes the item by its VALUE (e.g. L.remove(20)). pop(idx) removes and returns the item by its INDEX (e.g. L.pop(0)).",
        "fourteenMark": "Q: Explain all methods to remove elements from a list in Python (del, pop, remove, clear) with syntax, exceptions raised, and practical code examples."
    },
    "partM_revision": "del L[i] = delete by index. L.pop(i) = delete by index & return value. L.remove(val) = delete by value. L.clear() = make list empty."
})

# u2-t15: Built-in Functions for Lists
notes.append({
    "id": "u2-t15",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Built-in Functions for Lists (len, min, max, sum, sorted)",
    "partA_intro": "Built-in functions in Python can take a list as an argument to perform aggregate calculations, find extreme values, sort items, or count total elements.",
    "partB_realLife": "Think of a teacher grading 50 exam answer sheets. She counts how many sheets there are (len), finds the highest score (max), finds the lowest score (min), and calculates total marks obtained by all students (sum).",
    "partC_hinglish": "Python mein bane-banaye (built-in) functions hote hain jinme aap list pass karke ek second mein result nikal sakte hain:\n1. len(L): List mein kul kitne items hain (length).\n2. min(L): Sabse chhota number kaunsa hai.\n3. max(L): Sabse bada number kaunsa hai.\n4. sum(L): Saare numbers ka jod (total) kitna hai.\n5. sorted(L): Nayi sorted list return karta hai bina purani list ko chede.",
    "partD_examDef": "Built-in list functions are globally accessible functions in Python that accept list sequences as arguments to return aggregated statistics or transformed collections (e.g., len, min, max, sum, sorted).",
    "partE_points": [
        "len(list): Returns total number of elements.",
        "min(list): Returns smallest element in the list. (Elements must be comparable).",
        "max(list): Returns largest element in the list.",
        "sum(list): Calculates arithmetic total of all numeric elements in the list.",
        "sorted(list): Returns a NEW sorted list in ascending order without modifying original list."
    ],
    "partF_syntax": "length = len(my_list)\nsmallest = min(my_list)\nlargest = max(my_list)\ntotal = sum(my_list)\nordered = sorted(my_list)",
    "partG_example": "# Program demonstrating built-in functions on a numeric list\nscores = [45, 88, 32, 95, 60]\n\nprint(\"List:\", scores)\nprint(\"Total elements len():\", len(scores))\nprint(\"Lowest score min():\", min(scores))\nprint(\"Highest score max():\", max(scores))\nprint(\"Sum of scores sum():\", sum(scores))\nprint(\"Average:\", sum(scores) / len(scores))\nprint(\"Sorted list sorted():\", sorted(scores))",
    "partH_lineByLine": [
        "Line 1: scores contains [45, 88, 32, 95, 60].",
        "Line 4: len(scores) returns 5.",
        "Line 5: min(scores) scans and returns lowest value 32.",
        "Line 6: max(scores) scans and returns highest value 95.",
        "Line 7: sum(scores) calculates 45+88+32+95+60 = 320.",
        "Line 8: Calculates average: 320 / 5 = 64.0.",
        "Line 9: sorted(scores) returns [32, 45, 60, 88, 95]."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "len(scores)", "action": "Counts items", "value": "5"},
        {"step": 2, "statement": "min(scores)", "action": "Finds minimum", "value": "32"},
        {"step": 3, "statement": "max(scores)", "action": "Finds maximum", "value": "95"},
        {"step": 4, "statement": "sum(scores)", "action": "Adds all items", "value": "320"}
    ],
    "partJ_output": "List: [45, 88, 32, 95, 60]\nTotal elements len(): 5\nLowest score min(): 32\nHighest score max(): 95\nSum of scores sum(): 320\nAverage: 64.0\nSorted list sorted(): [32, 45, 60, 88, 95]",
    "partK_mistakes": [
        "Using sum() on list of strings: sum(['a', 'b']) raises TypeError: unsupported operand type for +: 'int' and 'str'.",
        "Using min() or max() on mixed list of strings and integers: raises TypeError '<' not supported between instances of 'str' and 'int'."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What will be the output of: sum([10, 20, 30]) / len([10, 20, 30])?", "a": "20.0 (average of elements)."},
            {"q": "Does the sorted() function modify the original list in memory?", "a": "No, it returns a new sorted list."}
        ],
        "shortAnswer": "Q: Write a Python program to find the largest, smallest, and average of a list of numbers.\nAns:\nnums = [12, 45, 67, 23]\nprint('Max:', max(nums))\nprint('Min:', min(nums))\nprint('Avg:', sum(nums)/len(nums))",
        "fourteenMark": "Q: Discuss built-in functions available for list processing in Python. Write a complete menu-driven program to perform length calculation, sum, average, min, max, and sorting."
    },
    "partM_revision": "len() = count. min() = lowest. max() = highest. sum() = total. sorted() = returns new sorted list."
})

# u2-t16: List Methods
notes.append({
    "id": "u2-t16",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "List Methods (append, insert, extend, reverse, index, count)",
    "partA_intro": "List methods are functions built directly into list objects that are invoked using dot notation (list.method()). They modify the list in place or provide information about list contents.",
    "partB_realLife": "Think of managing a line of people: append() adds someone to the very end of the line. insert() lets someone cut into the line at a specific position. extend() adds a whole group of people to the back. reverse() tells everyone to turn around 180 degrees.",
    "partC_hinglish": "Exam mein List Methods par 14 marks ka question aana lagbhag pakka hota hai! Dhyan se samjhein:\n1. append(x): List ke AAKHIR (end) mein ek naya item jodta hai.\n2. insert(index, x): Kisi bhi manpasand position par naya item ghusata hai.\n3. extend(list2): Doosri list ke saare items ko pehli list ke aakhir mein jod deta hai.\n4. reverse(): Poori list ko ulta kar deta hai in-place.\n5. index(x): Batata hai ki x pehli baar kis position par aaya hai.\n6. count(x): Ginta hai ki x list mein kul kitni baar aaya hai.",
    "partD_examDef": "List methods are built-in member functions invoked on list instances using dot notation to modify list state in place (append, insert, extend, sort, reverse) or query contents (index, count).",
    "partE_points": [
        "append(item): Appends item to the very end. Increases length by 1.",
        "insert(index, item): Inserts item before the specified index, shifting other elements right.",
        "extend(iterable): Appends elements of another list/sequence to the current list.",
        "reverse(): Reverses the elements of the list in place without returning anything (returns None).",
        "sort(): Sorts list in ascending order in place.",
        "index(item): Returns first index position where item appears.",
        "count(item): Returns the number of occurrences of item in the list."
    ],
    "partF_syntax": "my_list.append(item)\nmy_list.insert(index, item)\nmy_list.extend(another_list)\nmy_list.reverse()\npos = my_list.index(item)\nfreq = my_list.count(item)",
    "partG_example": "# Program demonstrating all key list methods\nitems = [\"Pen\", \"Book\", \"Pen\"]\n\n# 1. append()\nitems.append(\"Pencil\")\nprint(\"After append:\", items)\n\n# 2. insert()\nitems.insert(1, \"Eraser\")\nprint(\"After insert at 1:\", items)\n\n# 3. count() and index()\nprint(\"Count of 'Pen':\", items.count(\"Pen\"))\nprint(\"First index of 'Pen':\", items.index(\"Pen\"))\n\n# 4. extend()\nitems.extend([\"Scale\", \"Colors\"])\nprint(\"After extend:\", items)\n\n# 5. reverse()\nitems.reverse()\nprint(\"After reverse:\", items)",
    "partH_lineByLine": [
        "Line 1: items = [\"Pen\", \"Book\", \"Pen\"].",
        "Line 4: items.append(\"Pencil\") adds 'Pencil' at index 3.",
        "Line 8: items.insert(1, \"Eraser\") shifts 'Book' and places 'Eraser' at index 1.",
        "Line 12: items.count(\"Pen\") counts occurrences (2).",
        "Line 13: items.index(\"Pen\") finds first occurrence at 0.",
        "Line 16: items.extend([\"Scale\", \"Colors\"]) unpacks and appends both items.",
        "Line 20: items.reverse() inverts list in place."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "append('Pencil')", "action": "Adds at end", "value": "['Pen', 'Book', 'Pen', 'Pencil']"},
        {"step": 2, "statement": "insert(1, 'Eraser')", "action": "Inserts at index 1", "value": "['Pen', 'Eraser', 'Book', 'Pen', 'Pencil']"},
        {"step": 3, "statement": "count('Pen')", "action": "Counts 'Pen'", "value": "2"},
        {"step": 4, "statement": "extend([...])", "action": "Adds 2 items to end", "value": "7 items total"},
        {"step": 5, "statement": "reverse()", "action": "Reverses order", "value": "Reversed in-place"}
    ],
    "partJ_output": "After append: ['Pen', 'Book', 'Pen', 'Pencil']\nAfter insert at 1: ['Pen', 'Eraser', 'Book', 'Pen', 'Pencil']\nCount of 'Pen': 2\nFirst index of 'Pen': 0\nAfter extend: ['Pen', 'Eraser', 'Book', 'Pen', 'Pencil', 'Scale', 'Colors']\nAfter reverse: ['Colors', 'Scale', 'Pencil', 'Pen', 'Book', 'Eraser', 'Pen']",
    "partK_mistakes": [
        "Difference between append and extend: L.append([1, 2]) adds the list as a SINGLE nested element [..., [1, 2]]. L.extend([1, 2]) adds individual items [..., 1, 2].",
        "Assigning result of sort() or reverse(): x = L.sort() sets x to None because these methods modify in-place and return None!"
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "What is the return value of list.sort() and list.reverse() in Python?", "a": "None (they modify the list in place)."},
            {"q": "What is the difference between append() and extend() in Python?", "a": "append() adds its argument as a single element; extend() adds each item of an iterable argument individually."}
        ],
        "shortAnswer": "Q: Explain insert() and count() methods with syntax and examples.\nAns: insert(pos, val) places val at specified index. count(val) returns frequency of val in the list.",
        "fourteenMark": "Q: What are list methods in Python? Explain append(), insert(), extend(), sort(), reverse(), index(), and count() with syntax, dry-run, and write a program demonstrating each."
    },
    "partM_revision": "append(x) = add to end. insert(i, x) = add at index i. extend(L2) = merge lists. reverse() = flip order. count(x) = frequency. index(x) = first position."
})

# u2-t17: Implementing Arrays using Lists
notes.append({
    "id": "u2-t17",
    "unit": "Unit-II",
    "chapter": "Chapter 6: Lists & Implementing Arrays",
    "title": "Implementing Arrays using Lists in Python",
    "partA_intro": "Unlike C or C++, standard Python does not have a native primitive array type built into the basic language syntax. Instead, Python programmers utilize Lists to implement 1D and 2D arrays because lists offer dynamic sizing, element indexing, and built-in operations.",
    "partB_realLife": "Think of a row of egg cartons. An array is a fixed-size row where each slot holds an egg accessible by its pocket number (0, 1, 2, ...). Python's list behaves like an elastic carton that can grow or shrink as needed.",
    "partC_hinglish": "C language mein Array ek fixed-size ka structure hota hai jisme ek hi type ka data rakha jata hai. Python mein alag se koi 'array' keyword nahi hota (jab tak hum alag se module import na karein). Python mein hum 'Lists' ka use karke hi Array banate hain. Agar hum homogeneous list banayein (jisme saare elements ek hi type ke hon, jaise sirf numbers), toh wo bilkul Array ki tarah behave karti hai: index se access karna, traverse karna, search karna, aur elements add karna.",
    "partD_examDef": "In Python, arrays are conceptually implemented using lists due to their contiguous sequential storage, zero-based integer indexing, traversal capability, and support for array operations like insertion, deletion, and linear searching.",
    "partE_points": [
        "Homogeneous Implementation: To simulate an array, use a list containing elements of identical data types.",
        "Array Operations implemented via List:\n  - Traversal: Accessing each element using a for loop.\n  - Insertion: Adding elements via append() or insert().\n  - Deletion: Removing elements via pop() or remove().\n  - Searching: Finding element position via index() or linear search loop.\n  - Updating: Modifying element via arr[i] = new_value.",
        "Advantages of List as Array: Dynamic sizing (no fixed length declaration needed), built-in boundary checks, rich library methods."
    ],
    "partF_syntax": "# Initializing a 1D Array of size N with zeros:\narr = [0] * size\n\n# Creating and populating an array:\narr = [10, 20, 30, 40, 50]",
    "partG_example": "# Program implementing a 1D Array using a Python list\n# Performing Traversal, Insertion, Updation, and Linear Search\n\n# 1. Initialize Array\narray = [10, 20, 30, 40, 50]\nprint(\"Initial Array:\", array)\n\n# 2. Traversal\nprint(\"Array Elements:\")\nfor i in range(len(array)):\n    print(f\"Element at index {i}: {array[i]}\")\n\n# 3. Updation\narray[2] = 99\nprint(\"After updating index 2:\", array)\n\n# 4. Linear Search\ntarget = 40\nfound_at = -1\nfor i in range(len(array)):\n    if array[i] == target:\n        found_at = i\n        break\n\nprint(f\"Element {target} found at index: {found_at}\")",
    "partH_lineByLine": [
        "Line 5: array = [10, 20, 30, 40, 50] creates a 1D integer array.",
        "Lines 9-11: Traverses array by index using for i in range(len(array)).",
        "Line 14: array[2] = 99 updates element at index 2 from 30 to 99.",
        "Lines 17-23: Implements linear search: loops through array, compares array[i] == target, records index and breaks."
    ],
    "partI_dryRun": [
        {"step": 1, "statement": "array = [10, 20, 30, 40, 50]", "action": "Creates 1D array", "value": "5 elements"},
        {"step": 2, "statement": "array[2] = 99", "action": "Updates element at index 2", "value": "[10, 20, 99, 40, 50]"},
        {"step": 3, "statement": "Linear Search for 40", "action": "Matches at i=3", "value": "found_at = 3"}
    ],
    "partJ_output": "Initial Array: [10, 20, 30, 40, 50]\nArray Elements:\nElement at index 0: 10\nElement at index 1: 20\nElement at index 2: 30\nElement at index 3: 40\nElement at index 4: 50\nAfter updating index 2: [10, 20, 99, 40, 50]\nElement 40 found at index: 3",
    "partK_mistakes": [
        "Assuming Python has a native 'array' keyword like C: Python requires lists or the import of the 'array' / 'numpy' module for strict low-level arrays.",
        "Exceeding array bounds: accessing array[len(array)] produces IndexError."
    ],
    "partL_examPrep": {
        "oneMark": [
            {"q": "How can you initialize a 1D array of 5 zeros using a Python list?", "a": "[0] * 5"},
            {"q": "What is the time complexity of accessing an element by index in a list-based array?", "a": "O(1) (Constant time)."}
        ],
        "shortAnswer": "Q: How are arrays implemented in Python using lists?\nAns: Lists provide indexed contiguous memory and methods to simulate arrays. A list with elements of the same data type functions as an array supporting traversal, insertion, deletion, and searching.",
        "fourteenMark": "Q: Explain how 1D arrays are implemented in Python using Lists. Write complete Python programs to implement: (1) Array Traversal, (2) Insertion of an element at a given position, (3) Deletion of an element, and (4) Linear Search."
    },
    "partM_revision": "Arrays in Python are implemented using Lists. Supports O(1) index access, traversal with for i in range(len(arr)), insertion via insert(), and search via loop."
})

with open("data/notes.json", "w", encoding="utf-8") as f:
    json.dump(notes, f, indent=2)

print(f"Total notes successfully saved: {len(notes)}")

