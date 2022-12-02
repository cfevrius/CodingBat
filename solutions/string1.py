# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
    return f'Hello {name}!'

# Given two strings, a and b, return the result of putting them together in the order 
# abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
    return f'{a}{b}{b}{a}'

# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags around the word, 
# e.g. "<i>Yay</i>".
def make_tags(tag, word):
    return f'<{tag}>{word}</{tag}>'

# Given an "out" string length 4, such as "<<>>", and a word, return a new string where 
# the word is in the middle of the out string, e.g. "<<word>>". Note: use str[i:j] to 
# extract the string starting at index i and going up to but not including index j.
def make_out_word(out, word):
    return f'{out[:2]}{word}{out[-2:]}'

# Given a string, return a new string made of 3 copies of the last 2 chars of the 
# original string. The string length will be at least 2.
def extra_end(str):
    return 3 * str[-2:]

# Given a string, return the string made of its first two chars, so the String "Hello" 
# yields "He". If the string is shorter than length 2, return whatever there is, so "X" 
# yields "X", and the empty string "" yields the empty string "". Note that len(str) returns 
# the length of a string.
def first_two(str):
    return str[:2]

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    return str[:(len(str) // 2)]

# Given a string, return a version without the first and last char, so "Hello" yields "ell". The 
# string length will be at least 2.
def without_end(str):
    return str[1:-1]

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter 
# string on the outside and the longer string on the inside. The strings will not be the same 
# length, but they may be empty (length 0).
def combo_string(a, b):
    short, long = sorted([a, b], key=len)
    return f'{short}{long}{short}'

# Given 2 strings, return their concatenation, except omit the first char of each. The strings 
# will be at least length 1.
def non_start(a, b):
    return f'{a[1:]}{b[1:]}'

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
# The string length will be at least 2.
def left_2(str):
    return f'{str[2:]}{str[:2]}'

# Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. 
# The string length will be at least 2.
def right_2(str):
    return f'{str[-2:]}{str[:-2]}'

# Given a string, return a string length 1 from its front, unless front is false, in which case 
# return a string length 1 from its back. The string will be non-empty.
def the_end(str, front):
    return str[0:1] if front else str[-1:]

# Given a string, return a version without both the first and last char of the string. The string 
# may be any length, including 0.
def without_end_2(str):
    return str[1:-1]

# Given a string of even length, return a string made of the middle two chars, so the string "string" 
# yields "ri". The string length will be at least 2.
def middle_two(str):
    start = len(str) // 2 - 1
    return str[start:start + 2]

# Given a string, return true if it ends in "ly".
def ends_ly(str):
    return str[-2:] == 'ly'

# Given a string and an int n, return a string made of the first and last n chars from the string. The 
# string length will be at least n.
def n_twice(str, n):
    return '' if n == 0 else f'{str[:n]}{str[-n:]}'

# Given a string and an index, return a string length 2 starting at the given index. If the index 
# is too big or too small to define a string length 2, use the first 2 chars. The string length 
# will be at least 2.
def two_char(str, index):
    return str[:2] if (index > (len(str) - 2) or index < 0) else str[index:index+2]

# Given a string of odd length, return the string length 3 from its middle, so "Candy" yields 
# "and". The string length will be at least 3.
def middle_three(str):
    index = len(str) // 2 - 1
    return str[index: index + 3]

# Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as 
# with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, including 0. 
# Note: use == to compare 2 strings.
def has_bad(str):
    matches = [i for i, _ in enumerate(str[-3:]) if str[i:i+3] == 'bad']
    return 0 in matches or 1 in matches

# Given a string, return a string length 2 made of its first 2 chars. If the string length is 
# less than 2, use '@' for the missing chars.
def at_first(str):
    return f"{str[:2]}{'@' * (2 - len(str))}"

# Given 2 strings, a and b, return a new string made of the first char of a and the last char 
# of b, so "yo" and "java" yields "ya". If either string is length 0, use '@' for its 
# missing char.
def last_chars(a, b):
    return f"{a[0] if len(a) > 0 else '@'}{b[-1] if len(b) > 0 else '@'}"

# Given two strings, append them together (known as "concatenation") and return the result. 
# However, if the concatenation creates a double-char, then omit one of the chars, so 
# "abc" and "cat" yields "abcat".
def con_cat(a, b):
    return f'{a}{b if b[0:1] != a[-1:] else b[1:]}'

# Given a string of any length, return a new string where the last 2 chars, if present, are 
# swapped, so "coding" yields "codign".
def last_two(str):
    return f'{str[:-2]}{str[-1:]}{str[-2:-1]}'

# Given a string, if the string begins with "red" or "blue" return that color string, otherwise 
# return the empty string.
def see_color(str):
    return 'red' if str.startswith('red') else 'blue' if str.startswith('blue') else ''

# Given a string, return true if the first 2 chars in the string also appear at the end of the 
# string, such as with "edited".
def front_again(str):
    return str[:2] == str[-2:] if len(str) >= 2 else False

# Given two strings, append them together (known as "concatenation") and return the result. 
# However, if the strings are different lengths, omit chars from the longer string so it 
# is the same length as the shorter string. So "Hello" and "Hi" yield "loHi". The strings 
# may be any length.
def min_cat(a, b):
    shorter, longer = sorted([a, b], key=len)
    index = len(shorter)
    adjust_str = lambda x : x if x == shorter else x[-index:] if index > 0 else ''
    return f'{adjust_str(a)}{adjust_str(b)}'

# Given a string, return a new string made of 3 copies of the first 2 chars of the 
# original string. The string may be any length. If there are fewer than 2 chars, 
# use whatever is there.
def extra_front(str):
    return 3 * str[:2]

# Given a string, if a length 2 substring appears at both its beginning and end, return 
# a string without the substring at the beginning, so "HelloHe" yields "lloHe". The substring 
# may overlap with itself, so "Hi" yields "". Otherwise, return the original string unchanged.
def without2(str):
    return str[2:] if str[:2] == str[-2:] and len(str) >= 2 else str

# Given a string, return a version without the first 2 chars. Except keep the first char if it 
# is 'a' and keep the second char if it is 'b'. The string may be any length. Harder than it looks.
def de_front(str):
    return ''.join([x for i, x in enumerate(str) if (i != 0 or x == 'a')  and (i != 1 or x == 'b')])

# Given a string and a second "word" string, we'll say that the word matches the string if it 
# appears at the front of the string, except its first char does not need to match exactly. On 
# a match, return the front of the string, or otherwise return the empty string. So, so with the 
# string "hippo" the word "hi" returns "hi" and "xip" returns "hip". The word will be at least 
# length 1.
def start_word(str, word):
    return str[:len(word)] if str[1:len(word)] == word[1:] else ''

# Given a string, if the first or last chars are 'x', return the string without those 'x' chars, 
# and otherwise return the string unchanged.
def without_x(str):
    return ''.join([x for i, x in enumerate(str) if (i != 0 or x != 'x') and (i != (len(str) - 1) or x != 'x') ])

# Given a string, if one or both of the first 2 chars is 'x', return the string without those 
# 'x' chars, and otherwise return the string unchanged. This is a little harder than it looks.
def without_x_2(str):
    return ''.join([x for i, x in enumerate(str) if (i != 0 or x != 'x') and (i != 1 or x != 'x')])