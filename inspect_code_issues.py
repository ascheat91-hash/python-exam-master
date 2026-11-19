import json

notes = json.load(open('data/notes.json', encoding='utf-8'))

for topic_id in ['u2-t8', 'u2-t10']:
    n = next(x for x in notes if x['id'] == topic_id)
    print(f"=== {topic_id}: {n['title']} ===")
    print("--- partG_example ---")
    print(repr(n['partG_example']))
    print("--- partJ_output ---")
    print(repr(n['partJ_output']))
    print()

