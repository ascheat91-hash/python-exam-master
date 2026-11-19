import json

notes = json.load(open('data/notes.json', encoding='utf-8'))

for tid in ['u1-t3', 'u1-t13', 'u2-t11']:
    n = next(x for x in notes if x['id'] == tid)
    print(f"=== {tid}: {n['title']} ===")
    print("examDef:", n['partD_examDef'])
    print("hinglish:", n['partC_hinglish'][:150])
    print("points:", n['partE_points'][:3])
    print()

