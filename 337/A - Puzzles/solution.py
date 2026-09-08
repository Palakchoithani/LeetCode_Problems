n, m = map(int, input().split())
 
a = list(map(int, input().split()))
 
a.sort()
 
ans = float('inf')
 
for i in range(m - n + 1):
    diff = a[i + n - 1] - a[i]
    ans = min(ans, diff)
 
print(ans)