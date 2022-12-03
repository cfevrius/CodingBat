# Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    return None

# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    return None

# Return true if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    return None

# Return the number of times that the string "code" appears anywhere in the given string, except 
# we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    return None

# Given two strings, return true if either of the strings appears at the very end of the other string, 
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
# Note: str.lower() returns the lowercase version of a string.
def end_other(a, b):
    return None

# Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
# by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
    return None

# Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.
def bob_there(str):
    return None

# We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char 
# somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. 
# Return true if the given string is xy-balanced.
def xyz_balance(str):
    return None

# Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the 
# second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
def mix_string(a, b):
    return None

# Given a string and an int n, return a string made of n repetitions of the last n characters of the string. 
# You may assume that n is between 0 and the length of the string, inclusive.
def repeat_end(str, n):
    return None

# Given a string and an int n, return a string made of the first n characters of the string, followed by the 
# first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, 
# inclusive (i.e. n >= 0 and n <= len(str)).
def repeat_front(str, n):
    return None

# Given two strings, word and a separator sep, return a big string made of count occurrences of the word, separated 
# by the separator string.
def repeat_separator(word, sep, count):
    return None

# Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear 
# somewhere else in the string? Assume that the string is not empty and that N is in the range 1..len(str).
def prefix_again(str, n):
    return None

# Given a string, does "xyz" appear in the middle of the string? To define middle, we'll say that the number of chars 
# to the left and right of the "xyz" must differ by at most one. This problem is harder than it looks.
def xyz_middle(str):
    return None

# A sandwich is two pieces of bread with something in between. Return the string that is between the first and last 
# appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.
def get_sandwich(str):
    return None

# Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, 
# they are the same.
def same_star_char(str):
    return None

# Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields "bca". 
# Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of fewer than 
# 3 chars at the end.
def one_two(str):
    return None

# Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string 
# where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".
def zip_zap(str):
    return None

# Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left 
# and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".
def star_out(str):
    return None

# Given a string and a non-empty word string, return a version of the original String where all chars have been replaced by pluses 
# ("+"), except for appearances of the word string which are preserved unchanged.
def plus_out(str, word):
    return None
    
# Given a string and a non-empty word string, return a string made of each char just before and just after every appearance of the 
# word in the string. Ignore cases where there is no char before or after the word, and a char may be included twice if it is between 
# two words.
def word_ends(str, word):
    return None
