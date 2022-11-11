# Given a string name, e.g. "Bob", return a 
# greeting of the form "Hello Bob!".
def hello_name(name):
    return f"Hello {name}!"

# Given two strings, a and b, return the result 
# of putting them together in the order abba, e.g. 
# "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
    return f"{a}{b}{b}{a}"

# The web is built with HTML strings like "<i>Yay</i>" 
# which draws Yay as italic text. In this example, the 
# "i" tag makes <i> and </i> which surround the word "Yay". 
# Given tag and word strings, create the HTML string with tags 
# around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"

# Given an "out" string length 4, such as "<<>>", and a word, return 
# a new string where the word is in the middle of the out string, e.g. "<<word>>". 
# Note: use str[i:j] to extract the string starting at index i and going 
# up to but not including index j.
def make_out_word(out, word):
    return f"{out[:2]}{word}{out[-2:]}"

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

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on 
# the outside and the longer string on the inside. The strings will not be the same length, but they 
# may be empty (length 0).
def combo_string(a, b):
    short, long = sorted([a, b], key=len)
    return f"{short}{long}{short}"

# Given 2 strings, return their concatenation, except omit the first char of each. The strings will 
# be at least length 1.
def non_start(a, b):
    return f"{a[1:]}{b[1:]}"