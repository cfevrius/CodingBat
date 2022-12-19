import unittest
import source.map2 as map2

class TestMap2(unittest.TestCase):
    def test_word0(self):
        self.assertEqual(map2.word0(['a', 'b', 'a', 'b']), {'a': 0, 'b': 0})
        self.assertEqual(map2.word0(['a', 'b', 'a', 'c', 'b']), {'a': 0, 'b': 0, 'c': 0})
        self.assertEqual(map2.word0(['c', 'b', 'a']), {'a': 0, 'b': 0, 'c': 0})
        self.assertEqual(map2.word0(['c', 'c', 'c', 'c']), {'c': 0})
        self.assertEqual(map2.word0([]), {})
    
    def test_world_len(self):
        self.assertEqual(map2.word_len(['a', 'bb', 'a', 'bb']), {'bb': 2, 'a': 1})
        self.assertEqual(map2.word_len(['this', 'and', 'that', 'and']), {'that': 4, 'and': 3, 'this': 4})
        self.assertEqual(map2.word_len(['code', 'code', 'code', 'bug']), {'code': 4, 'bug': 3})
        self.assertEqual(map2.word_len([]), {})
        self.assertEqual(map2.word_len(['z']), {'z': 1})
    
    def test_pairs(self):
        self.assertEqual(map2.pairs(['code', 'bug']), {'b': 'g', 'c': 'e'})
        self.assertEqual(map2.pairs(['man', 'moon', 'main']), {'m': 'n'})
        self.assertEqual(map2.pairs(['man', 'moon', 'good', 'night']), {'g': 'd', 'm': 'n', 'n': 't'})
        self.assertEqual(map2.pairs([]), {})
        self.assertEqual(map2.pairs(['a', 'b']), {'a': 'a', 'b': 'b'})
        self.assertEqual(map2.pairs(['are', 'codes', 'and', 'cods']), {'a': 'd', 'c': 's'})
        self.assertEqual(map2.pairs(['apple', 'banana', 'tea', 'coffee']), {'a': 'e', 'b': 'a', 'c': 'e', 't': 'a'})
    
    def test_word_count(self):
        self.assertEqual(map2.word_count(['a', 'b', 'a', 'c', 'b']), {'a': 2, 'b': 2, 'c': 1})
        self.assertEqual(map2.word_count(['c', 'b', 'a']), {'a': 1, 'b': 1, 'c': 1})
        self.assertEqual(map2.word_count(['c', 'c', 'c', 'c']), {'c': 4})
        self.assertEqual(map2.word_count([]), {})
        self.assertEqual(map2.word_count(['this', 'and', 'this', '']), {'': 1, 'and': 1, 'this': 2})
        self.assertEqual(map2.word_count(['x', 'y', 'x', 'Y', 'X']), {'x': 2, 'X': 1, 'y': 1, 'Y': 1})
        self.assertEqual(map2.word_count(['123', '0', '123', '1']), {'0': 1, '1': 1, '123': 2})
        self.assertEqual(map2.word_count(['d', 'a', 'e', 'd', 'a', 'd', 'b', 'b', 'z', 'a', 'a', 'b', 'z', 'x', 'b', 'f', 'x', 'two', 'b', 'one', 'two']), {'a': 4, 'b': 5, 'd': 3, 'e': 1, 'f': 1, 'one': 1, 'x': 2, 'z': 2, 'two': 2})
        self.assertEqual(map2.word_count(['apple', 'banana', 'apple', 'apple', 'tea', 'coffee', 'banana']), {'banana': 2, 'apple': 3, 'tea': 1, 'coffee': 1})
    
    def test_first_char(self):
        self.assertEqual(map2.first_char(['salt', 'tea', 'soda', 'toast']), {'s': 'saltsoda', 't': 'teatoast'})
        self.assertEqual(map2.first_char(['aa', 'bb', 'cc', 'aAA', 'cCC', 'd']), {'a': 'aaaAA', 'b': 'bb', 'c': 'cccCC', 'd': 'd'})
        self.assertEqual(map2.first_char([]), {})
        self.assertEqual(map2.first_char(['apple', 'bells', 'salt', 'aardvark', 'bells', 'sun', 'zen', 'bells']), {'a': 'appleaardvark', 'b': 'bellsbellsbells', 's': 'saltsun', 'z': 'zen'})
    
    def test_word_appends(self):
        self.assertEqual(map2.word_appends(['a', 'b', 'a']), 'a')
        self.assertEqual(map2.word_appends(['a', 'b', 'a', 'c', 'a', 'd', 'a']), 'aa')
        self.assertEqual(map2.word_appends(['a', '', 'a']), 'a')
        self.assertEqual(map2.word_appends([]), '')
        self.assertEqual(map2.word_appends(['a', 'b', 'b', 'a', 'a']), 'ba')
        self.assertEqual(map2.word_appends(['a', 'b', 'b', 'b', 'a', 'c', 'a', 'a']), 'baa')
        self.assertEqual(map2.word_appends(['a', 'b', 'b', 'b', 'a', 'c', 'a', 'a', 'a', 'b', 'a']), 'baaba')
        self.assertEqual(map2.word_appends(['not', 'and', 'or', 'and', 'this', 'and', 'or', 'that', 'not']), 'andornot')
        self.assertEqual(map2.word_appends(['a', 'b', 'c']), '')
        self.assertEqual(map2.word_appends(['this', 'or', 'that', 'and', 'this', 'and', 'that']), 'thisandthat')
        self.assertEqual(map2.word_appends(['xx', 'xx', 'yy', 'xx', 'zz', 'yy', 'zz', 'xx']), 'xxyyzzxx')
    
    def test_word_multiple(self):
        self.assertEqual(map2.word_multiple(['a', 'b', 'a', 'c', 'b']), {'a': True, 'b': True, 'c': False})
        self.assertEqual(map2.word_multiple(['c', 'b', 'a']), {'a': False, 'b': False, 'c': False})
        self.assertEqual(map2.word_multiple(['c', 'c', 'c', 'c']), {'c': True})
        self.assertEqual(map2.word_multiple([]), {})
        self.assertEqual(map2.word_multiple(['this', 'and', 'this']), {'and': False, 'this': True})
        self.assertEqual(map2.word_multiple(['d', 'a', 'e', 'd', 'a', 'd', 'b', 'b', 'z', 'a', 'a', 'b', 'z', 'x']), {'a': True, 'b': True, 'd': True, 'e': False, 'x': False, 'z': True})
    
    def test_all_swap(self):
        self.assertEqual(map2.all_swap(['ab', 'ac']), ['ac', 'ab'])
        self.assertEqual(map2.all_swap(['ax', 'bx', 'cx', 'cy', 'by', 'ay', 'aaa', 'azz']), ['ay', 'by', 'cy', 'cx', 'bx', 'ax', 'azz', 'aaa'])
        self.assertEqual(map2.all_swap(['ax', 'bx', 'ay', 'by', 'ai', 'aj', 'bx', 'by']), ['ay', 'by', 'ax', 'bx', 'aj', 'ai', 'by', 'bx'])
        self.assertEqual(map2.all_swap(['ax', 'bx', 'cx', 'ay', 'cy', 'aaa', 'abb']), ['ay', 'bx', 'cy', 'ax', 'cx', 'abb', 'aaa'])
        self.assertEqual(map2.all_swap(['easy', 'does', 'it', 'every', 'ice', 'eaten']), ['every', 'does', 'ice', 'easy', 'it', 'eaten'])
        self.assertEqual(map2.all_swap(['list', 'of', 'words', 'swims', 'over', 'lily', 'water', 'wait']), ['lily', 'over', 'water', 'swims', 'of', 'list', 'words', 'wait'])
        self.assertEqual(map2.all_swap(['4', '8', '15', '16', '23', '42']), ['42', '8', '16', '15', '23', '4'])
        self.assertEqual(map2.all_swap(['aaa']), ['aaa'])
        self.assertEqual(map2.all_swap([]), [])
        self.assertEqual(map2.all_swap(['a', 'b', 'c', 'xx', 'yy', 'zz']), ['a', 'b', 'c', 'xx', 'yy', 'zz'])
    
    def test_first_swap(self):
        self.assertEqual(map2.first_swap(['ab', 'ac']), ['ac', 'ab'])
        self.assertEqual(map2.first_swap(['ax', 'bx', 'cx', 'cy', 'by', 'ay', 'aaa', 'azz']), ['ay', 'by', 'cy', 'cx', 'bx', 'ax', 'aaa', 'azz'])
        self.assertEqual(map2.first_swap(['ax', 'bx', 'ay', 'by', 'ai', 'aj', 'bx', 'by']), ['ay', 'by', 'ax', 'bx', 'ai', 'aj', 'bx', 'by'])
        self.assertEqual(map2.first_swap(['ax', 'bx', 'cx', 'ay', 'cy', 'aaa', 'abb']), ['ay', 'bx', 'cy', 'ax', 'cx', 'aaa', 'abb'])
        self.assertEqual(map2.first_swap(['easy', 'does', 'it', 'every', 'ice', 'eaten']), ['every', 'does', 'ice', 'easy', 'it', 'eaten'])
        self.assertEqual(map2.first_swap(['list', 'of', 'words', 'swims', 'over', 'lily', 'water', 'wait']), ['lily', 'over', 'water', 'swims', 'of', 'list', 'words', 'wait'])
        self.assertEqual(map2.first_swap(['4', '8', '15', '16', '23', '42']),  ['42', '8', '16', '15', '23', '4'])
        self.assertEqual(map2.first_swap(['aaa']), ['aaa'])
        self.assertEqual(map2.first_swap([]), [])
        self.assertEqual(map2.first_swap(['a', 'b', 'c', 'xx', 'yy', 'zz']), ['a', 'b', 'c', 'xx', 'yy', 'zz'])
    
if __name__ == '__main__':
    unittest.main()