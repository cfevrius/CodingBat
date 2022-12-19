import unittest
import source.functional2 as functional2

class TestFunctional2(unittest.TestCase):
    def test_no_neg(self):
        self.assertEqual(functional2.no_neg([1, -2]), [1])
        self.assertEqual(functional2.no_neg([-3, -3, 3, 3]), [3, 3])
        self.assertEqual(functional2.no_neg([-1, -1, -1]), [])
        self.assertEqual(functional2.no_neg([]), [])
        self.assertEqual(functional2.no_neg([0, 1, 2]), [0, 1, 2])
        self.assertEqual(functional2.no_neg([3, -10, 1, -1, 4, -400]), [3, 1, 4])
        self.assertEqual(functional2.no_neg([-1, 3, 1, -1, -10, -100, -111, 5]), [3, 1, 5])
    
    def test_no_9(self):
        self.assertEqual(functional2.no_9([1, 2, 19]), [1, 2])
        self.assertEqual(functional2.no_9([9, 19, 29, 3]), [3])
        self.assertEqual(functional2.no_9([1, 2, 3]), [1, 2, 3])
        self.assertEqual(functional2.no_9([45, 99, 90, 28, 13, 999, 0]), [45, 90, 28, 13, 0])
        self.assertEqual(functional2.no_9([]), [])
        self.assertEqual(functional2.no_9([9]), [])
        self.assertEqual(functional2.no_9([0, 9, 0]), [0, 0])
    
    def test_no_teen(self):
        self.assertEqual(functional2.no_teen([12, 13, 19, 20]), [12, 20])
        self.assertEqual(functional2.no_teen([1, 14, 1]), [1, 1])
        self.assertEqual(functional2.no_teen([15]), [])
        self.assertEqual(functional2.no_teen([-15]),  [-15])
        self.assertEqual(functional2.no_teen([]), [])
        self.assertEqual(functional2.no_teen([0, 1, 2, -3]), [0, 1, 2, -3])
        self.assertEqual(functional2.no_teen([15, 17, 19, 21, 19]), [21])
        self.assertEqual(functional2.no_teen([-16, 2, 15, 3, 16, 25]), [-16, 2, 3, 25])
    
    def test_no_z(self):
        self.assertEqual(functional2.no_z(["aaa", "bbb", "aza"]), ["aaa", "bbb"])
        self.assertEqual(functional2.no_z(["hziz", "hzello", "hi"]), ["hi"])
        self.assertEqual(functional2.no_z(["hello", "howz", "are", "youz"]), ["hello", "are"])
        self.assertEqual(functional2.no_z([]), [])
        self.assertEqual(functional2.no_z([""]), [""])
        self.assertEqual(functional2.no_z(["x", "y", "z"]), ["x", "y"])
    
    def test_no_long(self):
        self.assertEqual(functional2.no_long(["this", "not", "too", "long"]), ["not", "too"])
        self.assertEqual(functional2.no_long(["a", "bbb", "cccc"]), ["a", "bbb"])
        self.assertEqual(functional2.no_long(["cccc", "cccc", "cccc"]), [])
        self.assertEqual(functional2.no_long([]), [])
        self.assertEqual(functional2.no_long([""]), [""])
        self.assertEqual(functional2.no_long(["empty", "", "empty"]), [""])
        self.assertEqual(functional2.no_long(["a"]), ["a"])
        self.assertEqual(functional2.no_long(["aaaa", "bbb", "***", "333"]), ["bbb", "***", "333"])
    
    def test_no_34(self):
        self.assertEqual(functional2.no_34(["a", "bb", "ccc"]), ["a", "bb"])
        self.assertEqual(functional2.no_34(["a", "bb", "ccc", "dddd"]), ["a", "bb"])
        self.assertEqual(functional2.no_34(["ccc", "dddd", "apple"]), ["apple"])
        self.assertEqual(functional2.no_34(["this", "not", "too", "long"]), [])
        self.assertEqual(functional2.no_34(["a", "bbb", "cccc", "xx"]), ["a", "xx"])
        self.assertEqual(functional2.no_34(["dddd", "ddd", "xxxxxxx"]), ["xxxxxxx"])
        self.assertEqual(functional2.no_34([]), [])
        self.assertEqual(functional2.no_34([""]), [""])
        self.assertEqual(functional2.no_34(["empty", "", "empty"]), ["empty", "", "empty"])
        self.assertEqual(functional2.no_34(["a"]), ["a"])
        self.assertEqual(functional2.no_34(["aaaa", "bbb", "*****", "333"]), ["*****"])
    
    def test_no_yy(self):
        self.assertEqual(functional2.no_yy(["a", "b", "c"]), ["ay", "by", "cy"])
        self.assertEqual(functional2.no_yy(["a", "b", "cy"]), ["ay", "by"])
        self.assertEqual(functional2.no_yy(["xx", "ya", "zz"]), ["xxy", "yay", "zzy"])
        self.assertEqual(functional2.no_yy(["xx", "yay", "zz"]), ["xxy", "zzy"])
        self.assertEqual(functional2.no_yy(["yyx", "y", "zzz"]), ["zzzy"])
        self.assertEqual(functional2.no_yy(["hello", "there"]), ["helloy", "therey"])
        self.assertEqual(functional2.no_yy(["ya"]), ["yay"])
        self.assertEqual(functional2.no_yy([]), [])
        self.assertEqual(functional2.no_yy([""]), ["y"])
        self.assertEqual(functional2.no_yy(["xx", "yy", "zz"]), ["xxy", "zzy"])
    
    def test_two_2(self):
        self.assertEqual(functional2.two_2([1, 2, 3]), [4, 6])
        self.assertEqual(functional2.two_2([2, 6, 11]), [4])
        self.assertEqual(functional2.two_2([0]), [0])
        self.assertEqual(functional2.two_2([]), [])
        self.assertEqual(functional2.two_2([1, 11, 111, 16]), [])
        self.assertEqual(functional2.two_2([2, 3, 5, 7, 11]), [4, 6, 10, 14])
        self.assertEqual(functional2.two_2([3, 1, 4, 1, 6, 99, 0]), [6, 8, 198, 0])
    
    def test_square_56(self):
        self.assertEqual(functional2.square_56([3, 1, 4]), [19, 11])
        self.assertEqual(functional2.square_56([1]), [11])
        self.assertEqual(functional2.square_56([2]), [14])
        self.assertEqual(functional2.square_56([3]), [19])
        self.assertEqual(functional2.square_56([4]), [])
        self.assertEqual(functional2.square_56([5]), [])
        self.assertEqual(functional2.square_56([6]), [])
        self.assertEqual(functional2.square_56([7]), [59])
        self.assertEqual(functional2.square_56([1, 2, 3, 4, 5, 6, 7]), [11, 14, 19, 59])
        self.assertEqual(functional2.square_56([3, -1, -4, 1, 5, 9]), [19, 11, 11, 91])

if __name__ == '__main__':
    unittest.main()