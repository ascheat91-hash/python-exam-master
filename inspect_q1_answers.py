import json

papers = json.load(open('data/model-papers.json', encoding='utf-8'))

for p in papers:
    print(f"=== {p['id']} ===")
    for q in p['q1']['questions']:
        print(f"[{q['subId']}] type: {q['type']}, options: {bool(q.get('options'))}")
        print(f"  Q: {q['question'][:50]!r}")
        print(f"  Ans: {q['modelAnswer']!r}")

