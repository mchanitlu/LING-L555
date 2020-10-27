import sys
text = sys.stdin.read()
for c in text:
        if c == '.':
                text = text.replace('. ','.\n')
        if c == ')':
                text = text.replace('.) ','.\n')
        if c == '?':
                text = text.replace('? ','.\n')
        if c == '!':
                text = text.replace('! ','.\n')
print(text)
