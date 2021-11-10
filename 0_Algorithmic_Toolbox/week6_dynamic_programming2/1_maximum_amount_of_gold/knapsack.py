# Uses python3
import sys

def optimal_weight(W,w):
    w = [0] + w
    items = len(w)
    capacity = W + 1

    weights = [[0 for _ in range(items)] for _ in range(capacity)]

    for i in range(1, items):
        for j in range(1, capacity):
            weights[j][i] = weights[j][i - 1]
            if w[i] <= j:
                val = weights[j - w[i]][i - 1] + w[i]
                if weights[j][i] < val:
                    weights[j][i] = val

    return weights[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    #print(W,n,w)
    #W = 10
    #w = [1,4,8]
    print(optimal_weight(W,w))
