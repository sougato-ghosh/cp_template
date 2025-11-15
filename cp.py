import sys
import math
#from collections import defaultdict, deque
#from bisect import bisect_left, bisect_right
#from heapq import heappush, heappop

# Fast input
input = lambda: sys.stdin.readline().strip()

# Constants
MOD = 10**9 + 7
INF = float('inf')

# Debug print (disable in contest)
def debug(*args):
    print("DEBUG:", *args)

# Solve function
def solve():
    # Example input
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Example logic
    arr.sort()
    print(*arr)

# Main
if __name__ == "__main__":
    t = 1
    # Uncomment below if multiple test cases
    # t = int(input())
    for _ in range(t):
        solve()



import sys
import math
from collections import defaultdict, Counter
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop

# Fast input
input = sys.stdin.readline

# Debug (optional)
def debug(*args):
    print(*args, file=sys.stderr)

# Solve function
def solve():
    # Example: read integers
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Your logic here
    print(sum(arr))

# Main
def main():
    t = 1
    t = int(input())  # Uncomment if multiple test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
