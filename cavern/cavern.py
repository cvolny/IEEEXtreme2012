#!/usr/bin/python

import sys
import shlex
from collections import deque
from copy import deepcopy


def print_bitmap(bitmap, rows, cols):
    print "   " + "  ".join([str(x)[-1] for x in range(cols)])
    for i in range(rows):
        print str(i)[-1], bitmap[i]

def get_neighbors(node, adjacency):
    neighbors = set()
    for i in range(1,len(adjacency)):
        if adjacency[node][i] == 1:
            neighbors.add(i)
    return neighbors

def get_next_remaining(remaining, adjacency):
    largest = -1
    result = None
    for node in remaining:
        neighbors = set(get_neighbors(node, adjacency))
        viable = neighbors.intersection(remaining)
        if len(viable) > largest:
            largest = len(viable)
            result = node
    return result

parser = shlex.shlex(sys.stdin)
parser.whitespace_split = True

corridors = deque()
highest = 1
for x in range(100):
    one = parser.get_token()
    two = parser.get_token()
    if not (one and two):
        break
    a = int(one)
    b = int(two)
    if b > highest:
        highest = b
    if a > highest:
        highest = a
    corridors.append((a,b))





n = highest + 1
nodes = range(1,n)
adjacency = [ [ 0 for x in range(n+2) ] for y in range(n+2) ]

for x,y in corridors:
    adjacency[x][y] = 1
    adjacency[y][x] = 1

neighbors = [ None for i in range(0,n) ]
for i in nodes:
    neighbors[i] = get_neighbors(i, adjacency)

remaining = set(nodes)
independent = deque()
dependent = deque()
optimal = deque()
solutions = deque()
shortest = sys.maxint

for node in nodes:
    if not node in optimal:
        while len(remaining) > 0:
           #print >> sys.stderr, node
            independent.append(node)
            neighbors = get_neighbors(node, adjacency)
            dependent += neighbors
            for neighbor in neighbors:
                if neighbor in remaining:
                    remaining.remove(neighbor)
            node = get_next_remaining(remaining, adjacency)
            remaining.remove(node)
        if len(independent) < shortest:
            shortest = len(independent)
            solutions.clear() 
        solutions.append(deepcopy(independent))
        [optimal.append(x) for x in independent]
        independent.clear()
        dependent.clear()
        remaining = set(nodes)

for solution in solutions:
    for entry in solution:
        print entry,
    print
