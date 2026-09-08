import sys
import heapq
 
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))
 
    # A = minimum cost needed before playing
    # the win-condition card for the first time.
 
    heap = []
 
    # First k-1 cards are initially before the win-condition
    for i in range(k - 1):
        heapq.heappush(heap, a[i])
 
    cost = 0
 
    # Bring the win-condition from position p to position k
    for i in range(k - 1, p - 1):
        heapq.heappush(heap, a[i])
 
        cheapest = heapq.heappop(heap)
        cost += cheapest
 
    # Play the win-condition for the first time
    cost += a[p - 1]
 
    if cost > m:
        print(0)
        continue
 
    # After playing it, the win-condition goes to the back.
    # To play it again, n-k other cards have to be played.
    # Choose the n-k cheapest cards (excluding win-condition).
 
    others = []
 
    for i in range(n):
        if i != p - 1:
            heapq.heappush(others, a[i])
 
    cycle_cost = a[p - 1]
 
    for _ in range(n - k):
        cycle_cost += heapq.heappop(others)
 
    # We already played it once.
    answer = 1 + (m - cost) // cycle_cost
 
    print(answer)