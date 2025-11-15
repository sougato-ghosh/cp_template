# Python Competitive Programming Standard Library Reference

This document is a compact yet comprehensive guide to the most essential Python standard library tools, syntax, and idioms used in competitive programming.

---

## **1. Fast I/O**

### `input()`

Basic input function.

```python
x = input().strip()
```

### `sys.stdin` for fast input

```python
import sys
input = sys.stdin.readline
```

### Output

```python
print(a, b)
```

---

## **2. Data Types & Conversions**

### Integer, Float, String

```python
x = int(s)
y = float(s)
z = str(x)
```

### List from input

```python
arr = list(map(int, input().split()))
```

### List of strings

```python
words = input().split()
```

### Tuple

```python
t = (1, 2, 3)
```

### Set

```python
s = set([1, 2, 3])
```

### Dictionary

```python
d = {"a": 1, "b": 2}
```

---

## **3. List Operations**

### Creation

```python
arr = [0] * 10
arr = [i*i for i in range(10)]
```

### Methods

```python
arr.append(x)
arr.pop()        # remove last
arr.pop(i)       # remove index i
arr.remove(x)    # remove value x
arr.sort()
arr.sort(reverse=True)
arr.reverse()
arr.count(x)
arr.index(x)
```

### Sorting with key

```python
arr.sort(key=lambda x: x[1])
```

### Slicing

```python
arr[1:5]
arr[::-1]
```

### Copy

```python
b = arr[:]
```

---

## **4. String Operations**

```python
s = "hello"
s.upper()
s.lower()
s.capitalize()
s.title()
s.count("l")
s.find("lo")
s.replace("l", "L")
s.split()
"-".join(list_of_words)
s.strip()
```

Reversing string:

```python
rev = s[::-1]
```

Checking numeric/alphabetic:

```python
s.isdigit()
s.isalpha()
s.isalnum()
```

---

## **5. Math Library**

```python
import math
math.sqrt(x)
math.gcd(a, b)
math.lcm(a, b)
math.factorial(n)
math.ceil(x)
math.floor(x)
math.log(x, base)
math.pi
math.inf
```

---

## **6. `itertools` (Very Important)**

```python
from itertools import permutations, combinations, combinations_with_replacement, product, accumulate, groupby
```

### Permutations

```python
for p in permutations([1,2,3]):
    pass
```

### Combinations

```python
for c in combinations([1,2,3], 2):
    pass
```

### Cartesian Product

```python
for p in product([0,1], repeat=3):
    pass
```

### Accumulate (prefix sums)

```python
from itertools import accumulate
prefix = list(accumulate(arr))
```

---

## **7. `collections` Library**

### `deque` (O(1) pops and pushes both ends)

```python
from collections import deque
q = deque([1,2,3])
q.append(4)
q.appendleft(0)
q.pop()
q.popleft()
```

### `Counter`

```python
from collections import Counter
c = Counter(arr)
c[5]      # frequency of 5
c.most_common(1)
```

### `defaultdict`

```python
from collections import defaultdict
d = defaultdict(int)
d["x"] += 1
```

### `OrderedDict`

```python
from collections import OrderedDict
```

---

## **8. `heapq` – Priority Queue (Min-Heap)**

```python
import heapq
h = []
heapq.heappush(h, x)
x = heapq.heappop(h)
```

Max-heap trick:

```python
heapq.heappush(h, -x)
mx = -heapq.heappop(h)
```

---

## **9. Bisect (Binary Search)**

```python
import bisect
idx = bisect.bisect_left(arr, x)
idx = bisect.bisect_right(arr, x)
bisect.insort(arr, x)
```

---

## **10. Random**

```python
import random
random.randint(a, b)
random.choice(arr)
random.shuffle(arr)
```

---

## **11. Time & Date (Rare but Useful)**

```python
import time
time.time()
```

---

## **12. Algorithms Templates**

### Fast Exponentiation

```python
def modpow(a, b, m):
    r = 1
    while b:
        if b & 1:
            r = r * a % m
        a = a * a % m
        b >>= 1
    return r
```

### Sieve of Eratosthenes

```python
def sieve(n):
    prime = [True]* (n+1)
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    return [i for i in range(2, n+1) if prime[i]]
```

### BFS

```python
from collections import deque

def bfs(start, graph):
    q = deque([start])
    vis = {start}
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
```

### DFS

```python
def dfs(u, graph, vis):
    vis.add(u)
    for v in graph[u]:
        if v not in vis:
            dfs(v, graph, vis)
```

### Prefix Sum

```python
prefix = [0]
for x in arr:
    prefix.append(prefix[-1] + x)
```

### Binary Search Template

```python
def binary_search(arr, x):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            lo = mid+1
        else:
            hi = mid-1
    return -1
```

---

## **13. File I/O (Offline Testing)**

```python
with open("input.txt") as f:
    data = f.read().split()
```

---

## **14. Useful Tricks for CP**

### Swapping

```python
a, b = b, a
```

### Multiple Input Reading

```python
for _ in range(int(input())):
    pass
```

### Large Recursion

```python
import sys
sys.setrecursionlimit(10**7)
```

---

## **15. Python Built-in Functions (Must Know!)**

```python
abs(x)
min(a)
max(a)
sum(a)
len(a)
sorted(a)
any(a)
all(a)
map()
filter()
zip()
```

---

## **16. Lambda Functions**

```python
f = lambda x: x*x
arr.sort(key=lambda x: x[1])
```

---

## **17. Regex Basics**

```python
import re
m = re.match(pattern, text)
re.findall(pattern, text)
re.sub(pattern, repl, text)
```

---

## **18. Dataclass (Sometimes Useful)**

```python
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
```

---

## **19. Decimal for Precision**

```python
from decimal import Decimal, getcontext
getcontext().prec = 30
x = Decimal('1.2345')
```

---

## **20. Fractions**

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)
```

---

# End of Reference
