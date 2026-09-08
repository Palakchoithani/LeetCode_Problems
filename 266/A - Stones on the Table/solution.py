n = int(input())
s = input().strip()
 
ans = 0
 
for i in range(1, n):
    if s[i] == s[i - 1]:
        ans += 1
 
print(ans)