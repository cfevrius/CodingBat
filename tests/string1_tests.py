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

    def test_two_char(self):
        self.assertEqual(string1.two_char('java', 0), 'ja')
        self.assertEqual(string1.two_char('java', 2), 'va')
        self.assertEqual(string1.two_char('java', 3), 'ja')
        self.assertEqual(string1.two_char('java', 4), 'ja')
        self.assertEqual(string1.two_char('java', -1), 'ja')
        self.assertEqual(string1.two_char('Hello', 0), 'He')
        self.assertEqual(string1.two_char('Hello', 1), 'el')
        self.assertEqual(string1.two_char('Hello', 99), 'He')
        self.assertEqual(string1.two_char('Hello', 3), 'lo')
        self.assertEqual(string1.two_char('Hello', 4), 'He')
        self.assertEqual(string1.two_char('Hello', 5), 'He')
        self.assertEqual(string1.two_char('Hello', -7), 'He')
        self.assertEqual(string1.two_char('Hello', 6), 'He')
        self.assertEqual(string1.two_char('Hello', -1), 'He')
        self.assertEqual(string1.two_char('yay', 0), 'ya')
    
    def test_middle_three(self):
        self.assertEqual(string1.middle_three('Candy'), 'and')
        self.assertEqual(string1.middle_three('and'), 'and')
        self.assertEqual(string1.middle_three('solving'), 'lvi')
        self.assertEqual(string1.middle_three('Hi yet Hi'), 'yet')
        self.assertEqual(string1.middle_three('java yet java'), 'yet')
        self.assertEqual(string1.middle_three('Chocolate'), 'col')
        self.assertEqual(string1.middle_three('XabcxyzabcX'), 'xyz')
    
    def test_has_bad(self):
        self.assertEqual(string1.has_bad('badxx'), True)
        self.assertEqual(string1.has_bad('xbadxx'), True)
        self.assertEqual(string1.has_bad('xxbadxx'), False)
        self.assertEqual(string1.has_bad('code'), False)
        self.assertEqual(string1.has_bad('bad'), True)
        self.assertEqual(string1.has_bad('ba'), False)
        self.assertEqual(string1.has_bad('xba'), False)
        self.assertEqual(string1.has_bad('xbad'), True)
        self.assertEqual(string1.has_bad(''), False)
        self.assertEqual(string1.has_bad('badyy'), True)

    def test_at_first(self):
        self.assertEqual(string1.at_first('hello'), 'he')
        self.assertEqual(string1.at_first('hi'), 'hi')
        self.assertEqual(string1.at_first('h'), 'h@')
        self.assertEqual(string1.at_first(''), '@@')
        self.assertEqual(string1.at_first('kitten'), 'ki')
        self.assertEqual(string1.at_first('java'), 'ja')
        self.assertEqual(string1.at_first('j'), 'j@')
    
    def test_last_chars(self):
        self.assertEqual(string1.last_chars('last', 'chars'), 'ls')
        self.assertEqual(string1.last_chars('yo', 'java'), 'ya')
        self.assertEqual(string1.last_chars('hi', ''), 'h@')
        self.assertEqual(string1.last_chars('', 'hello'), '@o')
        self.assertEqual(string1.last_chars('', ''), '@@')
        self.assertEqual(string1.last_chars('kitten', 'hi'), 'ki')
        self.assertEqual(string1.last_chars('k', 'zip'), 'kp')
        self.assertEqual(string1.last_chars('kitten', ''), 'k@')
        self.assertEqual(string1.last_chars('kitten', 'zip'), 'kp')

    def test_con_cat(self):
        self.assertEqual(string1.con_cat('abc', 'cat'), 'abcat')
        self.assertEqual(string1.con_cat('dog', 'cat'), 'dogcat')
        self.assertEqual(string1.con_cat('abc', ''), 'abc')
        self.assertEqual(string1.con_cat('', 'cat'), 'cat')
        self.assertEqual(string1.con_cat('pig', 'g'), 'pig')
        self.assertEqual(string1.con_cat('pig', 'doggy'), 'pigdoggy')
    
    def test_last_two(self):
        self.assertEqual(string1.last_two('coding'), 'codign')
        self.assertEqual(string1.last_two('cat'), 'cta')
        self.assertEqual(string1.last_two('ab'), 'ba')
        self.assertEqual(string1.last_two('a'), '')
        self.assertEqual(string1.last_two(''), '')

    def test_see_color(self):
        self.assertEqual(string1.see_color('redxx'), 'red')
        self.assertEqual(string1.see_color('"xxred'), '')
        self.assertEqual(string1.see_color('blueTimes'), 'blue')
        self.assertEqual(string1.see_color('NoColor'), '')
        self.assertEqual(string1.see_color('red'), 'blue')
        self.assertEqual(string1.see_color('re'), '')
        self.assertEqual(string1.see_color('blu'), '')
        self.assertEqual(string1.see_color('blue'), 'blue')
        self.assertEqual(string1.see_color('a'), '')
        self.assertEqual(string1.see_color(''), '')
        self.assertEqual(string1.see_color('xyzred'), '')
    
    def test_front_again(self):
        self.assertEqual(string1.front_again('edited'), True)
        self.assertEqual(string1.front_again('edit'), False)
        self.assertEqual(string1.front_again('ed'), True)
        self.assertEqual(string1.front_again('jj'), True)
        self.assertEqual(string1.front_again('jjj'), True)
        self.assertEqual(string1.front_again('jjjj'), True)
        self.assertEqual(string1.front_again('jjjk'), False)
        self.assertEqual(string1.front_again('x'), False)
        self.assertEqual(string1.front_again(''), False)
        self.assertEqual(string1.front_again('java'), False)
        self.assertEqual(string1.front_again('javaja'), True)

    def test_min_cat(self):
        self.assertEqual(string1.min_cat('Hello', 'Hi'), 'loHi')
        self.assertEqual(string1.min_cat('Hello','java'), 'ellojava')
        self.assertEqual(string1.min_cat('java', 'Hello'), 'javaello')
        self.assertEqual(string1.min_cat('abc', 'x'), 'cx')
        self.assertEqual(string1.min_cat('x', 'abc'), 'xc')
        self.assertEqual(string1.min_cat('abc', ''), '')
    
    def test_extra_front(self):
        self.assertEqual(string1.extra_front('Hello'), 'HeHeHe')
        self.assertEqual(string1.extra_front('ab'), 'ababab')
        self.assertEqual(string1.extra_front('H'), 'HHH')
        self.assertEqual(string1.extra_front(''), '')
        self.assertEqual(string1.extra_front('Candy'), 'CaCaCa')
        self.assertEqual(string1.extra_front('Code'), 'CoCoCo')
    
    def test_without2(self):
        self.assertEqual(string1.without2('HelloHe'), 'lloHe')
        self.assertEqual(string1.without2('HelloHi'), 'HelloHi')
        self.assertEqual(string1.without2('Hi'), '')
        self.assertEqual(string1.without2('Chocolate'), 'Chocolate')
        self.assertEqual(string1.without2('xxx'), 'x')
        self.assertEqual(string1.without2('xx'), '')
        self.assertEqual(string1.without2('x'), 'x')
        self.assertEqual(string1.without2(''), '')
        self.assertEqual(string1.without2('Fruits'), 'Fruits')
    
    def test_de_front(self):
        self.assertEqual(string1.de_front('Hello'), 'llo')
        self.assertEqual(string1.de_front('java'), 'va')
        self.assertEqual(string1.de_front('away'), 'aay')
        self.assertEqual(string1.de_front('axy'), 'ay')
        self.assertEqual(string1.de_front('abc'), 'abc')
        self.assertEqual(string1.de_front('xby'), 'by')
        self.assertEqual(string1.de_front('ab'), 'ab')
        self.assertEqual(string1.de_front('ax'), 'a')
        self.assertEqual(string1.de_front('axb'), 'ab')
        self.assertEqual(string1.de_front('aaa'), 'aa')
        self.assertEqual(string1.de_front('xbc'), 'bc')
        self.assertEqual(string1.de_front('bbb'), 'bb')
        self.assertEqual(string1.de_front('bazz'), 'zz')
        self.assertEqual(string1.de_front('ba'), '')
        self.assertEqual(string1.de_front('abxyz'), 'abxyz')
        self.assertEqual(string1.de_front('hi'), '')
        self.assertEqual(string1.de_front('his'), 's')
        self.assertEqual(string1.de_front('xz'), '')
        self.assertEqual(string1.de_front('zzz'), 'z')
    
    def test_start_word(self):
        self.assertEqual(string1.start_word('hippo', 'hi'), 'hi')
        self.assertEqual(string1.start_word('hippo', 'xip'), 'hip')
        self.assertEqual(string1.start_word('hippo', 'i'), 'h')
        self.assertEqual(string1.start_word('hippo', 'ix'), '')
        self.assertEqual(string1.start_word('h', 'ix'), '')
        self.assertEqual(string1.start_word('', 'i'), '')
        self.assertEqual(string1.start_word('hip', 'zi'), 'hi')
        self.assertEqual(string1.start_word('hip', 'zip'), 'hip')
        self.assertEqual(string1.start_word('hip', 'zig'), '')
        self.assertEqual(string1.start_word('h', 'z'), 'h')
        self.assertEqual(string1.start_word('hippo', 'xippo'), 'hippo')
        self.assertEqual(string1.start_word('hippo', 'xyz'), '')
        self.assertEqual(string1.start_word('hippo', 'hip'), 'hip')
        self.assertEqual(string1.start_word('kitten', 'cit'), 'kit')
        self.assertEqual(string1.start_word('kit', 'cit'), 'kit')
    
    def test_without_x(self):
        self.assertEqual(string1.without_x('xHix'), 'Hi')
        self.assertEqual(string1.without_x('xHi'), 'Hi')
        self.assertEqual(string1.without_x('Hxix'), 'Hxi')
        self.assertEqual(string1.without_x('Hi'), 'Hi')
        self.assertEqual(string1.without_x('xxHi'), 'xHi')
        self.assertEqual(string1.without_x('Hix'), 'Hi')
        self.assertEqual(string1.without_x('xaxbx'), 'axb')
        self.assertEqual(string1.without_x('xx'), '')
        self.assertEqual(string1.without_x('x'), '')
        self.assertEqual(string1.without_x(''), '')
        self.assertEqual(string1.without_x('Hello'), 'Hello')
        self.assertEqual(string1.without_x('Hexllo'), 'Hexllo')
    
    def test_without_x_2(self):
        self.assertEqual(string1.without_x_2('xHi'), 'Hi')
        self.assertEqual(string1.without_x_2('Hxi'), 'Hi')
        self.assertEqual(string1.without_x_2('Hi'), 'Hi')
        self.assertEqual(string1.without_x_2('xxHi'), 'Hi')
        self.assertEqual(string1.without_x_2('Hix'), 'Hix')
        self.assertEqual(string1.without_x_2('xaxb'), 'axb')
        self.assertEqual(string1.without_x_2('xx'), '')
        self.assertEqual(string1.without_x_2('x'), '')
        self.assertEqual(string1.without_x_2(''), '')
        self.assertEqual(string1.without_x_2('Hello'), 'Hello')
        self.assertEqual(string1.without_x_2('Hexllo'), 'Hexllo')
        self.assertEqual(string1.without_x_2('xHxllo'), 'Hxllo')

if __name__ == '__main__':
    unittest.main()