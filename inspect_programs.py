import json

programs = json.load(open('data/programs.json', encoding='utf-8'))

for p in programs:
    print(f"=== {p['id']}: {p['title']} ===")
    print("Problem:", p['problem'])
    print("Does code have palindrome check?:", 'palindrome' in p['code'].lower())
    print("Does code have compound interest?:", 'compound' in p['code'].lower())
    print()

