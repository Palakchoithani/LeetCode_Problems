n = int(input())
 
count = {}
 
for _ in range(n):
    team = input().strip()
    count[team] = count.get(team, 0) + 1
 
print(max(count, key=count.get))