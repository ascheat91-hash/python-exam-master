import json

notes = json.load(open('data/notes.json', encoding='utf-8'))

# Topic u2-t8 fix
n8 = next(x for x in notes if x['id'] == 'u2-t8')
n8['partG_example'] = (
    "# Demonstration of 1, 2, and 3 argument forms of range()\n"
    "print('1-arg range(3):')\n"
    "for i in range(3):\n"
    "    print(i, end=' ')\n"
    "print()  # newline\n\n"
    "print('2-arg range(2, 6):')\n"
    "for i in range(2, 6):\n"
    "    print(i, end=' ')\n"
    "print()  # newline\n\n"
    "print('3-arg range(10, 0, -2):')\n"
    "for i in range(10, 0, -2):\n"
    "    print(i, end=' ')\n"
    "print()  # newline"
)
n8['partJ_output'] = (
    "1-arg range(3):\n"
    "0 1 2 \n"
    "2-arg range(2, 6):\n"
    "2 3 4 5 \n"
    "3-arg range(10, 0, -2):\n"
    "10 8 6 4 2 "
)

# Topic u2-t10 fix
n10 = next(x for x in notes if x['id'] == 'u2-t10')
n10['partG_example'] = (
    "# Program demonstrating break, continue, and pass\n"
    "print('Demonstrating break (stops at 3):')\n"
    "for i in range(1, 6):\n"
    "    if i == 3:\n"
    "        break\n"
    "    print(i, end=' ')\n"
    "print()  # newline\n\n"
    "print('Demonstrating continue (skips 3):')\n"
    "for i in range(1, 6):\n"
    "    if i == 3:\n"
    "        continue\n"
    "    print(i, end=' ')\n"
    "print()  # newline\n\n"
    "print('Demonstrating pass (placeholder):')\n"
    "for i in range(1, 4):\n"
    "    if i == 2:\n"
    "        pass  # Placeholder, does nothing\n"
    "    print(i, end=' ')\n"
    "print()  # newline"
)
n10['partJ_output'] = (
    "Demonstrating break (stops at 3):\n"
    "1 2 \n"
    "Demonstrating continue (skips 3):\n"
    "1 2 4 5 \n"
    "Demonstrating pass (placeholder):\n"
    "1 2 3 "
)

with open('data/notes.json', 'w', encoding='utf-8') as f:
    json.dump(notes, f, indent=2)

print("Updated notes for u2-t8 and u2-t10.")

