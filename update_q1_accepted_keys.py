import json

papers = json.load(open('data/model-papers.json', encoding='utf-8'))

# Standardize acceptedKeys for each Q1 question across all 5 papers
accepted_map = {
    # Paper 1
    ("model-1", "q1-1"): ["1_test", "(c) 1_test", "c"],
    ("model-1", "q1-2"): ["true, false, none", "true, false and none", "true, false, and none"],
    ("model-1", "q1-3"): ["#", "hash", "hash symbol", "# symbol"],
    ("model-1", "q1-4"): ["str", "string", "<class 'str'>"],
    ("model-1", "q1-5"): ["4 1", "4, 1", "4 and 1"],
    ("model-1", "q1-6"): ["break terminates", "break exits", "continue skips"], # manual self-check
    ("model-1", "q1-7"): ["mutable", "mutable (can be modified)"],

    # Paper 2
    ("model-2", "q1-1"): ["str", "(b) str", "b"],
    ("model-2", "q1-2"): ["false, true", "false true", "false and true"],
    ("model-2", "q1-3"): ["/ gives float", "/ returns float", "float and int", "division and floor division"],
    ("model-2", "q1-4"): ["null statement", "placeholder", "does nothing", "no-op"],
    ("model-2", "q1-5"): ["2, 5, 8", "2 5 8", "[2, 5, 8]"],
    ("model-2", "q1-6"): ["len()", "len", "len(list)"],
    ("model-2", "q1-7"): ["30"],

    # Paper 3
    ("model-3", "q1-1"): ["123var", "(c) 123var", "c"],
    ("model-3", "q1-2"): ["<class 'complex'>", "complex"],
    ("model-3", "q1-3"): ["3"],
    ("model-3", "q1-4"): ["== compares value", "value and identity"],
    ("model-3", "q1-5"): ["[1, 4, 7]", "1, 4, 7", "1 4 7"],
    ("model-3", "q1-6"): ["insert()", "insert", "list.insert()"],
    ("model-3", "q1-7"): ["skips current iteration", "skips iteration", "skips round"],

    # Paper 4
    ("model-4", "q1-1"): ["input()", "input"],
    ("model-4", "q1-2"): ["1, 0", "1 and 0", "true=1, false=0", "true = 1, false = 0", "1 0"],
    ("model-4", "q1-3"): ["256"],
    ("model-4", "q1-4"): [":", "colon", "colon (:)"],
    ("model-4", "q1-5"): ["0, 1, 2, 3, 4", "0 1 2 3 4", "[0, 1, 2, 3, 4]"],
    ("model-4", "q1-6"): ["3"],
    ("model-4", "q1-7"): ["break", "break statement"],

    # Paper 5
    ("model-5", "q1-1"): ["''' ... '''", "(c) ''' ... '''", "c"],
    ("model-5", "q1-2"): ["float", "<class 'float'>", "5.0"],
    ("model-5", "q1-3"): ["false true", "false, true", "false and true"],
    ("model-5", "q1-4"): ["pass", "pass statement"],
    ("model-5", "q1-5"): ["'olle'", "olle", "\"olle\""],
    ("model-5", "q1-6"): ["remove by value", "remove takes value, pop takes index"],
    ("model-5", "q1-7"): ["my_list[::-1]", "[::-1]"]
}

for p in papers:
    pid = p['id']
    for q in p['q1']['questions']:
        sub_id = q['subId']
        key = (pid, sub_id)
        if key in accepted_map:
            q['acceptedAnswers'] = accepted_map[key]
        else:
            q['acceptedAnswers'] = []

with open('data/model-papers.json', 'w', encoding='utf-8') as f:
    json.dump(papers, f, indent=2)

print("Saved acceptedAnswers in model-papers.json successfully.")

