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
        self.assertEqual(string1.hello_name('ho ho ho'), 'Hello ho ho ho!')
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
        self.assertEqual(string1.make_tags('address', 'here'), '<address>here</address>')
        self.assertEqual(string1.make_tags('body', 'Heart'), '<body>Heart</body>')
        self.assertEqual(string1.make_tags('i', 'i'), '<i>i</i>')
        self.assertEqual(string1.make_tags('i', ''), '<i></i>')

    def test_make_out_word(self):
        self.assertEqual(string1.make_out_word('<<>>>', 'Yay'), '<<Yay>>')
        self.assertEqual(string1.make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
        self.assertEqual(string1.make_out_word('[[]]', 'word'), '[[word]]')
        self.assertEqual(string1.make_out_word('HHoo', 'Hello'), 'HHHellooo')
        self.assertEqual(string1.make_out_word('abyz', 'YAY'), 'abYAYyz')
    
    def test_extra_end(self):
        self.assertEqual(string1.extra_end('Hello'), 'lololo')
        self.assertEqual(string1.extra_end('ab'), 'ababab')
        self.assertEqual(string1.extra_end('Hi'), 'HiHiHi')
        self.assertEqual(string1.extra_end('Candy'), 'dydydy')
        self.assertEqual(string1.extra_end('Code'), 'dedede')

    def test_first_two(self):
        self.assertEqual(string1.first_two('Hello'), 'He') 
        self.assertEqual(string1.first_two('abcdefg'), 'ab') 
        self.assertEqual(string1.first_two('ab'), 'ab') 
        self.assertEqual(string1.first_two('a'), 'a') 
        self.assertEqual(string1.first_two(''), '') 
        self.assertEqual(string1.first_two('Kitten'), 'Ki') 
        self.assertEqual(string1.first_two('hi'), 'hi') 
        self.assertEqual(string1.first_two('hiya'), 'hi') 
    
    def test_first_half(self):
        self.assertEqual(string1.first_half('WooHoo'), 'Woo')
        self.assertEqual(string1.first_half('HelloThere'), 'Hello')
        self.assertEqual(string1.first_half('abcdef'), 'abc')
        self.assertEqual(string1.first_half('ab'), 'a')
        self.assertEqual(string1.first_half(''), '')
        self.assertEqual(string1.first_half('0123456789'), '01234')
        self.assertEqual(string1.first_half('kitten'), 'kit')
    
    def test_without_end(self):
        self.assertEqual(string1.without_end('Hello'), 'ell')
        self.assertEqual(string1.without_end('java'), 'av')
        self.assertEqual(string1.without_end('coding'), 'odin')
        self.assertEqual(string1.without_end('code'), 'od')
        self.assertEqual(string1.without_end('ab'), '')
        self.assertEqual(string1.without_end('Chocolate!'), 'hocolate')
        self.assertEqual(string1.without_end('kitten'), 'itte')
        self.assertEqual(string1.without_end('woohoo'), 'ooho')
    
    def test_combo_string(self):
        self.assertEqual(string1.combo_string('Hello','hi'), 'hiHellohi')
        self.assertEqual(string1.combo_string('hi','Hello'), 'hiHellohi')
        self.assertEqual(string1.combo_string('aaa','b'), 'baaab')
        self.assertEqual(string1.combo_string('b','aaa'), 'baaab')
        self.assertEqual(string1.combo_string('aaa',''), 'aaa')
        self.assertEqual(string1.combo_string('','bb'), 'bb')
        self.assertEqual(string1.combo_string('aaa','1234'), 'aaa1234aaa')
        self.assertEqual(string1.combo_string('aaa','bb'), 'bbaaabb')
        self.assertEqual(string1.combo_string('a','bb'), 'abba')
        self.assertEqual(string1.combo_string('bb','a'), 'abba')
        self.assertEqual(string1.combo_string('xyz','ab'), 'abxyzab')
    
    def test_non_start(self):
        self.assertEqual(string1.non_start('Hello', 'There'), 'ellohere')
        self.assertEqual(string1.non_start('java', 'code'), 'avaode')
        self.assertEqual(string1.non_start('shotl', 'java'), 'hotlava')
        self.assertEqual(string1.non_start('ab', 'xy'), 'by')
        self.assertEqual(string1.non_start('ab', 'x'), 'b')
        self.assertEqual(string1.non_start('x', 'ac'), 'c')
        self.assertEqual(string1.non_start('a', 'x'), '')
        self.assertEqual(string1.non_start('kit', 'kat'), 'itat')
        self.assertEqual(string1.non_start('mart', 'dart'), 'artart')
    
    def test_left_2(self):
        self.assertEqual(string1.left_2('Hello'), 'lloHe')
        self.assertEqual(string1.left_2('java'), 'vaja')
        self.assertEqual(string1.left_2('Hi'), 'Hi')
        self.assertEqual(string1.left_2('code'), 'deco')
        self.assertEqual(string1.left_2('cat'), 'tca')
        self.assertEqual(string1.left_2('12345'), '34512')
        self.assertEqual(string1.left_2('Chocolate'), 'ocolateCh')
        self.assertEqual(string1.left_2('bricks'), 'icksbr')
    
    def test_right_2(self):
        self.assertEqual(string1.right_2('Hello'), 'loHel')
        self.assertEqual(string1.right_2('java'), 'vaja')
        self.assertEqual(string1.right_2('Hi'), 'Hi')
        self.assertEqual(string1.right_2('code'), 'deco')
        self.assertEqual(string1.right_2('cat'), 'atc')
        self.assertEqual(string1.right_2('12345'), '45123')
    
    def test_the_end(self):
        self.assertEqual(string1.the_end('Hello', True), 'H')
        self.assertEqual(string1.the_end('Hello', False), 'o')
        self.assertEqual(string1.the_end('oh', True), 'o')
        self.assertEqual(string1.the_end('oh', False), 'h')
        self.assertEqual(string1.the_end('x', True), 'x')
        self.assertEqual(string1.the_end('x', False), 'x')
        self.assertEqual(string1.the_end('java', True), 'j')
        self.assertEqual(string1.the_end('chocolate', False), 'e')
        self.assertEqual(string1.the_end('1234', True), '1')
        self.assertEqual(string1.the_end('code', False), 'e')
    
    def test_without_end_2(self):
        self.assertEqual(string1.without_end_2('Hello'), 'ell')
        self.assertEqual(string1.without_end_2('abc'), 'b')
        self.assertEqual(string1.without_end_2('ab'), '')
        self.assertEqual(string1.without_end_2('a'), '')
        self.assertEqual(string1.without_end_2(''), '')
        self.assertEqual(string1.without_end_2('coldy'), 'old')
        self.assertEqual(string1.without_end_2('java code'), 'ava cod')
    
    def test_middle_two(self):
        self.assertEqual(string1.middle_two('string'), 'ri')
        self.assertEqual(string1.middle_two('code'), 'od')
        self.assertEqual(string1.middle_two('Practice'), 'ct')
        self.assertEqual(string1.middle_two('ab'), 'ab')
        self.assertEqual(string1.middle_two('0123456789'), '45')
    
    def test_ends_ly(self):
        self.assertEqual(string1.ends_ly('oddly'), True)
        self.assertEqual(string1.ends_ly('y'), False)
        self.assertEqual(string1.ends_ly('oddy'), False)
        self.assertEqual(string1.ends_ly('oddl'), False)
        self.assertEqual(string1.ends_ly('olydd'), False)
        self.assertEqual(string1.ends_ly('ly'), True)
        self.assertEqual(string1.ends_ly(''), False)
        self.assertEqual(string1.ends_ly('falsey'), False)
        self.assertEqual(string1.ends_ly('evenly'), True)
    
    def test_n_twice(self):
        self.assertEqual(string1.n_twice('Hello', 2), 'Helo')
        self.assertEqual(string1.n_twice('Chocolate', 3), 'Choate')
        self.assertEqual(string1.n_twice('Chocolate', 1), 'Ce')
        self.assertEqual(string1.n_twice('Chocolate', 0), '')
        self.assertEqual(string1.n_twice('Hello', 4), 'Hellello')
        self.assertEqual(string1.n_twice('Code', 4), 'CodeCode')
        self.assertEqual(string1.n_twice('Code', 2), 'Code')

if __name__ == '__main__':
    unittest.main()