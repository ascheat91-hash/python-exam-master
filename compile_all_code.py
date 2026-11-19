import json

notes = json.load(open('data/notes.json', encoding='utf-8'))

for n in notes:
    code = n.get('partG_example', '')
    try:
        compile(code, f"<note {n['id']}>", 'exec')
    except Exception as e:
        print(f"FAILED to compile note {n['id']}: {e}")
        print("Code was:")
        print(repr(code))

programs = json.load(open('data/programs.json', encoding='utf-8'))
for p in programs:
    code = p.get('code', '')
    try:
        compile(code, f"<prog {p['id']}>", 'exec')
    except Exception as e:
        print(f"FAILED to compile prog {p['id']}: {e}")

print("All code compilation tests completed.")

