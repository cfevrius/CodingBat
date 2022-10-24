'''
Given a string, return a new string which is 3 copies of the front
(the first 3 chars). If the string length is less than 3, the front is 
whatever is there.
'''
def front_3(str):
    front = str
    if len(str) >= 3:
        front = str[0:3]
    return 3 * front

assert front_3('Java') == 'JavJavJav'
assert front_3('Chocolate') == 'ChoChoCho'
assert front_3('abc') == 'abcabcabc'
assert front_3('abcXYZ') == 'abcabcabc'
assert front_3('ab') == 'ababab'
assert front_3('a') == 'aaa'
assert front_3('') == ''
