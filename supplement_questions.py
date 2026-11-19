import json

questions = json.load(open('data/questions.json', encoding='utf-8'))

# List of missing topics to add high-yield questions for
# u1-t3 (multiline comments), u1-t5 (dynamic typing check), u1-t11 (+=), u2-t2 (simple if), u2-t5 (nested if)
extra_q = [
    {
        "id": f"q-{len(questions)+1}",
        "topicId": "u1-t3",
        "unit": "Unit-I",
        "category": "MCQ",
        "level": "Level 1",
        "question": "Which of the following can be used to write multi-line explanatory notes or docstrings in Python?",
        "options": ["''' ... '''", "<!-- ... -->", "/* ... */", "-- ... --"],
        "correct": "''' ... '''",
        "explanation": "Triple quotes (''' or \"\"\") allow strings to span multiple lines and serve as multi-line comments or docstrings."
    },
    {
        "id": f"q-{len(questions)+2}",
        "topicId": "u1-t5",
        "unit": "Unit-I",
        "category": "PredictOutput",
        "level": "Level 2",
        "question": "What is the output of:\nx = 50\nx = 'Python'\nprint(type(x))",
        "options": None,
        "correct": "<class 'str'>",
        "explanation": "Due to dynamic typing, reassigning a string to variable 'x' changes its type dynamically to str."
    },
    {
        "id": f"q-{len(questions)+3}",
        "topicId": "u1-t11",
        "unit": "Unit-I",
        "category": "PredictOutput",
        "level": "Level 1",
        "question": "What is the output of:\nx = 15\nx %= 4\nprint(x)",
        "options": None,
        "correct": "3",
        "explanation": "x %= 4 computes 15 % 4 which leaves remainder 3, assigning 3 back to x."
    },
    {
        "id": f"q-{len(questions)+4}",
        "topicId": "u2-t2",
        "unit": "Unit-II",
        "category": "MCQ",
        "level": "Level 1",
        "question": "In a simple 'if' statement, what happens if the condition evaluates to False?",
        "options": ["Program terminates with error", "The indented statements are bypassed", "The compiler repeats the test", "Outputs False"],
        "correct": "The indented statements are bypassed",
        "explanation": "If the condition is False, the indented body is skipped and execution proceeds with the subsequent line."
    },
    {
        "id": f"q-{len(questions)+5}",
        "topicId": "u2-t5",
        "unit": "Unit-II",
        "category": "PredictOutput",
        "level": "Level 2",
        "question": "What is the output of:\na, b = 10, 5\nif a > 8:\n    if b > 8:\n        print('High')\n    else:\n        print('Medium')\nelse:\n    print('Low')",
        "options": None,
        "correct": "Medium",
        "explanation": "a > 8 (10 > 8) is True, entering outer if. Inner check b > 8 (5 > 8) is False, triggering inner else which prints 'Medium'."
    }
]

questions.extend(extra_q)
with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Total questions after supplement: {len(questions)}")

