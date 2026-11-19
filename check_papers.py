import json
papers = json.load(open('data/model-papers.json', encoding='utf-8'))
for i in range(len(papers)):
    p = papers[i]
    print(f"=== {p['title']} ===")
    print("Q1 q1:", p['q1']['questions'][0]['question'][:45])
    print("U1 Q2(a) marks:", p['unit1']['q2']['parts'][0]['marks'])
    print("U1 Q2(a) answer len:", len(p['unit1']['q2']['parts'][0]['modelAnswer']))

