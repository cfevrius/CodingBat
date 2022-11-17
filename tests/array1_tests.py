import sys
sys.path.append('')

import unittest
import solutions.array1 as array1

class TestArray1(unittest.TestCase):
    def test_first_last_6(self):
        self.assertEqual(array1.first_last_6([1, 2, 6]), True)
        self.assertEqual(array1.first_last_6([6, 1, 2, 3]), True)
        self.assertEqual(array1.first_last_6([13, 6, 1, 2, 3]), False)
        self.assertEqual(array1.first_last_6([13, 6, 1, 2, 6]), True)
        self.assertEqual(array1.first_last_6([3, 2, 1]), False)
        self.assertEqual(array1.first_last_6([3, 6, 1]), False)
        self.assertEqual(array1.first_last_6([3, 6]), True)
        self.assertEqual(array1.first_last_6([6]), True)
        self.assertEqual(array1.first_last_6([3]), False)
        self.assertEqual(array1.first_last_6([5, 6]), True)
        self.assertEqual(array1.first_last_6([5, 5]), False)
        self.assertEqual(array1.first_last_6([1, 2, 3, 4, 6]), True)
        self.assertEqual(array1.first_last_6([1, 2, 3, 4]), False)
    
    def test_same_first_last(self):
        self.assertEqual(array1.same_first_last([1, 2, 3]), False)
        self.assertEqual(array1.same_first_last([1, 2, 3, 1]), True)
        self.assertEqual(array1.same_first_last([1, 2, 1]), True)
        self.assertEqual(array1.same_first_last([7]), True)
        self.assertEqual(array1.same_first_last([]), False)
        self.assertEqual(array1.same_first_last([1, 2, 3, 4, 5, 1]), True)
        self.assertEqual(array1.same_first_last([1, 2, 3, 4, 5, 13]), False)
        self.assertEqual(array1.same_first_last([13, 2, 3, 4, 5, 13]), True)
        self.assertEqual(array1.same_first_last([7, 7]), True)

    def test_make_pi(self):
        self.assertEqual(array1.make_pi(), [3, 1, 4])
    
    def test_common_end(self):
        self.assertEqual(array1.common_end([1, 2, 3], [7, 3]), True)
        self.assertEqual(array1.common_end([1, 2, 3], [7, 3, 2]), False)
        self.assertEqual(array1.common_end([1, 2, 3], [1, 3]), True)
        self.assertEqual(array1.common_end([1, 2, 3], [1]), True)
        self.assertEqual(array1.common_end([1, 2, 3], [2]), False)

    def test_sum_3(self):
        self.assertEqual(array1.sum3([1, 2, 3]), 6)
        self.assertEqual(array1.sum3([5, 11, 2]), 18)
        self.assertEqual(array1.sum3([7, 0, 0]),  7)
        self.assertEqual(array1.sum3([1, 2, 1]), 4)
        self.assertEqual(array1.sum3([1, 1, 1]), 3)
        self.assertEqual(array1.sum3([2, 7, 2]), 11)

    def test_rotate_left_3(self):
        self.assertEqual(array1.rotate_left_3([1, 2, 3]), [2, 3, 1])
        self.assertEqual(array1.rotate_left_3([5, 11, 9]), [11, 9, 5])
        self.assertEqual(array1.rotate_left_3([7, 0, 0]), [0, 0, 7])
        self.assertEqual(array1.rotate_left_3([1, 2, 1]), [2, 1, 1])
        self.assertEqual(array1.rotate_left_3([0, 0, 1]), [0, 1, 0])

    def test_reverse_3(self):
        self.assertEqual(array1.reverse_3([1, 2, 3]), [3, 2, 1])
        self.assertEqual(array1.reverse_3([5, 11, 9]), [9, 11, 5])
        self.assertEqual(array1.reverse_3([7, 0, 0]), [0, 0, 7])
        self.assertEqual(array1.reverse_3([2, 1, 2]), [2, 1, 2])
        self.assertEqual(array1.reverse_3([1, 2, 1]), [1, 2, 1])
        self.assertEqual(array1.reverse_3([2, 11, 3]), [3, 11, 2])
        self.assertEqual(array1.reverse_3([0, 6, 5]), [5, 6, 0])
        self.assertEqual(array1.reverse_3([7, 2, 3]), [3, 2, 7])

    def test_max_end_3(self):
        self.assertEqual(array1.max_end_3([1, 2, 3]), [3, 3, 3])
        self.assertEqual(array1.max_end_3([11, 5, 9]), [11, 11, 11])
        self.assertEqual(array1.max_end_3([2, 11, 3]), [3, 3, 3])
        self.assertEqual(array1.max_end_3([11, 3, 3]), [11, 11, 11])
        self.assertEqual(array1.max_end_3([3, 11, 11]),  [11, 11, 11])
        self.assertEqual(array1.max_end_3([2, 2, 2]), [2, 2, 2])
        self.assertEqual(array1.max_end_3([2, 11, 2]), [2, 2, 2])
        self.assertEqual(array1.max_end_3([0, 0, 1]), [1, 1, 1])

    def test_sum_2(self):
        self.assertEqual(array1.sum_2([1, 2, 3]), 3)
        self.assertEqual(array1.sum_2([1, 1]), 2)
        self.assertEqual(array1.sum_2([1, 1, 1, 1]), 2)
        self.assertEqual(array1.sum_2([1, 2]), 3)
        self.assertEqual(array1.sum_2([1]), 1)
        self.assertEqual(array1.sum_2([]), 0)
        self.assertEqual(array1.sum_2([4, 5, 6]), 9)
        self.assertEqual(array1.sum_2([4]), 4)
    
    def test_middle_way(self):
        self.assertEqual(array1.middle_way([1, 2, 3], [4, 5, 6]), [2, 5])
        self.assertEqual(array1.middle_way([7, 7, 7], [3, 8, 0]), [7, 8])
        self.assertEqual(array1.middle_way([5, 2, 9], [1, 4, 5]), [2, 4])
        self.assertEqual(array1.middle_way([1, 9, 7], [4, 8, 8]), [9, 8])
        self.assertEqual(array1.middle_way([1, 2, 3], [3, 1, 4]), [2, 1])
        self.assertEqual(array1.middle_way([1, 2, 3], [4, 1, 1]), [2, 1])

    def test_make_ends(self):
        self.assertEqual(array1.make_ends([1, 2, 3]), [1, 3])
        self.assertEqual(array1.make_ends([1, 2, 3, 4]), [1, 4])
        self.assertEqual(array1.make_ends([7, 4, 6, 2]), [7, 2])
        self.assertEqual(array1.make_ends([1, 2, 2, 2, 2, 2, 2, 3]), [1, 3])
        self.assertEqual(array1.make_ends([7, 4]), [7, 4])
        self.assertEqual(array1.make_ends([7]), [7, 7])
        self.assertEqual(array1.make_ends([5, 2, 9]), [5, 9])
        self.assertEqual(array1.make_ends([2, 3, 4, 1]), [2, 1])
    
    def test_has_2_3(self):
        self.assertEqual(array1.has_2_3([2, 5]), True)
        self.assertEqual(array1.has_2_3([4, 3]), True)
        self.assertEqual(array1.has_2_3([4, 5]), False)
        self.assertEqual(array1.has_2_3([2, 2]), True)
        self.assertEqual(array1.has_2_3([3, 2]), True)
        self.assertEqual(array1.has_2_3([3, 3]), True)
        self.assertEqual(array1.has_2_3([7, 7]), False)
        self.assertEqual(array1.has_2_3([3, 9]), True)
        self.assertEqual(array1.has_2_3([9, 5]), False)
    
    def test_no_2_3(self):
        self.assertEqual(array1.no_2_3([4, 5]), True)
        self.assertEqual(array1.no_2_3([4, 2]), False)
        self.assertEqual(array1.no_2_3([3, 5]), False)
        self.assertEqual(array1.no_2_3([1, 9]), True)
        self.assertEqual(array1.no_2_3([2, 9]), False)
        self.assertEqual(array1.no_2_3([1, 3]), False)
        self.assertEqual(array1.no_2_3([1, 1]), True)
        self.assertEqual(array1.no_2_3([2, 2]), False)
        self.assertEqual(array1.no_2_3([3, 3]), False)
        self.assertEqual(array1.no_2_3([7, 8]), True)
        self.assertEqual(array1.no_2_3([8, 7]), True)
    
    def test_make_last(self):
        self.assertEqual(array1.make_last([4, 5, 6]), [0, 0, 0, 0, 0, 6])
        self.assertEqual(array1.make_last([1, 2]), [0, 0, 0, 2])
        self.assertEqual(array1.make_last([3]), [0, 3])
        self.assertEqual(array1.make_last([0]), [0, 0])
        self.assertEqual(array1.make_last([7, 7, 7]), [0, 0, 0, 0, 0, 7])
        self.assertEqual(array1.make_last([3, 1, 4]), [0, 0, 0, 0, 0, 4])
        self.assertEqual(array1.make_last([1, 2, 3, 4]),  [0, 0, 0, 0, 0, 0, 0, 4])
        self.assertEqual(array1.make_last([1, 2, 3, 0]), [0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(array1.make_last([2, 4]), [0, 0, 0, 4])

    def test_double_2_3(self):
        self.assertEqual(array1.double_2_3([2, 2]), True)
        self.assertEqual(array1.double_2_3([3, 3]), True)
        self.assertEqual(array1.double_2_3([2, 3]), False)
        self.assertEqual(array1.double_2_3([3, 2]), False)
        self.assertEqual(array1.double_2_3([4, 5]), False)
        self.assertEqual(array1.double_2_3([2]), False)
        self.assertEqual(array1.double_2_3([3]), False)
        self.assertEqual(array1.double_2_3([]), False)
        self.assertEqual(array1.double_2_3([3, 4]), False)
    
    def test_fix_23(self):
        self.assertEqual(array1.fix_23([]), [])
        self.assertEqual(array1.fix_23([]), [])
        self.assertEqual(array1.fix_23([]), [])
        self.assertEqual(array1.fix_23([]), [])
        self.assertEqual(array1.fix_23([]), [])
        self.assertEqual(array1.fix_23([]), [])
    
    def test_start_1(self):
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])
        self.assertEqual(array1.start_1([]), [])

    def test_bigger_two(self):
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])
        self.assertEqual(array1.bigger_two([], []), [])

    def test_make_middle(self):
        self.assertEqual(array1.make_middle([]), [])
        self.assertEqual(array1.make_middle([]), [])
        self.assertEqual(array1.make_middle([]), [])
        self.assertEqual(array1.make_middle([]), [])
        self.assertEqual(array1.make_middle([]), [])

    def test_plus_two(self):
        self.assertEqual(array1.plus_two([], []), [])
        self.assertEqual(array1.plus_two([], []), [])
        self.assertEqual(array1.plus_two([], []), [])
    
    def test_swap_ends(self):
        self.assertEqual(array1.swap_ends([]), [])
        self.assertEqual(array1.swap_ends([]), [])
        self.assertEqual(array1.swap_ends([]), [])
        self.assertEqual(array1.swap_ends([]), [])
        self.assertEqual(array1.swap_ends([]), [])
        self.assertEqual(array1.swap_ends([]), [])
    
    def test_mid_three(self):
        self.assertEqual(array1.mid_three([]), [])
        self.assertEqual(array1.mid_three([]), [])
        self.assertEqual(array1.mid_three([]), [])
    
    def test_max_triple(self):
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)
        self.assertEqual(array1.max_triple([]), 0)

    def test_front_piece(self):
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])
        self.assertEqual(array1.front_piece([]), [])

    def test_unlucky_1(self):
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
        self.assertEqual(array1.unlucky_1([]), False)
    
    def test_make_2(self):
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
        self.assertEqual(array1.make_2([], []), [])
    
    def test_front_11(self):
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])
        self.assertEqual(array1.front_11([], []), [])

if __name__ == '__main__':
    unittest.main()