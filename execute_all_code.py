import json, sys, io

notes = json.load(open('data/notes.json', encoding='utf-8'))

for n in notes:
    code = n.get('partG_example', '')
    expected = n.get('partJ_output', '').strip()
    
    # Check if code requires input()
    if 'input(' in code:
        print(f"Skipping interactive execution for {n['id']} (has input())")
        continue
        
    old_stdout = sys.stdout
    redirected = io.StringIO()
    sys.stdout = redirected
    try:
        exec(code, {})
        actual = redirected.getvalue().strip()
    except Exception as e:
        actual = f"EXEC_ERROR: {e}"
    finally:
        sys.stdout = old_stdout
        
    if actual != expected:
        print(f"=== Mismatch in {n['id']}: {n['title']} ===")
        print(f"Expected:\n{expected!r}")
        print(f"Actual:\n{actual!r}")
        print()
    else:
        # print(f"MATCH: {n['id']}")
        pass

print("Non-interactive code execution audit complete.")

