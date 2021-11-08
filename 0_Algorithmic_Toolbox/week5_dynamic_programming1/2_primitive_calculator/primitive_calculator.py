# Uses python3
import sys
sys.setrecursionlimit(10**4)
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

d = {}
def f(n):
    if n == 1:
        return 1, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n-1)[0] + 1, n - 1)
    if n % 2 == 0:
        ret = f(n//2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n//2)
    if n % 3 == 0:
        ret = f(n//3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n//3)
    d[n] = ans
    return ans

def optimal_min_sequence_0(n):
    ans = []
    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]
    ans.append(1)
    ans.reverse()
    return ans

def optimal_min_sequence(n):
    _count = [0] * (n + 1)
    _count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        min_hops = min([_count[x] for x in indices])

        _count[i] = min_hops + 1

    ptr = n
    optimal_seq = [ptr]
    while ptr != 1:

        candidates = [ptr - 1]
        if ptr % 2 == 0:
            candidates.append(ptr // 2)
        if ptr % 3 == 0:
            candidates.append(ptr // 3)

        ptr = min(
            [(c, _count[c]) for c in candidates],
            key=lambda x: x[1]
        )[0]
        optimal_seq.append(ptr)

    return reversed(optimal_seq)

input = sys.stdin.read()
n = int(input)
#n = 96234
sequence = list(optimal_min_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
