#!/usr/bin/env python3
"""Check JavaScript syntax in the index.html"""
with open('/opt/data/nowm.tech/index.html', 'r') as f:
    content = f.read()

start = content.find('<script>')
end = content.rfind('</script>')
if start != -1 and end != -1:
    js = content[start+len('<script>'):end]
    
    lines = js.split('\n')
    count = 0
    for i, line in enumerate(lines):
        opens = line.count('(')
        closes = line.count(')')
        count += opens - closes
        if count < 0:
            print(f'Line {i+1}: {line[:120]}')
            print(f'  Opens: {opens}, Closes: {closes}, Running count: {count}')
            break
    else:
        print(f'Final count: {count}')
        if count != 0:
            print('MISMATCH detected')
