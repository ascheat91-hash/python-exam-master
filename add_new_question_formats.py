import json

questions = json.load(open('data/questions.json', encoding='utf-8'))

# Categories to add:
# 1. Definition
# 2. ShortAnswer
# 3. Debugging (Find the error)
# 4. CodingExercise (Write a program)
# 5. Descriptive (Theory question)

new_questions = [
    # 1. Definition (Unit-I)
    {
        "id": f"q-{len(questions)+1}",
        "topicId": "u1-t2",
        "unit": "Unit-I",
        "category": "Definition",
        "level": "Level 1",
        "question": "Define 'Identifier' in Python and state its primary purpose in programming.",
        "options": None,
        "correct": "An identifier is a user-defined name given to a variable, function, class, or object to uniquely identify it in memory.",
        "explanation": "Identifiers act as custom labels for memory locations holding objects and code blocks."
    },
    # 2. Definition (Unit-II)
    {
        "id": f"q-{len(questions)+2}",
        "topicId": "u2-t13",
        "unit": "Unit-II",
        "category": "Definition",
        "level": "Level 1",
        "question": "What is meant by 'List Mutability' in Python?",
        "options": None,
        "correct": "List mutability means list elements can be modified, added, or removed in-place without altering the list's memory address.",
        "explanation": "Unlike immutable strings and tuples, lists allow direct in-place mutation via indexing and methods."
    },
    # 3. ShortAnswer (Unit-I)
    {
        "id": f"q-{len(questions)+3}",
        "topicId": "u1-t9",
        "unit": "Unit-I",
        "category": "ShortAnswer",
        "level": "Level 2",
        "question": "Differentiate between the division operator '/' and floor division operator '//' in Python with examples.",
        "options": None,
        "correct": "'/' returns float quotient (e.g. 7/2 = 3.5); '//' returns integer quotient rounded down (e.g. 7//2 = 3).",
        "explanation": "In Python 3, '/' always produces a float result, while '//' truncates the decimal portion."
    },
    # 4. ShortAnswer (Unit-II)
    {
        "id": f"q-{len(questions)+4}",
        "topicId": "u2-t10",
        "unit": "Unit-II",
        "category": "ShortAnswer",
        "level": "Level 2",
        "question": "Explain the difference between 'break' and 'continue' branching statements in loops.",
        "options": None,
        "correct": "'break' terminates the entire loop immediately; 'continue' skips only the remaining statements of the current iteration and advances to the next.",
        "explanation": "break exits the loop structure completely, whereas continue proceeds to the next iteration."
    },
    # 5. Debugging (Find the error) (Unit-I)
    {
        "id": f"q-{len(questions)+5}",
        "topicId": "u1-t4",
        "unit": "Unit-I",
        "category": "Debugging",
        "level": "Level 2",
        "question": "Identify the error in this code and write the corrected statement:\nage = input('Enter age: ')\nnext_year = age + 1",
        "options": None,
        "correct": "age = int(input('Enter age: '))",
        "explanation": "input() returns a string. Attempting string + int raises TypeError. Typecasting age to int fixes the issue."
    },
    # 6. Debugging (Find the error) (Unit-II)
    {
        "id": f"q-{len(questions)+6}",
        "topicId": "u2-t3",
        "unit": "Unit-II",
        "category": "Debugging",
        "level": "Level 2",
        "question": "Find the syntax error in the following conditional construct:\nnum = 14\nif num % 2 = 0:\n    print('Even')",
        "options": None,
        "correct": "if num % 2 == 0:",
        "explanation": "Single '=' is the assignment operator. Equality comparison in an if condition requires double '=='."
    },
    # 7. CodingExercise (Unit-I)
    {
        "id": f"q-{len(questions)+7}",
        "topicId": "u1-t9",
        "unit": "Unit-I",
        "category": "CodingExercise",
        "level": "Level 2",
        "question": "Write a 2-line Python script that swaps the values of two variables x and y without using a temporary third variable.",
        "options": None,
        "correct": "x, y = 10, 20\nx, y = y, x",
        "explanation": "Python supports tuple packing and unpacking, allowing direct variable swapping with 'x, y = y, x'."
    },
    # 8. CodingExercise (Unit-II)
    {
        "id": f"q-{len(questions)+8}",
        "topicId": "u2-t8",
        "unit": "Unit-II",
        "category": "CodingExercise",
        "level": "Level 2",
        "question": "Write a Python for loop using range() to print odd numbers from 1 to 9 on a single line separated by spaces.",
        "options": None,
        "correct": "for i in range(1, 10, 2):\n    print(i, end=' ')",
        "explanation": "range(1, 10, 2) starts at 1, steps by 2, and ends before 10, generating 1, 3, 5, 7, 9."
    },
    # 9. Descriptive/Theory (Unit-I)
    {
        "id": f"q-{len(questions)+9}",
        "topicId": "u1-t14",
        "unit": "Unit-I",
        "category": "Descriptive",
        "level": "Level 3",
        "question": "What is Operator Precedence and Associativity? Explain the PEMDAS rule with special emphasis on the associativity of the exponentiation (**) operator.",
        "options": None,
        "correct": "Precedence specifies evaluation priority; associativity specifies direction for equal-precedence operators. Exponentiation (**) has right-to-left associativity (e.g. 2**3**2 = 2**9 = 512).",
        "explanation": "Precedence rules resolve ambiguity in complex expressions; exponentiation evaluates right-to-left, unlike addition/subtraction."
    },
    # 10. Descriptive/Theory (Unit-II)
    {
        "id": f"q-{len(questions)+10}",
        "topicId": "u2-t17",
        "unit": "Unit-II",
        "category": "Descriptive",
        "level": "Level 3",
        "question": "Explain how 1D arrays are implemented using lists in Python. Describe traversal and linear search operations.",
        "options": None,
        "correct": "1D arrays are simulated using homogeneous lists. Traversal uses a for loop over range(len(arr)). Linear search checks arr[i] == target sequentially.",
        "explanation": "Python lists provide contiguous pointer indexing, enabling standard array algorithms including insertion, traversal, and linear searching."
    }
]

questions.extend(new_questions)

with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Total questions after adding 5 new practice categories: {len(questions)}")

