#Uses python3
import sys
import math
import queue
import heapq
# ```
# Prim(G)
#   for all u ∈ V:
#     cost[u] ← ∞, parent[u] ← nil
#   pick any initial vertex u0
#   cost[u0] ← 0
#   PrioQ ← MakeQueue(V) {priority is cost}
#   while PrioQ is not empty:
#     v ← ExtractMin(PrioQ)
#     for all {v, z} ∈ E:
#       if z ∈ PrioQ and cost[z] > w(v, z):
#         cost[z] ← w(v, z), 
#         parent[z] ← v
#         ChangePriority(PrioQ, z, cost[z])
# ```

def module(x1,y1,x2,y2):
        return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def distance(lfp: list ,path: list, x, y):
    result = 0 
    for i in path:
        result += module(x,y,lfp[i][0],lfp[i][1])
        x,y = lfp[i][0],lfp[i][1]
    return result

def minimum_distance(x, y):
    cost = []
    parent = []
    lfp =[]
    for i, _ in enumerate(x):
        cost.append(math.inf)
        parent.append(0)
        lfp.append([x[i],y[i]])
    
    heapq.
    
    H = queue.PriorityQueue()
    H.put(0)
    cost[0] = 0

    while not H.empty():
        u = H.get()
        for i, cord in enumerate(lfp):
            w = module(cord[0],cord[1],lfp[u][0],lfp[u][1])
            if  cost[i] > w:
                cost[i] = w
                parent[i] = u
                H.put(i)

    return distance(lfp, parent, lfp[parent[0]][0],lfp[parent[0]][1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
