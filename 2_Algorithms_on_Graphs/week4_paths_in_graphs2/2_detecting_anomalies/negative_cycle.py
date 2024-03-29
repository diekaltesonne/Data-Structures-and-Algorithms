#Uses python3
import sys

def dijkstra(adj, cost):
    # initiate all distances and previouses to be -1.
    dist = [-1] * len(adj)
    #just start from first vertex
    dist[0] = 0
    #first run Bellamford V - 1 cycles.  
    #if no negative cycles then this should be the last iteration of changes
    for i in range(len(adj)):
        for j  in range(len(adj)):
            for index, store in enumerate(adj[j]):
                jstoreCost = cost[j][index]
                if dist[store] > dist[j] + jstoreCost:
                    dist[store] = dist[j] + jstoreCost
        #check at V - 1 and then V to see if they change
        if i == len(adj) - 2:
            dist_Vminus1 = list(dist)
        if i == len(adj) - 1:
            dist_V = list(dist)
    #if there are changes on the Vth cycle,  then there was a negative cycle
    if dist_Vminus1 == dist_V:
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
