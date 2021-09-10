#Uses python3
#
import sys
import math
import heapq

# def extract_min(H):
#     v = 0
#     for i in range(len(H)):
#         if v == -1 or H[i] < H[v]:
#             v = i
#     H.pop(v)
#     return v


def change_priority(H,v,distance):
    for i, store in enumerate(H,0):
        if H[i][1] == v: 
            H[i][0] = distance

def dijkstra_search(adj, cost, s, t):
    dist = [10000] * len(adj)
    prev = [0] * len(adj)
    dist[s] = 0
    H = []
    for i, store in enumerate(dist,0):
        H.append([store,i]) 
    while len(H) != 0:
        u = heapq.heappop(H)[0]
        for v, ifno in enumerate(adj[u]):
            print(dist[adj[u][v]], "a")
            print(dist[u] + cost[u][v], "b")
            if dist[adj[u][v]] > dist[u] + cost[u][v]:
                dist[adj[u][v]] = dist[u] + cost[u][v]
                prev[adj[u][v]] = u
                change_priority(H,v,dist[v])
    return dist[t]

def dijkstra(adj, cost, s, t):
    used = [False] * len(adj)
    d = [math.inf] * len(adj)
    d[s] = 0
    for i in range(len(adj)):
        v = None
        for j in range(len(adj)):
            if used[j] == False and (v == None or d[j] < d[v]):
                v = j
        if d[v] == 10000:
            break
        used[v] = True
        for v1 in range(len(adj[v])):

            if d[adj[v][v1]] > d[v] + cost[v][v1]:
                d[adj[v][v1]] = d[v] + cost[v][v1]
    return d[t]




def distance(adj, cost, s, t):
    ans = dijkstra_search(adj,cost,s,t)
    if ans == 0:
        return -1
    else:
        return ans


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
