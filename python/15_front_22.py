'''
Given a string, take the first 2 chars and return the string with
the 2 chars added at both the front and back, so "kitten" yields
"kikittenki". If the string length is less than 2, use whatever 
chars are there.
'''
def front_22(str):
    front = str
    if(len(str) > 2):
        front = str[:2]
    return front + str + front

assert front_22('kitten') == 'kikittenki'
assert front_22('Ha') == 'HaHaHa'
assert front_22('abc') == 'ababcab'
assert front_22('ab') == 'ababab'
assert front_22('a') == 'aaa'
assert front_22('') == ''
assert front_22('Logic') == 'LoLogicLo'

