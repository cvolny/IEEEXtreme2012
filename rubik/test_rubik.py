#!/usr/bin/python

from rubik import Rubik
import unittest
import copy

class TestRubik(unittest.TestCase):

    def setUp(self):
        self.rubik = Rubik(*list("YRBOGW"))

    def test_export(self):
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_f(self):
        self.rubik.move_f()
        g = [
                #[self.up, self.left, self.front, self.right, self.back, self.down]
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['R', 'R', 'R']], # up
                [['R', 'R', 'W'],['R', 'R', 'W'],['R', 'R', 'W']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['Y', 'O', 'O'],['Y', 'O', 'O'],['Y', 'O', 'O']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['O', 'O', 'O'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_f_reverse(self):
        self.rubik.move_f(reverse=True)
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['O', 'O', 'O']], # up
                [['R', 'R', 'Y'],['R', 'R', 'Y'],['R', 'R', 'Y']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['W', 'O', 'O'],['W', 'O', 'O'],['W', 'O', 'O']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['R', 'R', 'R'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_b(self):
        self.rubik.move_b()
        g = [
                [['O', 'O', 'O'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['Y', 'R', 'R'],['Y', 'R', 'R'],['Y', 'R', 'R']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['O', 'O', 'W'],['O', 'O', 'W'],['O', 'O', 'W']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['R', 'R', 'R']], # down
            ]
        self.assertEqual(self.rubik.export(),g)
    
    def test_move_b_reverse(self):
        self.rubik.move_b(reverse=True)
        g = [
                [['R', 'R', 'R'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['W', 'R', 'R'],['W', 'R', 'R'],['W', 'R', 'R']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['O', 'O', 'Y'],['O', 'O', 'Y'],['O', 'O', 'Y']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['O', 'O', 'O']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_u(self):
        self.rubik.move_u()
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['B', 'B', 'B'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['O', 'O', 'O'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['G', 'G', 'G'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['R', 'R', 'R']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_u_reverse(self):
        self.rubik.move_u(reverse=True)
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['G', 'G', 'G'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['R', 'R', 'R'],['B', 'B', 'B'],['B', 'B', 'B']], # front
                [['B', 'B', 'B'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['G', 'G', 'G'],['G', 'G', 'G'],['O', 'O', 'O']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_d(self):
        self.rubik.move_d()
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['G', 'G', 'G']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['R', 'R', 'R']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['B', 'B', 'B']], # right
                [['O', 'O', 'O'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_d_reverse(self):
        self.rubik.move_d(reverse=True)
        g = [
                [['Y', 'Y', 'Y'],['Y', 'Y', 'Y'],['Y', 'Y', 'Y']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['B', 'B', 'B']], # left
                [['B', 'B', 'B'],['B', 'B', 'B'],['O', 'O', 'O']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['G', 'G', 'G']], # right
                [['R', 'R', 'R'],['G', 'G', 'G'],['G', 'G', 'G']], # back
                [['W', 'W', 'W'],['W', 'W', 'W'],['W', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_l(self):
        self.rubik.move_l()
        g = [
                [['G', 'Y', 'Y'],['G', 'Y', 'Y'],['G', 'Y', 'Y']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['Y', 'B', 'B'],['Y', 'B', 'B'],['Y', 'B', 'B']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['W', 'G', 'G'],['W', 'G', 'G'],['W', 'G', 'G']], # back
                [['B', 'W', 'W'],['B', 'W', 'W'],['B', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_l_reverse(self):
        self.rubik.move_l(reverse=True)
        g = [
                [['B', 'Y', 'Y'],['B', 'Y', 'Y'],['B', 'Y', 'Y']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['W', 'B', 'B'],['W', 'B', 'B'],['W', 'B', 'B']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['Y', 'G', 'G'],['Y', 'G', 'G'],['Y', 'G', 'G']], # back
                [['G', 'W', 'W'],['G', 'W', 'W'],['G', 'W', 'W']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_r(self):
        self.rubik.move_r()
        g = [
                [['Y', 'Y', 'B'],['Y', 'Y', 'B'],['Y', 'Y', 'B']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['B', 'B', 'W'],['B', 'B', 'W'],['B', 'B', 'W']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['G', 'G', 'Y'],['G', 'G', 'Y'],['G', 'G', 'Y']], # back
                [['W', 'W', 'G'],['W', 'W', 'G'],['W', 'W', 'G']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_move_r_reverse(self):
        self.rubik.move_r(reverse=True)
        g = [
                [['Y', 'Y', 'G'],['Y', 'Y', 'G'],['Y', 'Y', 'G']], # up
                [['R', 'R', 'R'],['R', 'R', 'R'],['R', 'R', 'R']], # left
                [['B', 'B', 'Y'],['B', 'B', 'Y'],['B', 'B', 'Y']], # front
                [['O', 'O', 'O'],['O', 'O', 'O'],['O', 'O', 'O']], # right
                [['G', 'G', 'W'],['G', 'G', 'W'],['G', 'G', 'W']], # back
                [['W', 'W', 'B'],['W', 'W', 'B'],['W', 'W', 'B']], # down
            ]
        self.assertEqual(self.rubik.export(),g)

    def test_parse_instructions_forward(self):
        r = self.rubik
        g = copy.deepcopy(r)
        # adjust r
        r.move_f()
        r.move_b()
        r.move_u()
        r.move_d()
        r.move_l()
        r.move_r()
        r.move_f()
        r.move_b()
        r.move_u()
        r.move_d()
        r.move_l()
        r.move_r()
        # adjust g
        g.parse_instructions("FBUDLRFBUDLR")
        self.assertEqual(r.export(),g.export())

    def test_parse_instructions_reverse(self):
        r = self.rubik
        g = copy.deepcopy(r)
        # adjust r
        r.move_f(reverse=True)
        r.move_b(reverse=True)
        r.move_u(reverse=True)
        r.move_d(reverse=True)
        r.move_l(reverse=True)
        r.move_r(reverse=True)
        # adjust g
        g.parse_instructions("F'B'U'D'L'R'")

        self.assertEqual(r.export(),g.export())

    def test_parse_instructions_twos(self):
        r = self.rubik
        g = copy.deepcopy(r)
        # adjust r
        r.move_f()
        r.move_f()
        r.move_b()
        r.move_b()
        r.move_u()
        r.move_u()
        r.move_d()
        r.move_d()
        r.move_l()
        r.move_l()
        r.move_r()
        r.move_r()
        # adjust g
        g.parse_instructions("F2B2U2D2L2R2")

        self.assertEqual(r.export(),g.export())

    def test_expected(self):
        rubrik1 = Rubik(*list("YRBOGW"))
        rubrik1.parse_instructions("R2")
        self.assertEqual(rubrik1.side_to_string(side='f'), "B B G\nB B G\nB B G")

        rubrik2 = Rubik(*list("YORBWG"))
        rubrik2.parse_instructions("RL'")
        self.assertEqual(rubrik2.side_to_string(side='f'), "G R G\nG R G\nG R G")

    def test_complex_steps(self):
        
        r = Rubik(*list("WGOYRB"))
        self.assertEqual(r.side_to_string(side='u'), "W W W\nW W W\nW W W")
        r.move_l()
        self.assertEqual(r.side_to_string(side='f'), "W O O\nW O O\nW O O")
        self.assertEqual(r.side_to_string(side='u'), "R W W\nR W W\nR W W")
        r.move_b()
        self.assertEqual(r.side_to_string(side='l'), "W G G\nW G G\nR G G")
        self.assertEqual(r.side_to_string(side='u'), "Y Y Y\nR W W\nR W W")
        r.move_u(reverse=True)
        self.assertEqual(r.side_to_string(side='f'), "W G G\nW O O\nW O O")
        self.assertEqual(r.side_to_string(side='u'), "Y W W\nY W W\nY R R")
        r.move_d(reverse=True)
        self.assertEqual(r.side_to_string(side='f'), "W G G\nW O O\nY Y O")
        self.assertEqual(r.side_to_string(side='u'), "Y W W\nY W W\nY R R")
        r.move_b(reverse=True)
        self.assertEqual(r.side_to_string(side='u'), "W W R\nY W W\nY R R")

if __name__ == '__main__':
    unittest.main()
