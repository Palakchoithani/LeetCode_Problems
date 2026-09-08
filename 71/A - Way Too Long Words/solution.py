t = int(input())
 
while t > 0:
    s = input().strip()
 
    if len(s) <= 10:
        print(s)
    else:
        print(s[0] + str(len(s) - 2) + s[-1])
 
    t -= 1