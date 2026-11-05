#!/usr/bin/env python3
"""Fix the brace imbalance in index.html"""
with open('/opt/data/nowm.tech/index.html', 'r') as f:
    content = f.read()

# The issue is that the template literal on line 2120 has an extra opening brace
# Line 2120: ${Object.keys(productData).map(id => {
# Line 2128: }).join('')}
# The { on line 2120 is never closed

# Let's check the content around that area
start = content.find('Object.keys(productData)')
end = content.find('<\\/script>')
print(f"Start: {start}, End: {end}")
print("Content around the issue:")
print(content[start:end+40])
