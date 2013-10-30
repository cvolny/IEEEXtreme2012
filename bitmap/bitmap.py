#!/usr/bin/python

import sys
import shlex
from collections import deque


def find_rectangle(bitmap, row, col):
    clear = deque([(row,col)])
    i = j = 0
    i_done = j_done = False
    while True:
        if i_done and j_done:
            break
        elif not i_done:
            i += 1
            if bitmap[row+i][col] == 0:
                i -= 1
                i_done = True
            else:
                clear.append((row+i, col))
        elif not j_done:
            j += 1
            if bitmap[row][col+j] == 0:
                j -= 1
                j_done = True
            else:
                clear.append((row, col+j))

    if i > 0 and j > 0:
        for x in range(1,i+1):
            if bitmap[row+i][col+x] == 0:
                if x > 1:
                    return []
                elif i == j:
                    # test for triangle
                    for z in range(1,i):
                        if bitmap[row+i-z][col+z] == 0:
                            return []
                        clear.append((row+i-z,col+z))
                    cleaner(bitmap, clear)
                    return ["Triangle"]
            clear.append((row+i,col+x))
        for y in range(1,j+1):
            if bitmap[row+y][col+j] == 0:
                if y > 1:
                    return []
            clear.append((row+y,col+j))
        cleaner(bitmap, clear)
        if i == j:
            return ["Square"]
        else:
            return ["Rectangle"]
    return []

def find_parallelogram(bitmap, row, col):
    clear = deque([(row,col)])
    i = j = k = 0
    i_done = j_done = k_done = False
    while True:
        i += 1
        if bitmap[row+i][col] == 0:
            i -= 1
            break
        else:
            clear.append((row+i, col))
    if i > 0:
        while True:
            j += 1
            if (bitmap[row+i-j][col+j] == 0)or (bitmap[row-j][col+j] == 0):
                j -= 1
                break
            else:
                clear.append((row+i-j, col+j))
                clear.append((row-j, col+j))
        if j > 0:
            good = True
            for z in range(i):
                if bitmap[row-j+z][col+j] == 0:
                    good = False
                    break
                else:
                    clear.append((row-j, col+j))
            if good:
                cleaner(bitmap, clear)
                return ["Parallelogram"]

    while True:
        i += 1
        if bitmap[row][col+i] == 0:
            i -= 1
            break
        else:
            clear.append((row, col+i))
    if i > 0:
        while True:
            j += 1
            if (bitmap[row+j][col+j] == 0) or (bitmap[row-j][col+j] == 0):
                j -= 1
                break
            else:
                clear.append((row+i-j, col+j))
                clear.append((row-j, col+j))
        if j > 0:
            good = True
            for z in range(i):
                if bitmap[row-j+z][col+j] == 0:
                    good = False
                    break
                else:
                    clear.append((row-j, col+j))
            if good:
                cleaner(bitmap, clear)
                return ["Parallelogram"]

        
def cleaner(bitmap, points):
    for row,col in points:
        bitmap[row][col] = 0

def print_bitmap(bitmap, rows, cols):
    print "   " + "  ".join([str(x)[-1] for x in range(cols)])
    for i in range(rows):
        print str(i)[-1], bitmap[i]


parser = shlex.shlex(sys.stdin)
parser.whitespace_split = True

rows = int(parser.get_token())
cols = int(parser.get_token())
bits = []
result = []
length = rows * cols
total = 0

while total < length:
    token = parser.get_token()
    number = int(token)
    binary = deque([1 if x == "1" else 0 for x in bin(number)[2:]])
    for i in range(8-len(binary)):
        binary.appendleft(0)
    n = len(binary)
    bits += binary
    total += n

bitmap = [[0] * (cols+1)]
for i in range(rows):
    bitmap.append(bits[i*cols:(i+1)*cols] + [0])
bitmap.append([0] * (cols+1))

print_bitmap(bitmap, rows+2, cols+1)

for row in range(rows):
    for col in range(cols):
        if bitmap[row][col]:
            result += find_rectangle(bitmap, row, col)
            result += find_parallelogram(bitmap, row, col)

print_bitmap(bitmap, rows+2, cols+1)


result.sort()

# NO LINEFEED
sys.stdout.write(", ".join(result))
