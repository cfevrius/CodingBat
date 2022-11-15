import sys
sys.path.append('')

import unittest
import solutions.array1 as array1

class TestArray1(unittest.TestCase):
    def test_first_last_6(self):
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
        self.assertEqual(array1.first_last_6([]), )
    
    def test_same_first_last(self):
        self.assertEqual(array1.same_first_last([]), )

    def test_make_pi(self):
        self.assertEqual(array1.make_pi([]), )
    
    def test_common_end(self):
        self.assertEqual(array1.common_end([]), )

    def test_sum_3(self):
        self.assertEqual(array1.sum3([]), )

    def test_rotate_left_3(self):
        self.assertEqual(array1.rotate_left3([]), )

    def test_reverse_3(self):
        self.assertEqual(array1.reverse3([]), )

    def test_max_end_3(self):
        self.assertEqual(array1.test_max_end3([]), )

    def test_sum_2(self):
        self.assertEqual(array1.test_sum_2([]), )
    
    def test_middle_way(self):
        self.assertEqual(array1.middle_way)

    def test_make_ends(self):
        self.assertEqual(array1.make_ends())
    
    def test_has_23(self):
        self.assertEqual(array1.has_23())
    
    def test_no_23(self):
        self.assertEqual(array1.no_23())
    
    def test_make_last(self):
        self.assertEqual(array1.make_last())

    def test_double_23(self):
        self.assertEqual(array1.double_23())
    
    def test_fix_23(self):
        self.assertEqual(array1.fix_23())
    
    def test_start_1(self):
        self.assertEqual(array1.start_1())

    def test_bigger_two(self):
        self.assertEqual(array1.bigger_two())

    def test_make_middle(self):
        self.assertEqual(array1.make_middle())

    def test_plus_two(self):
        self.assertEqual(array1.plus_two())
    
    def test_swap_ends(self):
        self.assertEqual(array1.swap_ends())
    
    def test_mid_three(self):
        self.assertEqual(array1.mid_three())
    
    def test_max_triple(self):
        self.assertEqual(array1.max_triple())

    def test_front_piece(self):
        self.assertEqual(array1.front_piece())

    def test_unlucky_1(self):
        self.assertEqual(array1.unlucky_1())
    
    def test_make_2(self):
        self.assertEqual(array1.make_2())
    
    def test_front_11(self):
        self.assertEqual(array1.front_11())

if __name__ == '__main__':
    unittest.main()