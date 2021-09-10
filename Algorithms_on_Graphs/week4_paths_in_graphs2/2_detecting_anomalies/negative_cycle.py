#Uses python3

from re import match
import sys
from typing import Match
import math

def dijkstra(adj, cost):
    prev = [-1] * len(adj)
    d = [100009] * len(adj)
    for v in range(len(adj)):
        x = -1
        for v1 in range(len(adj[v])):
            if d[adj[v][v1]] > d[v] + cost[v][v1]:
                d[adj[v][v1]] = d[v] + cost[v][v1]
                prev[adj[v][v1]] = d[v]
                x = adj[v][v1]
    
    x = -1
    for v in range(len(adj)):
        x = -1
        for v1 in range(len(adj[v])):
            if d[adj[v][v1]] > d[v] + cost[v][v1]:
                x = adj[v][v1]
                break
        if x != -1:
            break    

    if x == -1:
        return 0
    else:
        return 1

def negative_cycle(adj, cost):
    #write your code here
    return dijkstra(adj,cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
