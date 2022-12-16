import unittest
import solutions.recursion2 as recursion2

class TestRecursion2(unittest.TestCase):
    def test_group_sum(self):
        self.assertEqual(recursion2.group_sum(0, [2, 4, 8], 10), True)
        self.assertEqual(recursion2.group_sum(0, [2, 4, 8], 14), True)
        self.assertEqual(recursion2.group_sum(0, [2, 4, 8], 9), False)
        self.assertEqual(recursion2.group_sum(0, [2, 4, 8], 8), True)
        self.assertEqual(recursion2.group_sum(1, [2, 4, 8], 8), True)
        self.assertEqual(recursion2.group_sum(1, [2, 4, 8], 2), False)
        self.assertEqual(recursion2.group_sum(0, [1], 1), True)
        self.assertEqual(recursion2.group_sum(0, [9], 1), False)
        self.assertEqual(recursion2.group_sum(1, [9], 0), True)
        self.assertEqual(recursion2.group_sum(0, [], 0), True)
        self.assertEqual(recursion2.group_sum(0, [10, 2, 2, 5], 17), True)
        self.assertEqual(recursion2.group_sum(0, [10, 2, 2, 5], 15), True)
        self.assertEqual(recursion2.group_sum(0, [10, 2, 2, 5], 9), True)
    
    def test_group_sum_6(self):
        self.assertEqual(recursion2.group_sum_6(0, [5, 6, 2], 8), True)
        self.assertEqual(recursion2.group_sum_6(0, [5, 6, 2], 9), False)
        self.assertEqual(recursion2.group_sum_6(0, [5, 6, 2], 7), False)
        self.assertEqual(recursion2.group_sum_6(0, [1], 1), True)
        self.assertEqual(recursion2.group_sum_6(0, [9], 1), False)
        self.assertEqual(recursion2.group_sum_6(0, [], 0), True)
        self.assertEqual(recursion2.group_sum_6(0, [3, 2, 4, 6], 8), True)
        self.assertEqual(recursion2.group_sum_6(0, [6, 2, 4, 3], 8), True)
        self.assertEqual(recursion2.group_sum_6(0, [5, 2, 4, 6], 9), False)
        self.assertEqual(recursion2.group_sum_6(0, [6, 2, 4, 5], 9), False)
        self.assertEqual(recursion2.group_sum_6(0, [3, 2, 4, 6], 3), False)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 4], 12), True)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 4], 13), True)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 4], 4), False)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 4], 9), False)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 5], 14), True)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 5], 15), True)
        self.assertEqual(recursion2.group_sum_6(0, [1, 6, 2, 6, 5], 16), False)
    
    def test_group_no_adj(self):
        self.assertEqual(recursion2.group_no_adj(0, [2, 5, 10, 4], 12), True)
        self.assertEqual(recursion2.group_no_adj(0, [2, 5, 10, 4], 14), False)
        self.assertEqual(recursion2.group_no_adj(0, [2, 5, 10, 4], 7), False)
        self.assertEqual(recursion2.group_no_adj(0, [2, 5, 10, 4, 2], 7), True)
        self.assertEqual(recursion2.group_no_adj(0, [2, 5, 10, 4], 9), True)
        self.assertEqual(recursion2.group_no_adj(0, [10, 2, 2, 3, 3], 15), True)
        self.assertEqual(recursion2.group_no_adj(0, [10, 2, 2, 3, 3], 7), False)
        self.assertEqual(recursion2.group_no_adj(0, [], 0), True)
        self.assertEqual(recursion2.group_no_adj(0, [1], 1), True)
        self.assertEqual(recursion2.group_no_adj(0, [9], 1), False)
        self.assertEqual(recursion2.group_no_adj(0, [9], 0), True)
        self.assertEqual(recursion2.group_no_adj(0, [5, 10, 4, 1], 11), True)
    
    def test_group_sum5(self):
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 19), True)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 17), True)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 12), False)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 4, 10], 12), False)
        self.assertEqual(recursion2.group_sum_5(0, [3, 5, 1], 4), False)
        self.assertEqual(recursion2.group_sum_5(0, [3, 5, 1], 5), True)
        self.assertEqual(recursion2.group_sum_5(0, [1, 3, 5], 5), True)
        self.assertEqual(recursion2.group_sum_5(0, [3, 5, 1], 9), False)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 7), False)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 15), True)
        self.assertEqual(recursion2.group_sum_5(0, [2, 5, 10, 4], 11), False)
        self.assertEqual(recursion2.group_sum_5(0, [1], 1), True)
        self.assertEqual(recursion2.group_sum_5(0, [9], 1), False)
        self.assertEqual(recursion2.group_sum_5(0, [9], 0), True)
        self.assertEqual(recursion2.group_sum_5(0, [], 0), True)
    
    def test_group_sum_clump(self):
        self.assertEqual(recursion2.group_sum_clump(0, [2, 4, 8], 10), True)
        self.assertEqual(recursion2.group_sum_clump(0, [1, 2, 4, 8, 1], 14), True)
        self.assertEqual(recursion2.group_sum_clump(0, [2, 4, 4, 8], 14), False)
        self.assertEqual(recursion2.group_sum_clump(0, [8, 2, 2, 1], 9), True)
        self.assertEqual(recursion2.group_sum_clump(0, [8, 2, 2, 1], 11), False)
        self.assertEqual(recursion2.group_sum_clump(0, [1], 1), True)
        self.assertEqual(recursion2.group_sum_clump(0, [9], 1), False)
    
    def test_split_array(self):
        self.assertEqual(recursion2.split_array([2, 2]), True)
        self.assertEqual(recursion2.split_array([2, 3]), False)
        self.assertEqual(recursion2.split_array([5, 2, 3]), True)
        self.assertEqual(recursion2.split_array([5, 2, 2]), False)
        self.assertEqual(recursion2.split_array([1, 1, 1, 1, 1, 1]), True)
        self.assertEqual(recursion2.split_array([1, 1, 1, 1, 1]), False)
        self.assertEqual(recursion2.split_array([]), True)
        self.assertEqual(recursion2.split_array([1]), False)
        self.assertEqual(recursion2.split_array([3, 5]), False)
        self.assertEqual(recursion2.split_array([5, 3, 2]), True)
        self.assertEqual(recursion2.split_array([2, 2, 10, 10, 1, 1]), True)
        self.assertEqual(recursion2.split_array([1, 2, 2, 10, 10, 1, 1]), False)
        self.assertEqual(recursion2.split_array([1, 2, 3, 10, 10, 1, 1]), True)
    
    def test_split_odd_10(self):
        self.assertEqual(recursion2.split_odd_10([5, 5, 5]), True)
        self.assertEqual(recursion2.split_odd_10([5, 5, 6]), False)
        self.assertEqual(recursion2.split_odd_10([5, 5, 6, 1]), True)
        self.assertEqual(recursion2.split_odd_10([6, 5, 5, 1]), True)
        self.assertEqual(recursion2.split_odd_10([6, 5, 5, 1, 10]), True)
        self.assertEqual(recursion2.split_odd_10([6, 5, 5, 5, 1]), False)
        self.assertEqual(recursion2.split_odd_10([1]), True)
        self.assertEqual(recursion2.split_odd_10([]), False)
        self.assertEqual(recursion2.split_odd_10([10, 7, 5, 5]), True)
        self.assertEqual(recursion2.split_odd_10([10, 0, 5, 5]), False)
        self.assertEqual(recursion2.split_odd_10([10, 7, 5, 5, 2]), True)
        self.assertEqual(recursion2.split_odd_10([10, 7, 5, 5, 1]), False)
    
    def test_split_53(self):
        self.assertEqual(recursion2.split_53([1, 1]), True)
        self.assertEqual(recursion2.split_53([1, 1, 1]), False)
        self.assertEqual(recursion2.split_53([2, 4, 2]), True)
        self.assertEqual(recursion2.split_53([2, 2, 2, 1]), False)
        self.assertEqual(recursion2.split_53([3, 3, 5, 1]), True)
        self.assertEqual(recursion2.split_53([3, 5, 8]), False)
        self.assertEqual(recursion2.split_53([2, 4, 6]), True)
        self.assertEqual(recursion2.split_53([3, 5, 6, 10, 3, 3]), True)

if __name__ == '__main__':
    unittest.main()