'''
Given a string, return a new string where the first 
and last chars have been exchanged.
'''
def front_back(str):
    result = str
    if len(str) > 1:
        result = str[-1] + str[1:-1] + str[0]
    return result

# Test code
assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'
assert front_back('abc') == 'cba'
assert front_back('') == ''
assert front_back('Chocolate') == 'ehocolatC'
assert front_back('aavJ') == 'Java'
assert front_back('hello') == 'oellh'
