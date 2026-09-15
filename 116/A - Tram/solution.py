n = int(input())
 
current = 0
answer = 0
 
for _ in range(n):
    exit_count, enter_count = map(int, input().split())
 
    current -= exit_count
    current += enter_count
 
    answer = max(answer, current)
 
print(answer)