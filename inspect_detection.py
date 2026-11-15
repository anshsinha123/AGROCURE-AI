with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "currentPage === 'detection'" in line or 'currentPage === "detection"' in line:
        print(f"Line {i+1}:")
        print(''.join(lines[i:i+50]))
        break
