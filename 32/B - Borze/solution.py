s = input().strip()
 
result = []
 
i = 0
 
while i < len(s):
    if s[i] == '.':
        result.append('0')
    else:
        # '-' case
        if s[i + 1] == '.':
            result.append('1')
        else:
            result.append('2')
 
        i += 1  # skip next character
 
    i += 1
 
print(''.join(result))