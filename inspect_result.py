with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "currentPage === 'result'" in line or 'currentPage === "result"' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i:i+90]))
        break
