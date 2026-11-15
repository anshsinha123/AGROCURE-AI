with open('frontend/admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('<script type="text/babel">')
end = text.rfind('</script>')
script_code = text[start+26:end]

lines = script_code.splitlines()
print(f"Total script lines: {len(lines)}")

issues = []
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith('//') or s.startswith('/*') or s.startswith('*'):
        continue
    # count non-escaped single quotes
    sq = 0
    in_esc = False
    for char in s:
        if in_esc:
            in_esc = False
            continue
        if char == '\\':
            in_esc = True
        elif char == "'":
            sq += 1
    if sq % 2 != 0:
        issues.append((i+1, s))

print(f"Issues found: {len(issues)}")
for line_no, content in issues:
    print(f"Line {line_no}: {content}")
