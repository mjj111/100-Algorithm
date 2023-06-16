from heapq import *
import sys

si = sys.stdin.readline
n, m = map(int, si().split())
total = 0
graph = []
for _ in range(m):
    n1, n2, weight = map(int, si().split())
    graph.append((weight, n1, n2))
    total += weight


def prim(g, start):
    mst = 0
    tree = [[] for _ in range(n+1)]
    for w, b1, b2 in g:
        tree[b1].append((w, b1, b2))
        tree[b2].append((w, b2, b1))
    visited = []
    visited.append(start)
    candidate_arr = tree[start]
    heapify(candidate_arr)
    while candidate_arr:
        w, b1, b2 = heappop(candidate_arr)
        if b2 not in visited:
            visited.append(b2)
            mst += w
            for node in tree[b2]:
                if node[2] not in visited:
                    heappush(candidate_arr, node)
    return visited, total - mst


check, answer = prim(graph, 1)
if len(check) == n:
    print(answer)
else:
    print(-1)