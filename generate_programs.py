import json

programs = [
    {
        "id": "prog-1",
        "title": "Program 1: Calculate Simple Interest & Total Amount",
        "unit": "Unit-I",
        "chapter": "Variables, Reading Input & Arithmetic Operators",
        "problem": "Write a Python program to read Principal amount, Rate of interest, and Time period from the user, and calculate Simple Interest and the Total Payable Amount.",
        "whatItDoes": "Takes three numeric inputs from the user, applies the mathematical formula SI = (P * R * T) / 100, and displays the interest and total maturity amount.",
        "hinglish": "Is program mein hum user se teen cheezein input karwate hain: mool-dhan (Principal), byaaj ki dar (Rate), aur kitne saal ke liye (Time). Kyunki input() hamesha string deta hai, hum float() ka use karke number mein badal lete hain. Phir basic formula SI = (P*R*T)/100 lagakar answer screen par dikha dete hain.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read Principal amount (P) as float using float(input()).",
            "Step 3: Read Rate of interest (R) as float.",
            "Step 4: Read Time in years (T) as float.",
            "Step 5: Calculate Simple Interest: SI = (P * R * T) / 100.",
            "Step 6: Calculate Total Amount: Total = P + SI.",
            "Step 7: Display SI and Total.",
            "Step 8: Stop."
        ],
        "code": "# Python Program to calculate Simple Interest\nP = float(input(\"Enter Principal amount: \"))\nR = float(input(\"Enter Rate of interest (%): \"))\nT = float(input(\"Enter Time period (years): \"))\n\n# Formula calculation\nSI = (P * R * T) / 100\ntotal_amount = P + SI\n\n# Display results\nprint(\"Simple Interest =\", SI)\nprint(\"Total Payable Amount =\", total_amount)",
        "lineByLine": [
            "Line 2-4: Reads P, R, T from keyboard and converts string inputs to float numbers.",
            "Line 7: Computes interest using arithmetic operators *, / and parentheses.",
            "Line 8: Adds interest to principal for total sum.",
            "Lines 11-12: Displays the calculated values with descriptive labels."
        ],
        "dryRun": [
            {"step": 1, "action": "User enters P=1000, R=5, T=2", "state": "P=1000.0, R=5.0, T=2.0"},
            {"step": 2, "action": "SI = (1000 * 5 * 2) / 100", "state": "SI = 10000.0 / 100 = 100.0"},
            {"step": 3, "action": "total_amount = 1000 + 100", "state": "total_amount = 1100.0"},
            {"step": 4, "action": "print statements execute", "state": "Outputs 100.0 and 1100.0"}
        ],
        "expectedOutput": "Enter Principal amount: 1000\nEnter Rate of interest (%): 5\nEnter Time period (years): 2\nSimple Interest = 100.0\nTotal Payable Amount = 1100.0",
        "commonMistakes": [
            "Forgetting float() or int() around input(), causing TypeError when multiplying strings.",
            "Writing P*R*T/100 without keeping operator precedence in mind (though * and / have same precedence, brackets make it exam-safe)."
        ],
        "examQuestions": "Q (14 Marks): Write a Python program to calculate Simple Interest and Compound Interest taking inputs from user. Show dry-run and explain operator precedence."
    },
    {
        "id": "prog-2",
        "title": "Program 2: Check Even or Odd Number",
        "unit": "Unit-II",
        "chapter": "Conditional Statements (if-else)",
        "problem": "Write a Python program to read an integer from the user and determine whether it is an EVEN number or an ODD number.",
        "whatItDoes": "Uses the modulus operator (%) to check if the remainder after dividing by 2 is 0. If yes, it is Even; otherwise, it is Odd.",
        "hinglish": "Koyi bhi number Even tab hota hai jab wo 2 se poora bhaag (divide) ho jaye aur sheshphal (remainder) 0 bache. Is program mein hum '%' (modulus) operator se remainder nikalte hain aur if-else se check karte hain.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read an integer n from the user using int(input()).",
            "Step 3: If n % 2 == 0, then print 'n is Even'.",
            "Step 4: Else, print 'n is Odd'.",
            "Step 5: Stop."
        ],
        "code": "# Python Program to check Even or Odd\nnum = int(input(\"Enter an integer: \"))\n\nif num % 2 == 0:\n    print(num, \"is an EVEN number.\")\nelse:\n    print(num, \"is an ODD number.\")",
        "lineByLine": [
            "Line 2: Reads user input and typecasts to int.",
            "Line 4: Evaluates condition num % 2 == 0. If True, executes line 5.",
            "Line 6-7: If condition is False, executes line 7."
        ],
        "dryRun": [
            {"step": 1, "action": "User inputs 7", "state": "num = 7"},
            {"step": 2, "action": "7 % 2 == 0", "state": "1 == 0 is False"},
            {"step": 3, "action": "Jumps to else block", "state": "Prints 7 is an ODD number."}
        ],
        "expectedOutput": "Enter an integer: 7\n7 is an ODD number.",
        "commonMistakes": [
            "Using single '=' instead of double '==' in if num % 2 = 0 (causes SyntaxError).",
            "Forgetting the colon ':' after if and else."
        ],
        "examQuestions": "Q (7 Marks): Explain the if-else construct with a complete program to check even or odd numbers and provide a dry-run table."
    },
    {
        "id": "prog-3",
        "title": "Program 3: Find the Largest of Three Numbers",
        "unit": "Unit-II",
        "chapter": "Conditional Statements (if-elif-else)",
        "problem": "Write a Python program to accept three distinct numbers from the user and find the largest among them.",
        "whatItDoes": "Compares three numbers using logical 'and' operator inside an if-elif-else ladder to identify the maximum.",
        "hinglish": "Teen numbers a, b, c mein se sabse bada dhoondne ke liye hum check karte hain: Agar a, b se bhi bada hai AND c se bhi bada hai, toh a sabse bada hai. Warna agar b, c se bada hai toh b sabse bada hai. Warna aakhiri mein c sabse bada bacha.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read three numbers a, b, and c.",
            "Step 3: If (a >= b) and (a >= c), then largest = a.",
            "Step 4: Else if (b >= a) and (b >= c), then largest = b.",
            "Step 5: Else, largest = c.",
            "Step 6: Print largest.",
            "Step 7: Stop."
        ],
        "code": "# Python Program to find Largest of Three Numbers\na = float(input(\"Enter first number: \"))\nb = float(input(\"Enter second number: \"))\nc = float(input(\"Enter third number: \"))\n\nif (a >= b) and (a >= c):\n    largest = a\nelif (b >= a) and (b >= c):\n    largest = b\nelse:\n    largest = c\n\nprint(\"The largest number is:\", largest)",
        "lineByLine": [
            "Lines 2-4: Reads 3 numeric values into a, b, c.",
            "Line 6: Checks if 'a' is greater than or equal to both 'b' and 'c'.",
            "Line 8: Checks if 'b' is greater than or equal to both 'a' and 'c'.",
            "Line 10-11: If neither, 'c' is the largest.",
            "Line 13: Displays the result."
        ],
        "dryRun": [
            {"step": 1, "action": "Input: a=25, b=65, c=40", "state": "a=25, b=65, c=40"},
            {"step": 2, "action": "a >= b and a >= c (25 >= 65)", "state": "False"},
            {"step": 3, "action": "b >= a and b >= c (65 >= 25 and 65 >= 40)", "state": "True and True = True"},
            {"step": 4, "action": "largest = b", "state": "largest = 65.0"}
        ],
        "expectedOutput": "Enter first number: 25\nEnter second number: 65\nEnter third number: 40\nThe largest number is: 65.0",
        "commonMistakes": [
            "Using '&&' instead of 'and'. Python does not recognise '&&'.",
            "Writing 'else if' instead of 'elif'."
        ],
        "examQuestions": "Q (14 Marks): What is the if-elif-else ladder? Explain its execution flow and write a program to find the largest among three numbers with an execution trace."
    },
    {
        "id": "prog-4",
        "title": "Program 4: Reverse an Integer Number & Find Sum of Digits",
        "unit": "Unit-II",
        "chapter": "Loop Statements (while loop)",
        "problem": "Write a Python program to read a positive integer from the user, reverse its digits (e.g. 1234 -> 4321), and calculate the sum of its individual digits.",
        "whatItDoes": "Uses a while loop with modulus (% 10) to peel off the last digit, and floor division (// 10) to reduce the number until it becomes 0.",
        "hinglish": "Exam mein number ko reverse karne ka question har saal aane wale sabse important questions mein se ek hai! Logic simple hai: kisi bhi number ko 10 se divide karne par uska aakhiri digit reminder (% 10) mein milta hai. Phir number ko number // 10 karke chhota karte jaate hain jab tak number 0 na ho jaye.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read positive integer n.",
            "Step 3: Initialize rev = 0, digit_sum = 0.",
            "Step 4: While n > 0:\n  a. digit = n % 10\n  b. rev = (rev * 10) + digit\n  c. digit_sum = digit_sum + digit\n  d. n = n // 10",
            "Step 5: Display rev and digit_sum.",
            "Step 6: Stop."
        ],
        "code": "# Python Program to reverse a number and calculate sum of digits\nnum = int(input(\"Enter a positive integer: \"))\noriginal_num = num\nrev = 0\ndigit_sum = 0\n\nwhile num > 0:\n    digit = num % 10          # Extract last digit\n    rev = (rev * 10) + digit   # Append to reverse\n    digit_sum += digit         # Add to sum\n    num = num // 10            # Remove last digit\n\nprint(\"Original Number:\", original_num)\nprint(\"Reversed Number:\", rev)\nprint(\"Sum of Digits:\", digit_sum)",
        "lineByLine": [
            "Line 2-5: Reads num, preserves original_num, sets rev = 0 and digit_sum = 0.",
            "Line 7: Loop condition continues while num is greater than 0.",
            "Line 8: num % 10 extracts the rightmost digit.",
            "Line 9: rev * 10 shifts existing digits to the left and adds the new digit.",
            "Line 10: Adds digit to digit_sum.",
            "Line 11: num // 10 discards the rightmost digit.",
            "Lines 13-15: Displays results."
        ],
        "dryRun": [
            {"step": 1, "action": "num = 345", "state": "digit=5, rev=5, sum=5, num=34"},
            {"step": 2, "action": "num = 34", "state": "digit=4, rev=54, sum=9, num=3"},
            {"step": 3, "action": "num = 3", "state": "digit=3, rev=543, sum=12, num=0"},
            {"step": 4, "action": "num = 0", "state": "Loop terminates; output rev=543, sum=12"}
        ],
        "expectedOutput": "Enter a positive integer: 345\nOriginal Number: 345\nReversed Number: 543\nSum of Digits: 12",
        "commonMistakes": [
            "Using '/' instead of '//': num / 10 results in float, creating an infinite loop.",
            "Forgetting to multiply rev by 10 before adding digit."
        ],
        "examQuestions": "Q (14 Marks): Write a Python program using while loop to reverse a number and check whether it is a Palindrome number. Explain line by line."
    },
    {
        "id": "prog-5",
        "title": "Program 5: Factorial of a Number using for Loop and range()",
        "unit": "Unit-II",
        "chapter": "Loop Statements (for loop & range)",
        "problem": "Write a Python program to find the factorial of a given non-negative integer using a for loop and the range() function.",
        "whatItDoes": "Calculates n! = 1 * 2 * 3 * ... * n. If n is 0, factorial is 1. If n is negative, factorial does not exist.",
        "hinglish": "Factorial (n!) ka matlab hota hai 1 se lekar n tak ke saare numbers ka aapas mein multiplication. Jaise 5! = 1 * 2 * 3 * 4 * 5 = 120. range(1, n + 1) ka use karke hum 1 se lekar n tak loop chalate hain aur har number ko fact variable mein multiply karte jaate hain.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read integer n.",
            "Step 3: If n < 0, print 'Factorial does not exist'.",
            "Step 4: Else if n == 0, print 'Factorial is 1'.",
            "Step 5: Else, initialize fact = 1.\n  For i in range(1, n + 1):\n    fact = fact * i",
            "Step 6: Print fact.",
            "Step 7: Stop."
        ],
        "code": "# Python Program to calculate Factorial\nn = int(input(\"Enter a non-negative integer: \"))\n\nif n < 0:\n    print(\"Factorial does not exist for negative numbers.\")\nelif n == 0:\n    print(\"Factorial of 0 is 1.\")\nelse:\n    fact = 1\n    for i in range(1, n + 1):\n        fact *= i\n    print(f\"Factorial of {n} is: {fact}\")",
        "lineByLine": [
            "Line 2: Reads user input as integer.",
            "Lines 4-7: Handles edge cases: negative numbers and zero.",
            "Line 9: Initializes fact = 1 (multiplicative identity).",
            "Line 10: for i in range(1, n + 1): iterates through 1 to n.",
            "Line 11: fact *= i multiplies running product by current i.",
            "Line 12: Displays the final factorial product."
        ],
        "dryRun": [
            {"step": 1, "action": "n = 4, fact = 1", "state": "Start loop range(1, 5)"},
            {"step": 2, "action": "i = 1", "state": "fact = 1 * 1 = 1"},
            {"step": 3, "action": "i = 2", "state": "fact = 1 * 2 = 2"},
            {"step": 4, "action": "i = 3", "state": "fact = 2 * 3 = 6"},
            {"step": 5, "action": "i = 4", "state": "fact = 6 * 4 = 24"}
        ],
        "expectedOutput": "Enter a non-negative integer: 4\nFactorial of 4 is: 24",
        "commonMistakes": [
            "Writing range(1, n) instead of range(1, n + 1): Misses the last number n because stop is exclusive!",
            "Initializing fact = 0 instead of fact = 1: multiplying by 0 makes the result 0."
        ],
        "examQuestions": "Q (7 Marks): Write a Python program to calculate factorial of a number using for loop and range(). Show dry run table."
    },
    {
        "id": "prog-6",
        "title": "Program 6: Right-Angled Number Triangle Pattern using Nested Loops",
        "unit": "Unit-II",
        "chapter": "Loop Statements (Nested Loops)",
        "problem": "Write a Python program to print a right-angled triangle pattern of numbers up to N rows using nested for loops.",
        "whatItDoes": "Uses an outer loop to control the row count, and an inner loop to print numbers from 1 up to the current row number.",
        "hinglish": "Pattern printing ke questions mein do loops lagte hain. Bahar wala loop (i) tay karta hai ki kitni lines print hongi. Aur andar wala loop (j) tay karta hai ki us ek line mein kitne numbers print honge. end=' ' lagane se number ek hi line mein space ke sath aate hain, aur line khatam hone par print() agli line par le jata hai.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Read number of rows N.",
            "Step 3: For i from 1 to N:\n  a. For j from 1 to i:\n       Print j without newline (end=' ')\n  b. Print newline",
            "Step 4: Stop."
        ],
        "code": "# Python Program to print Number Triangle Pattern\nrows = int(input(\"Enter number of rows: \"))\n\nfor i in range(1, rows + 1):\n    for j in range(1, i + 1):\n        print(j, end=\" \")\n    print()  # Moves to next line after row completes",
        "lineByLine": [
            "Line 2: Reads total rows from user.",
            "Line 4: Outer loop runs i from 1 to rows.",
            "Line 5: Inner loop runs j from 1 to i for each row.",
            "Line 6: print(j, end=\" \") prints the number j with space, staying on same line.",
            "Line 7: print() prints newline character to begin next row."
        ],
        "dryRun": [
            {"step": 1, "action": "i = 1", "state": "Inner loop j runs for 1 -> prints '1 ' then newline"},
            {"step": 2, "action": "i = 2", "state": "Inner loop j runs for 1, 2 -> prints '1 2 ' then newline"},
            {"step": 3, "action": "i = 3", "state": "Inner loop j runs for 1, 2, 3 -> prints '1 2 3 ' then newline"}
        ],
        "expectedOutput": "Enter number of rows: 4\n1 \n1 2 \n1 2 3 \n1 2 3 4 ",
        "commonMistakes": [
            "Forgetting print() at end of outer loop, causing all numbers to print on a single continuous horizontal line.",
            "Using end=\"\" without space, bunching numbers together like 1234."
        ],
        "examQuestions": "Q (14 Marks): What is a nested loop? Write Python programs to print: (a) Number triangle pattern, (b) Star triangle pattern."
    },
    {
        "id": "prog-7",
        "title": "Program 7: Complete List Operations & Array Implementation",
        "unit": "Unit-II",
        "chapter": "Lists (Creation, Methods, Built-in Functions & Linear Search)",
        "problem": "Write a complete Python program to create a list of numbers, perform insertion, deletion, calculate sum/average/min/max, and search for a target element (Linear Search).",
        "whatItDoes": "Demonstrates all syllabus-required list operations: append(), insert(), pop(), remove(), sum(), len(), min(), max(), and searching in one unified college-ready program.",
        "hinglish": "Ye program Unit-II ke Chapter 6 (Lists) ka sabse zaroori 14-marks question cover karta hai. Isme hum ek list banate hain, usme element add karna, remove karna, max/min nikalna, aur element dhoondna (Linear Search) sab ek sath practically karte hain.",
        "algorithm": [
            "Step 1: Start",
            "Step 2: Create a list of numbers: marks = [45, 60, 32, 85, 70].",
            "Step 3: Add new elements using append() and insert().",
            "Step 4: Remove elements using pop() and remove().",
            "Step 5: Compute statistics using sum(), len(), min(), max().",
            "Step 6: Implement Linear Search by comparing each element against a search target.",
            "Step 7: Display all results and stop."
        ],
        "code": "# Python Program: Comprehensive List Operations & Array Implementation\nnumbers = [45, 60, 32, 85, 70]\nprint(\"Initial List / Array:\", numbers)\n\n# 1. Insertion\nnumbers.append(95)          # Appends to end\nnumbers.insert(2, 50)       # Inserts 50 at index 2\nprint(\"After Insertions:\", numbers)\n\n# 2. Deletion\npopped_item = numbers.pop() # Removes last element\nnumbers.remove(32)          # Removes value 32\nprint(\"After Deletions:\", numbers)\n\n# 3. Built-in Statistics\nprint(\"Total Elements:\", len(numbers))\nprint(\"Maximum Value:\", max(numbers))\nprint(\"Minimum Value:\", min(numbers))\nprint(\"Total Sum:\", sum(numbers))\nprint(\"Average:\", sum(numbers) / len(numbers))\n\n# 4. Implementing Linear Search (Array Search)\ntarget = 85\nfound_index = -1\nfor i in range(len(numbers)):\n    if numbers[i] == target:\n        found_index = i\n        break\n\nif found_index != -1:\n    print(f\"Element {target} found at index: {found_index}\")\nelse:\n    print(f\"Element {target} not found in array.\")",
        "lineByLine": [
            "Line 2: Initializes list with 5 integer elements.",
            "Lines 6-7: append(95) adds 95 at end; insert(2, 50) inserts 50 at index 2.",
            "Lines 11-12: pop() removes last item; remove(32) finds and removes value 32.",
            "Lines 16-20: Calls len(), max(), min(), sum() and calculates average.",
            "Lines 23-28: Linear search loop scans by index. If match is found, stores index and breaks.",
            "Lines 30-33: Prints whether search succeeded."
        ],
        "dryRun": [
            {"step": 1, "action": "Initial list", "state": "[45, 60, 32, 85, 70]"},
            {"step": 2, "action": "append(95), insert(2, 50)", "state": "[45, 60, 50, 32, 85, 70, 95]"},
            {"step": 3, "action": "pop(), remove(32)", "state": "[45, 60, 50, 85, 70]"},
            {"step": 4, "action": "Linear Search for 85", "state": "Matches at index 3 -> found_index = 3"}
        ],
        "expectedOutput": "Initial List / Array: [45, 60, 32, 85, 70]\nAfter Insertions: [45, 60, 50, 32, 85, 70, 95]\nAfter Deletions: [45, 60, 50, 85, 70]\nTotal Elements: 5\nMaximum Value: 85\nMinimum Value: 45\nTotal Sum: 310\nAverage: 62.0\nElement 85 found at index: 3",
        "commonMistakes": [
            "Expecting pop() to take a value: pop() takes an index; remove() takes a value.",
            "Linear search forgetting break statement, resulting in unnecessary continued iterations."
        ],
        "examQuestions": "Q (14 Marks): What is a List? Explain list operations (append, insert, pop, remove, len, max, min, sum) and write a program to implement Linear Search using a list."
    }
]

with open("data/programs.json", "w", encoding="utf-8") as f:
    json.dump(programs, f, indent=2)

print(f"Generated {len(programs)} detailed program practices successfully.")

