import unittest
import solutions.ap1 as ap1

class TestAP1(unittest.TestCase):
    def test_scores_increasing(self):
        self.assertEqual(ap1.scores_increasing([1, 3, 4]), True)
        self.assertEqual(ap1.scores_increasing([1, 3, 2]), False)
        self.assertEqual(ap1.scores_increasing([1, 1, 4]), True)
        self.assertEqual(ap1.scores_increasing([1, 1, 2, 4, 4, 7]), True)
        self.assertEqual(ap1.scores_increasing([1, 1, 2, 4, 3, 7]), False)
        self.assertEqual(ap1.scores_increasing([-5, 4, 11]), True)
    
    def test_scores_100(self):
        self.assertEqual(ap1.scores_100([1, 100, 100]), True)
        self.assertEqual(ap1.scores_100([1, 100, 99, 100]), False)
        self.assertEqual(ap1.scores_100([100, 1, 100, 100]), True)
        self.assertEqual(ap1.scores_100([100, 1, 100, 1]), False)
        self.assertEqual(ap1.scores_100([1, 2, 3, 4, 5]), False)
        self.assertEqual(ap1.scores_100([1, 2, 100, 4, 5]), False)

    def test_scores_clump(self):
        self.assertEqual(ap1.scores_clump([3, 4, 5]), True)
        self.assertEqual(ap1.scores_clump([3, 4, 6]), False)
        self.assertEqual(ap1.scores_clump([1, 3, 5, 5]), True)
        self.assertEqual(ap1.scores_clump([2, 4, 5, 6]), True)
        self.assertEqual(ap1.scores_clump([2, 4, 5, 7]), False)
        self.assertEqual(ap1.scores_clump([2, 4, 4, 7]), True)
        self.assertEqual(ap1.scores_clump([3, 3, 6, 7, 9]), False)
        self.assertEqual(ap1.scores_clump([3, 3, 7, 7, 9]), True)
        self.assertEqual(ap1.scores_clump([4, 5, 8]), False)
    
    def test_scores_average(self):
        self.assertEqual(ap1.scores_average([2, 2, 4, 4]), 4)
        self.assertEqual(ap1.scores_average([4, 4, 4, 2, 2, 2]), 4)
        self.assertEqual(ap1.scores_average([3, 4, 5, 1, 2, 3]), 4)
        self.assertEqual(ap1.scores_average([5, 6]), 6)
        self.assertEqual(ap1.scores_average([5, 4]), 5)
        self.assertEqual(ap1.scores_average([5, 4, 5, 6, 2, 1, 2, 3]), 5)

    def test_words_count(self):
        self.assertEqual(ap1.words_count(["a", "bb", "b", "ccc"], 1), 2)
        self.assertEqual(ap1.words_count(["a", "bb", "b", "ccc"], 3), 1)
        self.assertEqual(ap1.words_count(["a", "bb", "b", "ccc"], 4), 0)
        self.assertEqual(ap1.words_count(["xx", "yyy", "x", "yy", "z"], 1), 2)
        self.assertEqual(ap1.words_count(["xx", "yyy", "x", "yy", "z"], 2), 2)
        self.assertEqual(ap1.words_count(["xx", "yyy", "x", "yy", "z"], 3), 1)
    
    def test_words_front(self):
        self.assertEqual(ap1.words_front(["a", "b", "c", "d"], 1), ["a"])
        self.assertEqual(ap1.words_front(["a", "b", "c", "d"], 2), ["a", "b"])
        self.assertEqual(ap1.words_front(["a", "b", "c", "d"], 3), ["a", "b", "c"])
        self.assertEqual(ap1.words_front(["a", "b", "c", "d"], 4),  ["a", "b", "c", "d"])
        self.assertEqual(ap1.words_front(["Hi", "There"], 1), ["Hi"])
        self.assertEqual(ap1.words_front(["Hi", "There"], 2), ["Hi", "There"])
    
    def test_words_without_list(self):
        self.assertEqual(ap1.words_without_list(["a", "bb", "b", "ccc"], 1), ["bb", "ccc"])
        self.assertEqual(ap1.words_without_list(["a", "bb", "b", "ccc"], 3), ["a", "bb", "b"])
        self.assertEqual(ap1.words_without_list(["a", "bb", "b", "ccc"], 4), ["a", "bb", "b", "ccc"])
        self.assertEqual(ap1.words_without_list(["xx", "yyy", "x", "yy", "z"], 1), ["xx", "yyy", "yy"])
        self.assertEqual(ap1.words_without_list(["xx", "yyy", "x", "yy", "z"], 2), ["yyy", "x", "z"])
    
    def test_has_one(self):
        self.assertEqual(ap1.has_one(10), True)
        self.assertEqual(ap1.has_one(22), False)
        self.assertEqual(ap1.has_one(220), False)
        self.assertEqual(ap1.has_one(212), True)
        self.assertEqual(ap1.has_one(1), True)
        self.assertEqual(ap1.has_one(9), False)
        self.assertEqual(ap1.has_one(211112), True)
        self.assertEqual(ap1.has_one(121121), True)
        self.assertEqual(ap1.has_one(222222), False)
        self.assertEqual(ap1.has_one(56156), True)
        self.assertEqual(ap1.has_one(56556), False)
    
    def test_divides_self(self):
        self.assertEqual(ap1.divides_self(128), True)
        self.assertEqual(ap1.divides_self(12), True)
        self.assertEqual(ap1.divides_self(120), False)
        self.assertEqual(ap1.divides_self(122), True)
        self.assertEqual(ap1.divides_self(13), False)
        self.assertEqual(ap1.divides_self(32), False)
        self.assertEqual(ap1.divides_self(22), True)
        self.assertEqual(ap1.divides_self(42), False)
        self.assertEqual(ap1.divides_self(212), True)
        self.assertEqual(ap1.divides_self(213), False)
        self.assertEqual(ap1.divides_self(162), True)
    
    def test_copy_evens(self):
        self.assertEqual(ap1.copy_evens([3, 2, 4, 5, 8], 2), [2, 4])
        self.assertEqual(ap1.copy_evens([3, 2, 4, 5, 8], 3), [2, 4, 8])
        self.assertEqual(ap1.copy_evens([6, 1, 2, 4, 5, 8], 3), [6, 2, 4])
        self.assertEqual(ap1.copy_evens([6, 1, 2, 4, 5, 8], 4), [6, 2, 4, 8])
        self.assertEqual(ap1.copy_evens([3, 1, 4, 1, 5], 1), [4])
        self.assertEqual(ap1.copy_evens([2], 1), [2])
        self.assertEqual(ap1.copy_evens([6, 2, 4, 8], 2), [6, 2])
        self.assertEqual(ap1.copy_evens([6, 2, 4, 8], 3), [6, 2, 4])
        self.assertEqual(ap1.copy_evens([6, 2, 4, 8], 4), [6, 2, 4, 8])
        self.assertEqual(ap1.copy_evens([1, 8, 4], 1), [8])
        self.assertEqual(ap1.copy_evens([1, 8, 4], 2), [8, 4])
        self.assertEqual(ap1.copy_evens([2, 8, 4], 2), [2, 8])
    
    def test_copy_endy(self):
        self.assertEqual(ap1.copy_endy(), )
    
    def test_match_up(self):
        self.assertEqual(ap1.match_up(), )
    
    def test_score_up(self):
        self.assertEqual(ap1.score_up(), )
    
    def test_words_without(self):
        self.assertEqual(ap1.words_without(), )
    
    def test_scores_special(self):
        self.assertEqual(ap1.scores_special(), )
    
    def test_sum_heights(self):
        self.assertEqual(ap1.sum_heights(), )
    
    def test_sum_heights_2(self):
        self.assertEqual(ap1.sum_heights(), )
    
    def test_big_heights(self):
        self.assertEqual(ap1.big_heights(), )
    
    def test_user_compare(self):
        self.assertEqual(ap1.user_compare(), )
    
    def test_merge_two(self):
        self.assertEqual(ap1.merge_two(), )
    
    def test_common_two(self):
        self.assertEqual(ap1.common_two(), )

if __name__ == '__main__':
    unittest.main()