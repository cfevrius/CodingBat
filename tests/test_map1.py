import unittest
import solutions.map1 as map1

class TestMap1(unittest.TestCase):
    def test_map_bully(self):
        self.assertEqual(map1.map_bully({'a': 'candy', 'b': 'dirt'}), {'a': '', 'b': 'candy'})
        self.assertEqual(map1.map_bully({'a': 'candy'}), {'a': '', 'b': 'candy'})
        self.assertEqual(map1.map_bully({'a': 'candy', 'b': 'carrot', 'c': 'meh'}), {'a': '', 'b': 'candy', 'c': 'meh'})
        self.assertEqual(map1.map_bully({'b': 'carrot'}), {'b': 'carrot'})
        self.assertEqual(map1.map_bully({'c': 'meh'}), {'c': 'meh'})
        self.assertEqual(map1.map_bully({'a': 'sparkle', 'c': 'meh'}), {'a': '', 'b': 'sparkle', 'c': 'meh'})
    
    def test_map_share(self):
        self.assertEqual(map1.map_share({'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}), {'a': 'aaa', 'b': 'aaa'})
        self.assertEqual(map1.map_share({'b': 'xyz', 'c': 'ccc'}), {'b': 'xyz'})
        self.assertEqual(map1.map_share({'a': 'aaa', 'c': 'meh', 'd': 'hi'}), {'a': 'aaa', 'b': 'aaa', 'd': 'hi'})
        self.assertEqual(map1.map_share({'a': 'xyz', 'b': '1234', 'c': 'yo', 'z': 'zzz'}), {'a': 'xyz', 'b': 'xyz', 'z': 'zzz'})
        self.assertEqual(map1.map_share({'a': 'xyz', 'b': '1234', 'c': 'yo', 'd': 'ddd', 'e': 'everything'}), {'a': 'xyz', 'b': 'xyz', 'd': 'ddd', 'e': 'everything'})
    
    def test_map_ab(self):
        self.assertEqual(map1.map_ab({'a': 'Hi', 'b': 'There'}), {'a': 'Hi', 'ab': 'HiThere', 'b': 'There'})
        self.assertEqual(map1.map_ab({'a': 'Hi'}), {'a': 'Hi'})
        self.assertEqual(map1.map_ab({'b': 'There'}), {'b': 'There'})
        self.assertEqual(map1.map_ab({'c': 'meh'}), {'c': 'meh'})
        self.assertEqual(map1.map_ab({'a': 'aaa', 'ab': 'nope', 'b': 'bbb', 'c': 'ccc'}), {'a': 'aaa', 'ab': 'aaabbb', 'b': 'bbb', 'c': 'ccc'})
        self.assertEqual(map1.map_ab({'ab': 'nope', 'b': 'bbb', 'c': 'ccc'}), {'ab': 'nope', 'b': 'bbb', 'c': 'ccc'})

    def test_topping1(self):
        self.assertEqual(map1.topping1({'ice cream': 'peanuts'}), {'bread': 'butter', 'ice cream': 'cherry'})
        self.assertEqual(map1.topping1({}), {'bread': 'butter'})
        self.assertEqual(map1.topping1({'pancake': 'syrup'}), {'bread': 'butter', 'pancake': 'syrup'})
        self.assertEqual(map1.topping1({'bread': 'dirt', 'ice cream': 'strawberries'}), {'bread': 'butter', 'ice cream': 'cherry'})
        self.assertEqual(map1.topping1({'bread': 'jam', 'ice cream': 'strawberries', 'salad': 'oil'}), {'bread': 'butter', 'ice cream': 'cherry', 'salad': 'oil'})
    
    def test_topping2(self):
        self.assertEqual(map1.topping2({'ice cream': 'cherry'}), {'yogurt': 'cherry', 'ice cream': 'cherry'})
        self.assertEqual(map1.topping2({'spinach': 'dirt', 'ice cream': 'cherry'}), {'yogurt': 'cherry', 'spinach': 'nuts', 'ice cream': 'cherry'})
        self.assertEqual(map1.topping2({'yogurt': 'salt'}), {'yogurt': 'salt'})
        self.assertEqual(map1.topping2({'yogurt': 'salt', 'bread': 'butter'}), {'yogurt': 'salt', 'bread': 'butter'})
        self.assertEqual(map1.topping2({}), {})
        self.assertEqual(map1.topping2({'ice cream': 'air', 'salad': 'oil'}), {'yogurt': 'air', 'ice cream': 'air', 'salad': 'oil'})
    
    def test_topping3(self):
        self.assertEqual(map1.topping3({'potato': 'ketchup'}), {'potato': 'ketchup', 'fries': 'ketchup'})
        self.assertEqual(map1.topping3({'potato': 'butter'}), {'potato': 'butter', 'fries': 'butter'})
        self.assertEqual(map1.topping3({'salad': 'oil', 'potato': 'ketchup'}), {'spinach': 'oil', 'salad': 'oil', 'potato': 'ketchup', 'fries': 'ketchup'})
        self.assertEqual(map1.topping3({'toast': 'butter', 'salad': 'oil', 'potato': 'ketchup'}), {'toast': 'butter', 'spinach': 'oil', 'salad': 'oil', 'potato': 'ketchup', 'fries': 'ketchup'})
        self.assertEqual(map1.topping3({}), {})
        self.assertEqual(map1.topping3({'salad': 'pepper', 'fries': 'salt'}), {'spinach': 'pepper', 'salad': 'pepper', 'fries': 'salt'})
    
    def test_map_ab2(self):
        self.assertEqual(map1.map_ab2({'a': 'aaa', 'b': 'aaa', 'c': 'cake'}), {'c': 'cake'})
        self.assertEqual(map1.map_ab2({'a': 'aaa', 'b': 'bbb'}), {'a': 'aaa', 'b': 'bbb'})
        self.assertEqual(map1.map_ab2({'a': 'aaa', 'b': 'bbb', 'c': 'aaa'}), {'a': 'aaa', 'b': 'bbb', 'c': 'aaa'})
        self.assertEqual(map1.map_ab2({'a': 'aaa'}), {'a': 'aaa'})
        self.assertEqual(map1.map_ab2({'b': 'bbb'}), {'b': 'bbb'})
        self.assertEqual(map1.map_ab2({'a': '', 'b': '', 'c': 'ccc'}), {'c': 'ccc'})
        self.assertEqual(map1.map_ab2({}), {})
        self.assertEqual(map1.map_ab2({'a': 'a', 'b': 'b', 'z': 'zebra'}), {'a': 'a', 'b': 'b', 'z': 'zebra'})
    
    def test_map_ab3(self):
        self.assertEqual(map1.map_ab3({'a': 'aaa', 'c': 'cake'}), {'a': 'aaa', 'b': 'aaa', 'c': 'cake'})
        self.assertEqual(map1.map_ab3({'b': 'bbb', 'c': 'cake'}), {'a': 'bbb', 'b': 'bbb', 'c': 'cake'})
        self.assertEqual(map1.map_ab3({'a': 'aaa', 'b': 'bbb', 'c': 'cake'}), {'a': 'aaa', 'b': 'bbb', 'c': 'cake'})
        self.assertEqual(map1.map_ab3({'ccc': 'ccc'}), {'ccc': 'ccc'})
        self.assertEqual(map1.map_ab3({'c': 'a', 'd': 'b'}), {'c': 'a', 'd': 'b'})
        self.assertEqual(map1.map_ab3({}), {})
        self.assertEqual(map1.map_ab3({'a': ''}), {'a': '', 'b': ''})
        self.assertEqual(map1.map_ab3({'b': ''}), {'a': '', 'b': ''})
        self.assertEqual(map1.map_ab3({'a': '', 'b': ''}), {'a': '', 'b': ''})
        self.assertEqual(map1.map_ab3({'aa': 'aa', 'a': 'apple', 'z': 'zzz'}), {'aa': 'aa', 'a': 'apple', 'b': 'apple', 'z': 'zzz'})
    
    def test_map_ab4(self):
        self.assertEqual(map1.map_ab4({'a': 'aaa', 'b': 'bb', 'c': 'cake'}), {'a': 'aaa', 'b': 'bb', 'c': 'aaa'})
        self.assertEqual(map1.map_ab4({'a': 'aa', 'b': 'bbb', 'c': 'cake'}), {'a': 'aa', 'b': 'bbb', 'c': 'bbb'})
        self.assertEqual(map1.map_ab4({'a': 'aa', 'b': 'bbb'}), {'a': 'aa', 'b': 'bbb', 'c': 'bbb'})
        self.assertEqual(map1.map_ab4({'a': 'aaa'}), {'a': 'aaa'})
        self.assertEqual(map1.map_ab4({'b': 'bbb'}), {'b': 'bbb'})
        self.assertEqual(map1.map_ab4({'a': 'aaa', 'b': 'bbb', 'c': 'cake'}), {'a': '', 'b': '', 'c': 'cake'})
        self.assertEqual(map1.map_ab4({'a': 'a', 'b': 'b', 'c': 'cake'}), {'a': '', 'b': '', 'c': 'cake'})
        self.assertEqual(map1.map_ab4({'a': '', 'b': 'b', 'c': 'cake'}), {'a': '', 'b': 'b', 'c': 'b'})
        self.assertEqual(map1.map_ab4({'a': 'a', 'b': '', 'c': 'cake'}), {'a': 'a', 'b': '', 'c': 'a'})
        self.assertEqual(map1.map_ab4({'c': 'cat', 'd': 'dog'}), {'c': 'cat', 'd': 'dog'})
        self.assertEqual(map1.map_ab4({'ccc': 'ccc'}), {'ccc': 'ccc'})
        self.assertEqual(map1.map_ab4({'c': 'a', 'd': 'b'}), {'c': 'a', 'd': 'b'})
        self.assertEqual(map1.map_ab4({}), {})
        self.assertEqual(map1.map_ab4({'a': '', 'z': 'z'}), {'a': '', 'z': 'z'})
        self.assertEqual(map1.map_ab4({'b': '', 'z': 'z'}), {'b': '', 'z': 'z'})

if __name__ == '__main__':
    unittest.main()