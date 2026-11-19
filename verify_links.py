import re, glob, os

html_files = glob.glob('*.html')
print(f"Auditing {len(html_files)} HTML files for missing assets and links:")

for f in html_files:
    content = open(f, encoding='utf-8').read()
    
    # Check linked CSS
    css_links = re.findall(r'<link[^>]+href=[\'"]([^\'"]+\.css)[\'"]', content)
    for css in css_links:
        if not os.path.exists(css):
            print(f"❌ In {f}: Missing CSS file -> {css}")
            
    # Check linked JS
    js_scripts = re.findall(r'<script[^>]+src=[\'"]([^\'"]+\.js)[\'"]', content)
    for js in js_scripts:
        if not os.path.exists(js):
            print(f"❌ In {f}: Missing JS file -> {js}")
            
    # Check internal page navigation links
    page_links = re.findall(r'href=[\'"]([a-zA-Z0-9_-]+\.html)(?:\?[^\'"]*)?[\'"]', content)
    for p in page_links:
        if not os.path.exists(p):
            print(f"❌ In {f}: Broken internal link -> {p}")

print("Asset link verification complete.")

