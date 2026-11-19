import json, os

notes = json.load(open('data/notes.json', encoding='utf-8'))
questions = json.load(open('data/questions.json', encoding='utf-8'))
papers = json.load(open('data/model-papers.json', encoding='utf-8'))
programs = json.load(open('data/programs.json', encoding='utf-8'))
syllabus = json.load(open('data/syllabus.json', encoding='utf-8'))

print('=== SYLLABUS AUDIT ===')
syllabus_topics = []
for u in syllabus['units']:
    for ch in u['chapters']:
        for t in ch['topics']:
            syllabus_topics.append(t['id'])
print(f'Total syllabus topics listed in syllabus.json: {len(syllabus_topics)}')

note_ids = [n['id'] for n in notes]
print(f'Total topics in notes.json: {len(notes)}')
missing_in_notes = set(syllabus_topics) - set(note_ids)
print(f'Missing topics in notes: {missing_in_notes}')

print('\n=== NOTES STRUCTURE AUDIT (13 PARTS CHECK) ===')
required_parts = [
    'partA_intro', 'partB_realLife', 'partC_hinglish', 'partD_examDef',
    'partE_points', 'partF_syntax', 'partG_example', 'partH_lineByLine',
    'partI_dryRun', 'partJ_output', 'partK_mistakes', 'partL_examPrep', 'partM_revision'
]
incomplete_notes = []
for n in notes:
    for p in required_parts:
        if p not in n or not n[p]:
            incomplete_notes.append((n['id'], p))
print(f'Incomplete notes count: {len(incomplete_notes)}')

print('\n=== QUESTION BANK AUDIT ===')
print(f'Total questions in questions.json: {len(questions)}')
question_topics = set(q['topicId'] for q in questions)
topics_without_questions = set(syllabus_topics) - question_topics
print(f'Topics without any practice questions: {topics_without_questions}')

print('\n=== MODEL PAPERS AUDIT ===')
print(f'Total model papers: {len(papers)}')
for i, p in enumerate(papers):
    q1_count = len(p['q1']['questions'])
    u1_q2_parts = len(p['unit1']['q2']['parts']) if ('q2' in p['unit1'] and 'parts' in p['unit1']['q2']) else 0
    u1_q3_parts = len(p['unit1']['q3']['parts']) if ('q3' in p['unit1'] and 'parts' in p['unit1']['q3']) else 0
    u2_q4_parts = len(p['unit2']['q4']['parts']) if ('q4' in p['unit2'] and 'parts' in p['unit2']['q4']) else 0
    u2_q5_parts = len(p['unit2']['q5']['parts']) if ('q5' in p['unit2'] and 'parts' in p['unit2']['q5']) else 0
    print(f"Paper {i+1} ({p['id']}): Q1 count={q1_count}, U1 Q2 parts={u1_q2_parts}, U1 Q3 parts={u1_q3_parts}, U2 Q4 parts={u2_q4_parts}, U2 Q5 parts={u2_q5_parts}")

