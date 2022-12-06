# Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" 
# and the 'z' in "fez" count, but not the 'y' in "yellow" (not case sensitive). We'll say 
# that a y or z is at the end of a word if there is not an alphabetic letter immediately 
# following it. (Note: str.isalpha(char) tests if a char is an alphabetic letter.)
def count_yz(string):
    only_alphas = ''.join([v if str.isalpha(v) else ' ' 
                           for i, v in enumerate(string)])
    words = only_alphas.lower().split(' ')
    words_that_ends_in_z_or_y = [word
                                 for word in words
                                 if word.endswith('z') or word.endswith('y')]
    return len(words_that_ends_in_z_or_y)

# Given two strings, base and remove, return a version of the base string where all 
# instances of the remove string have been removed (not case sensitive). You may assume that 
# the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" 
# removing "xx" leaves "x".
def without_string(base, remove):
    return None

# Given a string, return true if the number of appearances of "is" anywhere in the string is 
# equal to the number of appearances of "not" anywhere in the string (case sensitive).
def equal_is_not(string):
    return None

# We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to 
# its left or right. Return true if all the g's in the given string are happy.
def g_happy(string):
    return None

# We'll say that a "triple" in a string is a char appearing three times in a row. Return the 
# number of triples in the given string. The triples may overlap.
def count_triple(string):
    return None

# Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other
# characters. Return 0 if there are no digits in the string. (Note: str.isdecimal(char) tests 
# if a char is one of the chars '0', '1', .. '9'. int(string) converts a string to an int.)
def sum_digits(string):
    return None

# Given a string, return the longest substring that appears at both the beginning and end of the 
# string without overlapping. For example, sameEnds("abXab") is "ab".
def same_ends(string):
    return None

# Given a string, look for a mirror image (backwards) string at both the beginning and end of the 
# given string. In other words, zero or more characters at the very begining of the given string, 
# and at the very end of the string in reverse order (possibly overlapping). For example, the string 
# "abXYZba" has the mirror end "ab".
def mirror_ends(string):
    return None

# Given a string, return the length of the largest "block" in the string. A block is a run of adjacent 
# chars that are the same.
def max_block(string):
    return None

# Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. 
# A number is a series of 1 or more digit chars in a row. (Note: str.isdecimal(char) tests if a char 
# is one of the chars '0', '1', .. '9'. int(string) converts a string to an int.)
def sum_numbers(string):
    return None

# Given a string, return a string where every appearance of the lowercase word "is" has been replaced with 
# "is not". The word "is" should not be immediately preceeded or followed by a letter -- so for example the 
# "is" in "this" does not count. (Note: str.isalpha(char) tests if a char is a letter.)
def not_replace(string):
    return None
