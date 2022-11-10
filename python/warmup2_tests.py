import unittest
import warmup2

class TestWarmUp1(unittest.TestCase):
    def test_string_times(self):
        self.assertEqual(warmup2.string_times('Hi', 2), 'HiHi')
        self.assertEqual(warmup2.string_times('Hi', 3), 'HiHiHi')
        self.assertEqual(warmup2.string_times('Hi', 1), 'Hi')
        self.assertEqual(warmup2.string_times('Hi', 0), '')
        self.assertEqual(warmup2.string_times('Hi', 5), 'HiHiHiHiHi')
        self.assertEqual(warmup2.string_times('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
        self.assertEqual(warmup2.string_times('x', 4), 'xxxx')
        self.assertEqual(warmup2.string_times('', 4), '')
        self.assertEqual(warmup2.string_times('code', 2), 'codecode')
        self.assertEqual(warmup2.string_times('code', 3), 'codecodecode')
    
    def test_front_times(self):
        self.assertEqual(warmup2.front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(warmup2.front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(warmup2.front_times('Abc', 3), 'AbcAbcAbc')
        self.assertEqual(warmup2.front_times('Ab', 4), 'AbAbAbAb')
        self.assertEqual(warmup2.front_times('A', 4), 'AAAA')
        self.assertEqual(warmup2.front_times('', 4), '')
        self.assertEqual(warmup2.front_times('Abc', 0), '')

    def test_string_bits(self):
        self.assertEqual(warmup2.string_bits('Hello'), 'Hlo')
        self.assertEqual(warmup2.string_bits('Hi'), 'H')
        self.assertEqual(warmup2.string_bits('Heeololeo'), 'Hello')
        self.assertEqual(warmup2.string_bits('HiHiHi'), 'HHH')
        self.assertEqual(warmup2.string_bits(''), '')
        self.assertEqual(warmup2.string_bits('Greetings'), 'Getns')
        self.assertEqual(warmup2.string_bits('Chocoate'), 'Coot')
        self.assertEqual(warmup2.string_bits('pi'), 'p')
        self.assertEqual(warmup2.string_bits('Hello Kitten'), 'HloKte')
        self.assertEqual(warmup2.string_bits('hxaxpxpxy'), 'happy')

    def test_string_splosion(self):
        self.assertEqual(warmup2.string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(warmup2.string_splosion('abc'), 'aababc' )
        self.assertEqual(warmup2.string_splosion('ab'), 'aab')
        self.assertEqual(warmup2.string_splosion('x'), 'x')
        self.assertEqual(warmup2.string_splosion('fade'), 'ffafadfade')
        self.assertEqual(warmup2.string_splosion('There'), 'TThTheTherThere' )
        self.assertEqual(warmup2.string_splosion('Kitten'), 'KKiKitKittKitteKitten' )
        self.assertEqual(warmup2.string_splosion('Bye'), 'BByBye' )
        self.assertEqual(warmup2.string_splosion('Good'), 'GGoGooGood' )
        self.assertEqual(warmup2.string_splosion('Bad'), 'BBaBad' )

    def test_last2(self):
        self.assertEqual(warmup2.last2('hixxhi'), 1)
        self.assertEqual(warmup2.last2('xaxxaxaxx'), 1)
        self.assertEqual(warmup2.last2('axxxaaxx'), 2)
        self.assertEqual(warmup2.last2('xxaxxaxxaxx'), 3)
        self.assertEqual(warmup2.last2('xaxaxaxx'), 0)
        self.assertEqual(warmup2.last2('xxxx'), 2)
        self.assertEqual(warmup2.last2('13121312'), 1)
        self.assertEqual(warmup2.last2('11212'), 1)
        self.assertEqual(warmup2.last2('13121311'), 0)
        self.assertEqual(warmup2.last2('1717171'), 2)
        self.assertEqual(warmup2.last2('hi'), 0)
        self.assertEqual(warmup2.last2('h'), 0)
        self.assertEqual(warmup2.last2(''), 0)

    def test_array_count9(self):
        self.assertEqual(warmup2.array_count9([1, 2, 9]), 1)
        self.assertEqual(warmup2.array_count9([1, 9, 9]), 2)
        self.assertEqual(warmup2.array_count9([1, 9, 9, 3, 9]), 3)
        self.assertEqual(warmup2.array_count9([1, 2, 3]), 0)
        self.assertEqual(warmup2.array_count9([]), 0)
        self.assertEqual(warmup2.array_count9([4, 2, 4, 3, 1]), 0)
        self.assertEqual(warmup2.array_count9([9, 2, 4, 3, 1]), 1)
    
    def test_array_front9(self):
        self.assertEqual(warmup2.array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(warmup2.array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(warmup2.array_front9([1, 2, 3, 4, 5]), False)
        self.assertEqual(warmup2.array_front9([9, 2, 3]), True )
        self.assertEqual(warmup2.array_front9([1, 9, 9]), True)
        self.assertEqual(warmup2.array_front9([1, 2, 3]), False)
        self.assertEqual(warmup2.array_front9([1, 9]), True)
        self.assertEqual(warmup2.array_front9([5, 5]), False)
        self.assertEqual(warmup2.array_front9([2]), False)
        self.assertEqual(warmup2.array_front9([9]), True)
        self.assertEqual(warmup2.array_front9([]), False)
        self.assertEqual(warmup2.array_front9([3, 9, 2, 3, 3]), True)
    
    def test_array123(self):
        self.assertEqual(warmup2.array123([1, 1, 2, 3, 1]), True)
        self.assertEqual(warmup2.array123([1, 1, 2, 4, 1]), False)
        self.assertEqual(warmup2.array123([1, 1, 2, 1, 2, 3]), True)
        self.assertEqual(warmup2.array123([1, 1, 2, 1, 2, 1]), False)
        self.assertEqual(warmup2.array123([1, 2, 3, 1, 2, 3]), True)
        self.assertEqual(warmup2.array123([1, 2, 3]), True)
        self.assertEqual(warmup2.array123([1, 1, 1]), False)
        self.assertEqual(warmup2.array123([1, 2]), False)
        self.assertEqual(warmup2.array123([1]), False )
        self.assertEqual(warmup2.array123([]), False)
    
    def test_string_match(self):
        self.assertEqual(warmup2.string_match('xxcaazz','xxbaaz'), 3)
        self.assertEqual(warmup2.string_match('abc','abc'), 2)
        self.assertEqual(warmup2.string_match('abc',  'axc'), 0)
        self.assertEqual(warmup2.string_match('hello','he'), 1)
        self.assertEqual(warmup2.string_match('he', 'hello'), 1)
        self.assertEqual(warmup2.string_match('h', 'hello'), 0)
        self.assertEqual(warmup2.string_match('', 'hello'), 0)
        self.assertEqual(warmup2.string_match('aabbccdd', 'abbbxxd'), 1)
        self.assertEqual(warmup2.string_match('aaxxaaxx', 'iaxxai'), 3)
        self.assertEqual(warmup2.string_match('iaxxai','aaxxaaxx'), 3) 
    
    def test_string_x(self):
        self.assertEqual(warmup2.string_x('xxHxix'), 'xHix')
        self.assertEqual(warmup2.string_x('abxxxcd'), 'abcd')
        self.assertEqual(warmup2.string_x('xabxxxcdx'), 'xabcdx')
        self.assertEqual(warmup2.string_x('xKittenx'), 'xKittenx')
        self.assertEqual(warmup2.string_x('Hello'), 'Hello')
        self.assertEqual(warmup2.string_x('xx'), 'xx')
        self.assertEqual(warmup2.string_x('x'), 'x')
        self.assertEqual(warmup2.string_x(''), '')
    
    def test_alt_pairs(self):
        self.assertEqual(warmup2.alt_pairs('kitten'), 'kien')
        self.assertEqual(warmup2.alt_pairs('Chocolate'), 'Chole')
        self.assertEqual(warmup2.alt_pairs('CodingHorror'), 'Congrr')
        self.assertEqual(warmup2.alt_pairs('yak'), 'ya')
        self.assertEqual(warmup2.alt_pairs('ya'), 'ya')
        self.assertEqual(warmup2.alt_pairs('y'), 'y')
        self.assertEqual(warmup2.alt_pairs(''), '')
        self.assertEqual(warmup2.alt_pairs('ThisThatTheOther'), 'ThThThth')
    
    def test_string_yak(self):
        self.assertEqual(warmup2.string_yak('yakpak'), 'pak')
        self.assertEqual(warmup2.string_yak('pakyak'), 'pak')
        self.assertEqual(warmup2.string_yak('yak123ya'), '123ya')
        self.assertEqual(warmup2.string_yak('yak'), '')
        self.assertEqual(warmup2.string_yak('yakxxxyak'), 'xxx')
        self.assertEqual(warmup2.string_yak('HiyakHi'), 'HiHi')
        self.assertEqual(warmup2.string_yak('xxxyakyyyakzzz'), 'xxxyyzzz')
    
    def test_array_667(self):
        self.assertEqual(warmup2.array_667([6, 6, 2]), 1)
        self.assertEqual(warmup2.array_667([6, 6, 2, 6]), 1)
        self.assertEqual(warmup2.array_667([6, 7, 2, 6]), 1)
        self.assertEqual(warmup2.array_667([6, 6, 2, 6, 7]), 2)
        self.assertEqual(warmup2.array_667([1, 6, 3]), 0)
        self.assertEqual(warmup2.array_667([6, 1]), 0)
        self.assertEqual(warmup2.array_667([]), 0)
        self.assertEqual(warmup2.array_667([3, 6, 7, 6]), 1)
        self.assertEqual(warmup2.array_667([3, 6, 6, 7]), 2)
        self.assertEqual(warmup2.array_667([6, 3, 6, 6]), 1)
        self.assertEqual(warmup2.array_667([6, 7, 6, 6]), 2)
        self.assertEqual(warmup2.array_667([1, 2, 3, 5, 6]), 0)
        self.assertEqual(warmup2.array_667([1, 2, 3, 6, 6]), 1)

if __name__ == '__main__':
    unittest.main()