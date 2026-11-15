with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'function handleFileUpload|const handleFileUpload', text)]
for idx in matches:
    print('Match at', idx)
    print(text[idx:idx+800])
