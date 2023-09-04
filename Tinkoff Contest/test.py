from collections import Counter
from itertools import islice

def solve(a, b, n):
    l = next((i for i in range(n) if a[i] != b[i]), n)
    r = next((i for i in reversed(range(n)) if a[i] != b[i]), -1)
    return 'YES' if l > r or \
        all(b[i] <= b[i+1] for i in range(l, r)) and \
        Counter(islice(a, l, r+1)) == Counter(islice(b, l, r+1)) \
        else 'NO'

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(solve(a, b, n))