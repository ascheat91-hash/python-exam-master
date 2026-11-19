import json

revision_data = {
    "quickDefinitions": [
        {"term": "Keywords", "def": "Reserved words in Python with fixed predefined syntactic meanings (e.g. if, for, True). Cannot be used as identifiers."},
        {"term": "Identifiers", "def": "User-defined names given to variables, functions, or classes to uniquely identify them in memory."},
        {"term": "Dynamic Typing", "def": "A language feature where variable data types are inferred automatically at runtime upon assignment."},
        {"term": "Comments", "def": "Non-executable explanatory notes written in code starting with # (or triple quotes) ignored by the interpreter."},
        {"term": "Operator Precedence", "def": "The set of rules determining the priority of operator evaluation in compound expressions."},
        {"term": "Control Flow", "def": "The order in which individual statements or instructions in a program are evaluated."},
        {"term": "Indentation", "def": "Whitespace (typically 4 spaces) used in Python to define hierarchical blocks of code."},
        {"term": "Entry-Controlled Loop", "def": "A loop (e.g., while loop) whose test condition is checked at the entry point before each execution."},
        {"term": "range() Function", "def": "A built-in sequence generator that creates an immutable progression of integers from start to stop-1."},
        {"term": "List", "def": "An ordered, mutable, heterogeneous collection of elements enclosed in square brackets []."},
        {"term": "List Mutability", "def": "The capability of list objects to have elements modified, added, or deleted in-place."},
        {"term": "Identity Operators", "def": "Operators ('is' and 'is not') that compare the memory addresses (identity) of two objects."}
    ],
    "syntaxCheatSheet": [
        {"title": "Print & Output", "syntax": "print(\"Text\", var, end=\" \", sep=\", \")"},
        {"title": "Read String Input", "syntax": "name = input(\"Prompt: \")"},
        {"title": "Read Integer Input", "syntax": "num = int(input(\"Enter integer: \"))"},
        {"title": "Read Float Input", "syntax": "price = float(input(\"Enter price: \"))"},
        {"title": "if - else Statement", "syntax": "if condition:\n    statements\nelse:\n    statements"},
        {"title": "if - elif - else Ladder", "syntax": "if cond1:\n    block1\nelif cond2:\n    block2\nelse:\n    default_block"},
        {"title": "while Loop", "syntax": "i = 1\nwhile i <= n:\n    statements\n    i += 1"},
        {"title": "for Loop with range()", "syntax": "for i in range(start, stop, step):\n    statements"},
        {"title": "Creating a List", "syntax": "my_list = [item1, item2, item3]"},
        {"title": "List Slicing", "syntax": "sub_list = my_list[start : stop : step]"},
        {"title": "List Append & Insert", "syntax": "my_list.append(item)\nmy_list.insert(index, item)"},
        {"title": "List Deletions", "syntax": "del my_list[i]\nval = my_list.pop(i)\nmy_list.remove(value)\nmy_list.clear()"}
    ],
    "operatorsComparison": [
        {"op": "+, -, *, /", "name": "Basic Arithmetic", "notes": "/ always returns float (5/2 = 2.5)"},
        {"op": "//", "name": "Floor Division", "notes": "Returns integer quotient, truncating decimal (5//2 = 2)"},
        {"op": "%", "name": "Modulus", "notes": "Returns remainder of division (7%3 = 1)"},
        {"op": "**", "name": "Exponentiation", "notes": "Raises base to power (2**3 = 8); Right-to-Left associativity"},
        {"op": "==", "name": "Equal to", "notes": "Compares value equality (returns True/False)"},
        {"op": "!=", "name": "Not Equal to", "notes": "True if operands have different values"},
        {"op": "and, or, not", "name": "Logical Operators", "notes": "English words (not &&, ||, !)"},
        {"op": "is, is not", "name": "Identity Operators", "notes": "Compares memory address id(a) == id(b)"}
    ],
    "oneDayRevisionChecklist": [
        "Memorize the 4 rules for naming identifiers (never start with digit, no spaces, no special symbols, no keywords).",
        "Remember that all keywords are lowercase except True, False, and None.",
        "Remember that input() ALWAYS returns a string; use int(input()) for numbers.",
        "Remember: '/' gives float, '//' gives int quotient, '%' gives remainder, '**' is power.",
        "Remember: Python has NO ++ or -- operator (use += 1).",
        "Know the difference between '=' (assign) and '==' (compare).",
        "Know the difference between '==' (value equal) and 'is' (memory address equal).",
        "Remember: in range(start, stop), the stop value is EXCLUDED (runs up to stop-1).",
        "Know the branching trio: 'break' (kills loop), 'continue' (skips round), 'pass' (does nothing).",
        "Know list operations: append() adds single item at end, extend() merges items, pop() removes & returns by index, remove() removes by value.",
        "Practice handwritten code for: Factorial, Even/Odd, Largest of 3, Reverse Number, and Linear Search."
    ]
}

with open("data/revision.json", "w", encoding="utf-8") as f:
    json.dump(revision_data, f, indent=2)

print("Saved revision data successfully.")

