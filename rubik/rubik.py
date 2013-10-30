#!/usr/bin/python

import sys

class Rubik():

    sq = 3
    sqrange = range(sq)
    order = ['u', 'l', 'f', 'r', 'b', 'd']
    label = {
                'u': 'Up',
                'l': 'Left',
                'f': 'Front',
                'r': 'Right',
                'b': 'Back',
                'd': 'Down',
              }

    def __init__(self, up, left, front, right, back, down):
        self.u = [ [ up for i in Rubik.sqrange ] for j in Rubik.sqrange ]
        self.l = [ [ left for i in Rubik.sqrange ] for j in Rubik.sqrange ]
        self.f = [ [ front for i in Rubik.sqrange ] for j in Rubik.sqrange ]
        self.r = [ [ right for i in Rubik.sqrange ] for j in Rubik.sqrange ]
        self.b = [ [ back for i in Rubik.sqrange ] for j in Rubik.sqrange ]
        self.d = [ [ down for i in Rubik.sqrange ] for j in Rubik.sqrange ]


    def move_f(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.f)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.u[2][i]
                self.u[2][i] = self.l[j][2]
                self.l[j][2] = self.d[0][j]
                self.d[0][j] = self.r[i][0]
                self.r[i][0] = temp[i]
        else:
            for i in range(3):
                self.move_f()
            

    def move_b(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.b)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.d[2][i]
                self.d[2][i] = self.l[i][0]
                self.l[i][0] = self.u[0][j]
                self.u[0][j] = self.r[j][2]
                self.r[j][2] = temp[i]
        else:
            for i in range(3):
                self.move_b()

    def move_u(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.u)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.b[2][i]
                self.b[2][i] = self.l[0][j]
                self.l[0][j] = self.f[0][j]
                self.f[0][j] = self.r[0][j]
                self.r[0][j] = temp[i]
        else:
            for i in range(3):
                self.move_u()

    def move_d(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.d)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.f[2][i]
                self.f[2][i] = self.l[2][i]
                self.l[2][i] = self.b[0][j]
                self.b[0][j] = self.r[2][i]
                self.r[2][i] = temp[i]
        else:
            for i in range(3):
                self.move_d()

    def move_l(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.l)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.u[i][0]
                self.u[i][0] = self.b[i][0]
                self.b[i][0] = self.d[i][0]
                self.d[i][0] = self.f[i][0]
                self.f[i][0] = temp[i]
        else:
            for i in range(3):
                self.move_l()

    def move_r(self, reverse=False):
        temp = Rubik.sqrange[:]
        if not reverse:
            pivot(self.r)
            for i in Rubik.sqrange:
                j = Rubik.sq - 1 - i
                temp[i] = self.u[j][2]
                self.u[j][2] = self.f[j][2]
                self.f[j][2] = self.d[j][2]
                self.d[j][2] = self.b[j][2]
                self.b[j][2] = temp[i]
        else:
            for i in range(3):
                self.move_r()

    def parse_instructions(self, line):
        line = "%s_" % line.lower()
        last = count = reverse = None
        commands = Rubik.order + ['_']
        #print >> sys.stderr, "Line:", line, "Commands:", commands
        for c in list(line):
            #print >> sys.stderr, "c='%s' command='%s' last='%s' reverse='%s' count='%s'" % (c,line,last,reverse,count)
            if c in commands:
                if last:
                    for i in range(count):
                        getattr(self, "move_%s" % last)(reverse=reverse)
                last = c
                reverse = False
                count = 1
            elif c.isdigit() and '2' == c:
                count = 2
            elif "'" == c:
                reverse = not reverse
            elif " " == c:
                next
            #else:
                #print >> sys.stderr, "Parse error on c='%s'!" % c

    def side_to_string(self, side='f', formatted=False):
        values = getattr(self, side)
        output = []
        for i in Rubik.sqrange:
            output.append(" ".join(values[i]))
        return "\n".join(output)

    def printme(self):
        for key in Rubik.order:
            print Rubik.label[key]
            side = getattr(self, key)
            print "   0 1 2"
            for i in Rubik.sqrange:
                print i, repr(side[i]).replace(",", "").replace("'", "")
            print

    def export(self):
        return [self.u, self.l, self.f, self.r, self.b, self.d]


def pivot(side):
    temp = side[0][0]
    side[0][0] = side[2][0]
    side[2][0] = side[2][2]
    side[2][2] = side[0][2]
    side[0][2] = temp

    temp = side[0][1]
    side[0][1] = side[1][0]
    side[1][0] = side[2][1]
    side[2][1] = side[1][2]
    side[1][2] = temp



if __name__ == "__main__":
    pattern = raw_input()
    r = Rubik(*list(pattern))
    instructions = raw_input()
    r.parse_instructions(instructions)
    print r.side_to_string(side='f')
    #r.printme()
