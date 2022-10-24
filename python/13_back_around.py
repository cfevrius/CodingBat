'''
Given a string, take the last char and return a new string with
the last char added at the front and back, so "cat" yields "tcatt".
The original string will be length 1 or more.
'''
def back_around(str):
    return str[-1] + str + str[-1]

assert back_around('cat') == "tcatt"
assert back_around('Hello') == "oHelloo"
assert back_around('a') == "aaa"
assert back_around('read') == "dreadd"
assert back_around('boo') == "obooo"