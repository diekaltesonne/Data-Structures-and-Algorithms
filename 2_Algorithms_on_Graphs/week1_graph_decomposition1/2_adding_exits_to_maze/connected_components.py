#Uses python3

import sys

visited = set()
k = 0

#write your code here
def reach(adj, x, ):
    visited.add(x)
    for i in adj[x]:
        if i not in visited:
            reach(adj,i)

def number_of_components(adj):
    result = 0
    for i in adj:
        if len(i) == 0:
            result += 1
        else:
            for j in i:
                if j not in visited:
                    result += 1
                    reach(adj,j)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
