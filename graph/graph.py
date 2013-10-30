#!/usr/bin/python

import sys
import shlex
from collections import deque

def print_vector(vector):
    return repr(vector).replace(str(sys.maxint), ' i').replace("'", "")

def dijkstra(graph, adj, begin, end):

    distance = [sys.maxint for i in range(vertices+1)]
    previous = [None for i in range(vertices+1)]
    distance[begin] = 0
    Q = graph[:]

    while Q:
        smallest = None
        for i in Q:
            if None == smallest or distance[i] < distance[smallest]:
                smallest = i

        if end == smallest:
            break
        #print Q
        Q.remove(smallest)
        
        if sys.maxint == distance[smallest]:
            break

        for neighbor in Q:
            edge = adjacency_weight(adj, smallest, neighbor)
            if edge < sys.maxint:
                alt = distance[smallest] + edge
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    previous[neighbor] = smallest
                    
    S = deque()
    u = end
    while not None == u:
        S.appendleft(u)
        u = previous[u]
    
    return S


def adjacency_weight(adj, x, y):
    return adj[x][y]


def path_weight(p, adj):
    w = 0
    for i in range(1,len(p)):
        w += adj[p[i-1]][p[i]]
    return w






parser = shlex.shlex(sys.stdin)
parser.whitespace_split = True

vertices = int(parser.get_token())
edges = int(parser.get_token())
adjacency = [ [ sys.maxint for i in range(vertices+1) ] for j in range(vertices+1) ]
graph = range(1, vertices+1)

# always calculate the path from the first node to the last node and back
start = 1
destination = vertices
total_weight = 0

# print first line values (DEBUGGG)
#print >> sys.stderr, "Vertices:", vertices, "Edges:", edges

# build adjacency matrix from input
for i in range(edges):
    s1 = int(parser.get_token())
    s2 = int(parser.get_token())
    weight = int(parser.get_token())
    #print >> sys.stderr, "S1:", s1, "S2:", s2, "weight:", weight
    adjacency[s1][s2] = weight
    adjacency[s2][s1] = weight

# print adjacency matrix (DEBUGGG)
#print >> sys.stderr, "    0   1   2   3   4   5   6   7 "
#for i in range(len(adjacency)):
#    print >> sys.stderr, i, print_vector(adjacency[i])
#print >> sys.stderr, "Distance:", distance
#print >> sys.stderr, "Previous:", previous

path = dijkstra(graph, adjacency, start, destination)

#print >> sys.stderr, repr(list(path))

weight = path_weight(path, adjacency)
#print ">>", weight
total_weight += weight


for vertex in list(path)[1:-1]:
    for i in range(vertices+1):
        adjacency[vertex][i] = sys.maxint
        adjacency[i][vertex] = sys.maxint

# print adjacency matrix (DEBUGGG)
#print >> sys.stderr, "    0   1   2   3   4   5   6   7 "
#for i in range(len(adjacency)):
#    print >> sys.stderr, i, print_vector(adjacency[i])


path2 = dijkstra(graph, adjacency, destination, start)

#print >> sys.stderr, repr(list(path2))

weight2 = path_weight(path2, adjacency)
#print ">>", weight2

total_weight += weight2

print total_weight
