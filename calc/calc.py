#!/usr/bin/python

import sys


def get_line(size, i, char, symbol="#", space=" "):
    if '-' == char:
        if i == size // 2:
            return symbol * size
        else:
            return space * size
    elif '1' == char:
        if i == 0:
            return space * (size // 2) + symbol + space * (size // 2)
        elif i < size // 2:
            return space * (size // 2 - i) + symbol + space * (i - 1) + symbol + space * (size // 2)
        elif i == size - 1:
            return symbol * size
        else:
            return space * (size // 2) + symbol + space * (size // 2)
    elif '2' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        elif i < size // 2:
            return space * (size - 1) + symbol
        else:
            return symbol + space * (size - 1)
    elif '3' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        else:
            return space * (size - 1) + symbol
    elif '4' == char:
        if i < size // 2:
            return symbol + space * (size - 2) + symbol
        elif i == size // 2:
            return symbol * size
        else:
            return space * (size - 1) + symbol
    elif '5' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        elif i < size // 2:
            return symbol + space * (size - 1)
        else:
            return space * (size - 1) + symbol
    elif '6' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        elif i < size // 2:
            return symbol + space * (size - 1)
        else:
            return symbol + space * (size - 2) + symbol
    elif '7' == char:
        if i == 0:
            return symbol * size
        else:
            return space * (size - 1 - i) + symbol + space * i
    elif '8' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        else:
            return symbol + space * (size - 2) + symbol
    elif '9' == char:
        if i in [0, size // 2, size-1]:
            return symbol * size
        elif i < size // 2:
            return symbol + space * (size - 2) + symbol
        else:
            return space * (size - 1) + symbol
    elif '0' == char:
        if i in [0, size-1]:
            return symbol * size
        else:
            return symbol + space * (size - 2) + symbol
    elif '_*' == char:
        if i in [0, size-1]:
            return space * size
        else:
            return space + "*" * (size - 2) + space
    elif '_/' == char:
        return space * (size - i - 1) + '/' + space * i
    elif '_+' == char:
        if i in [0, size-1]:
            return space * size 
        elif i == size // 2:
            return "+" * size
        else:
            return space * (size // 2) + "+" + space * (size // 2)
    elif '_-' == char:
        if i == size // 2:
            return '-' * size
        else:
            return space * size
    elif '_%' == char:
        square = size // 4
        if i < square:
            return '%' * square + space * (size - square - 1 - i) + '%' + space * i
        elif i > (size - square - 1):
            return space * (size - 1 - i) + '%' + space * (i - square) + '%' * square
        else:
            return space * (size - i - 1) + '%' + space * i


def get_word_line(word, gap):
    return "".join([get_line(size, i, c, outputc) + " " * gap for c in list(str(word))])[:-gap]

def get_spacer_line(char=" "):
    return char * (total_width - gaps)




left = int(raw_input())
right = int(raw_input())
operator = raw_input()
outputc = raw_input()
size = int(raw_input())
gaps = int(raw_input())
result = None

#print >> sys.stderr, "%s %s %s, %s at %s w/ %s" % (left, operator, right, outputc, size, gaps)


if '+' == operator:
    result = left + right    
elif '-' == operator:
    result = left - right
elif '*' == operator:
    result = left * right
elif '/' == operator:
    result = left // right
elif '%' == operator:
    result = left % right
else:
    print >> sys.stderr, "Invalid operator '%s'!" % (operator,)


# test printing all chars (DEBUGGG)
#for c in ['-','0','1','2','3','4','5','6','7','8','9','_+','_-','_*','_/','_%',]:
#    for i in range(size):
#        print get_line(size, i, c)
#    print

left_width = (size + gaps) * len(str(left))
right_width = (size + gaps) * len(str(right))
result_width = (size + gaps) * len(str(result))
operator_width = size

largest_width = 0
for width in [left_width, right_width, result_width]:
    if width > largest_width:
        largest_width = width

total_width = operator_width + gaps + largest_width

for i in range(size):
    print " " * (total_width - left_width) + get_word_line(left, gaps)

print get_spacer_line(" ")

for i in range(size):
    print get_line(size, i, "_%s" % operator) + " " * (total_width - operator_width - right_width) + get_word_line(right, gaps)
    
print get_spacer_line(" ")
print get_spacer_line("-")
print get_spacer_line(" ")

for i in range(size):
    print " " * (total_width - result_width) + get_word_line(result, gaps)


