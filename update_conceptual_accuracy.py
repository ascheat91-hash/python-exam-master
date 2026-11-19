import json

notes = json.load(open('data/notes.json', encoding='utf-8'))

# ==========================================
# 1. Update u1-t3: Comments vs Docstrings
# ==========================================
n3 = next(x for x in notes if x['id'] == 'u1-t3')
n3['title'] = "Comments (#) vs Docstrings (Triple Quotes)"
n3['partA_intro'] = (
    "Comments are non-executable explanatory notes written inside the program code for human readers. "
    "In Python, '#' is the official syntax for single-line comments. Python does NOT have a dedicated "
    "multiline comment syntax. Triple-quoted strings (''' or \"\"\") are technically string literals, but "
    "when not assigned to any variable, they are ignored by Python or used as docstrings to document functions and modules."
)
n3['partC_hinglish'] = (
    "Comments wo notes hote hain jo hum apne ya doosre programmers ke samajhne ke liye likhte hain. "
    "Python in lines ko bilkul ignore (skip) kar deta hai. Python mein single-line comment ke liye '#' use hota hai. "
    "Ek bahut important technical baat jo viva aur exam mein aati hai: Python mein multiline comment ke liye koi alag keyword "
    "ya syntax nahi hota! Hum multiple lines par '#' laga sakte hain, ya phir triple quotes (''' ya \"\"\") use karte hain. "
    "Triple quotes asal mein string literals hote hain; agar unhe kisi variable ko na dein toh Python unhe execute nahi karta, "
    "aur jab wo kisi function/class ke top par hote hain toh unhe 'Docstrings' kaha jata hai."
)
n3['partD_examDef'] = (
    "Comments are non-executable text statements in Python source code marked with '#' used for program documentation. "
    "Python has no native multi-line comment token; instead, consecutive '#' characters or unassigned triple-quoted "
    "string literals (often utilized as docstrings) serve multi-line explanatory purposes."
)
n3['partE_points'] = [
    "Single-line Comment: Uses the hash symbol (#). Everything from # to the end of that line is ignored by the interpreter.",
    "Inline Comment: A comment placed at the end of an executable statement (e.g., x = 10 # storing age).",
    "No Native Multiline Comment Syntax: Python does NOT possess a /* ... */ construct like C/Java.",
    "Multiline Comment convention: Created either by placing '#' at the beginning of each line, or using triple-quoted string blocks (''' or \"\"\").",
    "Docstrings vs Comments: Triple-quoted strings placed right at the beginning of a function, class, or module are 'docstrings'. Unlike comments, docstrings are retained at runtime in the __doc__ attribute."
]
n3['partF_syntax'] = (
    "# Single line comment\n"
    "# Line 1 of multiline comment\n"
    "# Line 2 of multiline comment\n\n"
    "\"\"\"\n"
    "Triple-quoted string literal used as\n"
    "a multiline documentation block / docstring.\n"
    "\"\"\""
)
n3['partG_example'] = (
    "# Program to demonstrate single-line comments and docstrings\n\n"
    "# Initializing student marks\n"
    "marks = 45  # Pass marks threshold is 35\n\n"
    "\"\"\"\n"
    "This multiline block is an unassigned string literal.\n"
    "Because it is unassigned, Python skips it during execution.\n"
    "\"\"\"\n"
    "print('Final Student Marks:', marks)"
)
n3['partH_lineByLine'] = [
    "Line 1: # Program... Python sees '#' and ignores the entire line.",
    "Line 3: # Initializing... Comment line ignored by interpreter.",
    "Line 4: marks = 45 is executed; '# Pass marks...' at the line end is ignored as an inline comment.",
    "Lines 6-9: Triple quotes enclose a multiline string literal; since it is not assigned to any variable, it is evaluated and discarded (acting as a comment block).",
    "Line 10: print() outputs the string and variable value."
]
n3['partJ_output'] = "Final Student Marks: 45"
n3['partL_examPrep']['shortAnswer'] = (
    "Q: What is the difference between a comment and a docstring in Python?\n"
    "Ans: Comments start with '#' and are completely stripped during compilation. "
    "Docstrings are triple-quoted string literals placed at the start of modules/functions, which are stored in the object's __doc__ attribute and accessible at runtime."
)
n3['partM_revision'] = "Single line comment = '#'. Python has NO native multiline comment symbol. Triple quotes ('''/\"\"\") are string literals used as docstrings/multiline notes."

# ==========================================
# 2. Update u1-t13: Identity and Equality
# ==========================================
n13 = next(x for x in notes if x['id'] == 'u1-t13')
n13['partA_intro'] = (
    "Identity operators compare the identity of two objects, verifying whether both variables reference "
    "the exact same object in Python's memory space. In contrast, equality operators compare whether the values "
    "held by two objects are identical."
)
n13['partC_hinglish'] = (
    "Ye exam ka ek favourite question hai! '==' operator do variables ki VALUE (andar ki cheez) check karta hai ki "
    "kya dono barabar hain. Jabki 'is' operator check karta hai OBJECT IDENTITY—yaani kya dono variables EK HI OBJECT ko "
    "point kar rahe hain. id() function Python mein har object ka ek unique integer identity number return karta hai. "
    "Exam mein ise universal physical memory address kehne ke bajaye 'unique object identity integer' kehna technically zyada accurate hai."
)
n13['partD_examDef'] = (
    "Identity operators ('is' and 'is not') test whether two identifiers refer to the exact same object in Python. "
    "The equality operator ('==') tests value equality, whereas 'is' tests object identity equivalence (evaluating id(a) == id(b))."
)
n13['partE_points'] = [
    "'is' Operator: Returns True if both variables point to the identical object in memory (id(a) == id(b)).",
    "'is not' Operator: Returns True if both variables point to distinct objects (id(a) != id(b)).",
    "id() Function: Returns an integer representing the unique identity of the object, guaranteed unique and constant for its lifetime.",
    "Equality (==) vs Identity (is): Two distinct list objects can have identical values (== evaluates to True) while having different identities ('is' evaluates to False)."
]
n13['partM_revision'] = "'==' compares values. 'is' compares object identity (id(a) == id(b)). id() returns the unique object identity integer."

# ==========================================
# 3. Update u2-t11: Python Lists Storage
# ==========================================
n11 = next(x for x in notes if x['id'] == 'u2-t11')
n11['partA_intro'] = (
    "A list in Python is an ordered, mutable sequence that stores REFERENCES to objects. "
    "Unlike primitive arrays in C that store raw data bytes contiguously, a Python list stores a contiguous array of "
    "pointers (references) to objects located elsewhere in memory, which allows it to hold heterogeneous (mixed) data types."
)
n11['partC_hinglish'] = (
    "List Python ka sabse popular aur versatile data type hai jise Square Brackets [ ] mein likhte hain. "
    "C language ke array mein direct numbers ek ke baad ek raw bytes mein store hote the, isliye sabka ek hi type hona zaroori tha. "
    "Lekin Python list asal mein REFERENCES (pointers/addresses) ka array hoti hai! List ke dabbo mein values nahi, "
    "balki values ke references store hote hain. Isliye Python list aasaani se number, string, float sab ek sath store kar sakti hai "
    "(Heterogeneous collection). Aur ye Mutable hoti hai, yaani elements ko badla ja sakta hai."
)
n11['partD_examDef'] = (
    "A list is an ordered, mutable collection of object references enclosed in square brackets [ ]. "
    "Internally, it is implemented as a dynamic array of pointers to objects, enabling heterogeneous storage and in-place element modification."
)
n11['partE_points'] = [
    "Stores Object References: Python lists store references (pointers) to objects, not the raw primitive values contiguously in-line.",
    "Heterogeneous: Can hold elements of different data types (e.g., [101, 'Anjali', 82.5, True]) because each slot holds a uniform object reference pointer.",
    "Ordered Sequence: Elements maintain the order of insertion and are accessible via zero-based indexing.",
    "Mutable: Elements can be updated, appended, and deleted in-place.",
    "Dynamic Resizing: Allocates and re-allocates memory automatically as elements are added or removed."
]
n11['partM_revision'] = "List = ordered, mutable sequence storing object references in []. Supports mixed data types because each element is a reference pointer."

with open('data/notes.json', 'w', encoding='utf-8') as f:
    json.dump(notes, f, indent=2)

print("Educational content accuracy updates completed successfully.")

