# Uses python3
import sys
import itertools
import numpy

def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)
        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partitions_opt(W, n, items):
    count = 0 
    val = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            val[i][j] = val[i][j-1]
            if items[j-1]<=i:
                temp = val[i-items[j-1]][j-1] + items[j-1]
                if temp > val[i][j]:
                    val[i][j] = temp
            if val[i][j] == W: count += 1
    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions_opt(total_weight//3, n, item_weights)

