import unittest
import solutions.functional1 as funtional1

class TestFunctional1(unittest.TestCase):
    def test_doubling(self):
        self.assertEqual(funtional1.doubling([1, 2, 3]), [2, 4, 6])
        self.assertEqual(funtional1.doubling([6, 8, 6, 8, -1]), [12, 16, 12, 16, -2])
        self.assertEqual(funtional1.doubling([]), [])
        self.assertEqual(funtional1.doubling([5]), [10])
        self.assertEqual(funtional1.doubling([5, 10]), [10, 20])
        self.assertEqual(funtional1.doubling([8, -5, 7, 3, 109]), [16, -10, 14, 6, 218])
        self.assertEqual(funtional1.doubling([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]),  [12, -6, 24, 46, 8, 2, 38, 22, 4, 6, 4])
        self.assertEqual(funtional1.doubling([3, 1, 4, 1, 5, 9]), [6, 2, 8, 2, 10, 18])
    
    def test_square(self):
        self.assertEqual(funtional1.square([1, 2, 3]), [1, 4, 9])
        self.assertEqual(funtional1.square([6, 8, -6, -8, 1]), [36, 64, 36, 64, 1])
        self.assertEqual(funtional1.square([]), [])
        self.assertEqual(funtional1.square([12]), [144])
        self.assertEqual(funtional1.square([5, 10]), [25, 100])
        self.assertEqual(funtional1.square([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]), [36, 9, 144, 529, 16, 1, 361, 121, 4, 9, 4])
    
    def test_add_star(self):
        self.assertEqual(funtional1.add_star(['a', 'bb', 'ccc']), ['a*', 'bb*', 'ccc*'])
        self.assertEqual(funtional1.add_star(['hello', 'there']), ['hello*', 'there*'])
        self.assertEqual(funtional1.add_star(['*']), ['**'])
        self.assertEqual(funtional1.add_star([]), [])
        self.assertEqual(funtional1.add_star(['kittens', 'and', 'chocolate', 'and']), ['kittens*', 'and*', 'chocolate*', 'and*'])
        self.assertEqual(funtional1.add_star(['empty', 'string', '']), ['empty*', 'string*', '*'])
    
    def test_copies3(self):
        self.assertEqual(funtional1.copies3(['a', 'bb', 'ccc']), ['aaa', 'bbbbbb', 'ccccccccc'])
        self.assertEqual(funtional1.copies3(['24', 'a', '']), ['242424', 'aaa', ''])
        self.assertEqual(funtional1.copies3(['hello', 'there']), ['hellohellohello', 'theretherethere'])
        self.assertEqual(funtional1.copies3(['no']), ['nonono'])
        self.assertEqual(funtional1.copies3([]), [])
        self.assertEqual(funtional1.copies3(['this', 'and', 'that', 'and']), ['thisthisthis', 'andandand', 'thatthatthat', 'andandand'])
    
    def test_more_y(self):
        self.assertEqual(funtional1.more_y(['a', 'b', 'c']), ['yay', 'yby', 'ycy'])
        self.assertEqual(funtional1.more_y(['hello', 'there']), ['yhelloy', 'ytherey'])
        self.assertEqual(funtional1.more_y(['yay']), ['yyayy'])
        self.assertEqual(funtional1.more_y(['', 'a', 'xx']), ['yy', 'yay', 'yxxy'])
        self.assertEqual(funtional1.more_y([]), [])
        self.assertEqual(funtional1.more_y(['xx', 'yy', 'zz']), ['yxxy', 'yyyy', 'yzzy'])
    
    def test_math1(self):
        self.assertEqual(funtional1.math1([1, 2, 3]), [20, 30, 40])
        self.assertEqual(funtional1.math1([6, 8, 6, 8, 1]), [70, 90, 70, 90, 20])
        self.assertEqual(funtional1.math1([10]), [110])
        self.assertEqual(funtional1.math1([]), [])
        self.assertEqual(funtional1.math1([5, 10]), [60, 110])
        self.assertEqual(funtional1.math1([-1, -2, -3, -2, -1]), [0, -10, -20, -10, 0])
        self.assertEqual(funtional1.math1([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]), [70, -20, 130, 240, 50, 20, 200, 120, 30, 40, 30])
    
    def test_right_digit(self):
        self.assertEqual(funtional1.right_digit([1, 22, 93]), [1, 2, 3]	)
        self.assertEqual(funtional1.right_digit([16, 8, 886, 8, 1]), [6, 8, 6, 8, 1])
        self.assertEqual(funtional1.right_digit([10, 0]), [0, 0])
        self.assertEqual(funtional1.right_digit([]), [])
        self.assertEqual(funtional1.right_digit([5, 10]), [5, 0])
        self.assertEqual(funtional1.right_digit([5, 50, 500, 5000, 5000]), [5, 0, 0, 0, 0])
        self.assertEqual(funtional1.right_digit([6, 23, 12, 23, 4, 1, 19, 1119, 2, 3, 2]), [6, 3, 2, 3, 4, 1, 9, 9, 2, 3, 2])
    
    def test_lower(self):
        self.assertEqual(funtional1.lower(['Hello', 'Hi']), ['hello', 'hi'])
        self.assertEqual(funtional1.lower(['AAA', 'BBB', 'ccc']), ['aaa', 'bbb', 'ccc'])
        self.assertEqual(funtional1.lower(['KitteN', 'ChocolaTE']), ['kitten', 'chocolate'])
        self.assertEqual(funtional1.lower([]), [])
        self.assertEqual(funtional1.lower(['EMPTY', '']), ['empty', ''])
        self.assertEqual(funtional1.lower(['aaX', 'bYb', 'Ycc', 'ZZZ']), ['aax', 'byb', 'ycc', 'zzz'])
    
    def test_no_x(self):
        self.assertEqual(funtional1.no_x(['ax', 'bb', 'cx']), ['a', 'bb', 'c'])
        self.assertEqual(funtional1.no_x(['xxax', 'xbxbx', 'xxcx']), ['a', 'bb', 'c'])
        self.assertEqual(funtional1.no_x(['x']), [''])
        self.assertEqual(funtional1.no_x(['']), [''])
        self.assertEqual(funtional1.no_x([]), [])
        self.assertEqual(funtional1.no_x(['the', 'taxi']), ['the', 'tai'])
        self.assertEqual(funtional1.no_x(['the', 'xxtxaxixxx']), ['the', 'tai'])
        self.assertEqual(funtional1.no_x(['this', 'is', 'the', 'x']), ['this', 'is', 'the', ''])

if __name__ == '__main__':
    unittest.main()