import sys
 
input = sys.stdin.readline
 
t = int(input())
 
while t > 0:
    t -= 1
 
    n = int(input())
    a = list(map(int, input().split()))
 
    # Step 1: Count frequencies of consecutive equal elements
    freq = []
    count = 1
 
    for i in range(1, n):
        if a[i] == a[i - 1]:
            count += 1
        else:
            freq.append(count)
            count = 1
 
    freq.append(count)
 
    # Step 2: Try all possible k
    ans = 0
 
    for k in range(1, n + 1):
        elements = 0
 
        for f in freq:
            if f >= k:
                elements += 1
 
        ans = max(ans, elements * k)
 
    print(ans)