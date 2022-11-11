import sys
sys.path.append('')

import unittest
import solutions.string1 as string1

class TestString1(unittest.TestCase):
    def test_hello_names(self):
        self.assertEqual(string1.hello_name('Bob'), 'Hello Bob!')
        self.assertEqual(string1.hello_name('Alice'), 'Hello Alice!')
        self.assertEqual(string1.hello_name('X'), 'Hello X!')
        self.assertEqual(string1.hello_name('Dolly'), 'Hello Dolly!')
        self.assertEqual(string1.hello_name('Alpha'), 'Hello Alpha!')
        self.assertEqual(string1.hello_name('Omega'), 'Hello Omega!')
        self.assertEqual(string1.hello_name('Goodbye'), 'Hello Goodbye!')
        self.assertEqual(string1.hello_name('ho ho ho'), 'Hello ho ho ho')
        self.assertEqual(string1.hello_name('xyz!'), 'Hello xyz!!')
        self.assertEqual(string1.hello_name('Hello'), 'Hello Hello!')

    def test_make_abba(self):
        self.assertEqual(string1.make_abba('Hi', 'Bye'), 'HiByeByeHi')
        self.assertEqual(string1.make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
        self.assertEqual(string1.make_abba('What', 'Up'), 'WhatUpUpWhat')
        self.assertEqual(string1.make_abba('aaa', 'bbb'), 'aaabbbbbbaaa')
        self.assertEqual(string1.make_abba('x', 'y'), 'xyyx')
        self.assertEqual(string1.make_abba('x', ''), 'xx')
        self.assertEqual(string1.make_abba('', 'y'), 'yy')
        self.assertEqual(string1.make_abba('Bo', 'Ya'), 'BoYaYaBo')
        self.assertEqual(string1.make_abba('Ya', 'Ya'), 'YaYaYaYa')

    def test_make_tags(self):
        self.assertEqual(string1.make_tags('i', 'Yay'), '<i>Yay</i>')
        self.assertEqual(string1.make_tags('i', 'Hello'), '<i>Hello</i>')
        self.assertEqual(string1.make_tags('cite', 'Yay'), '<cite>Yay</cite>')
        self.assertEqual(string1.make_tags('address', 'here'), '<address>here</address')
        self.assertEqual(string1.make_tags('body', 'Heart'), '<body>Heart</body>')
        self.assertEqual(string1.make_tags('i', 'i'), '<i>i</i>')
        self.assertEqual(string1.make_tags('i', ''), '<i></i>')

if __name__ == '__main__':
    unittest.main()