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
    base_without_removes = ' '.join([word 
                                     for word in base.split() 
                                     if word.lower() != remove.lower()])

    # remove lowercase, uppercase, and exact matches 
    removed_all_matches = base_without_removes.replace(remove.lower(), '').replace(remove.upper(), '').replace(remove, '')
    return removed_all_matches

# Given a string, return true if the number of appearances of "is" anywhere in the string is 
# equal to the number of appearances of "not" anywhere in the string (case sensitive).
def equal_is_not(string):
    return string.count('is') == string.count('not')

# We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to 
# its left or right. Return true if all the g's in the given string are happy.
def g_happy(string):
    get_char_at_index = lambda index: string[index] if 0 <= index <= len(string) - 1 else ''
    are_gs_happy = ['g' in {get_char_at_index(i-1), get_char_at_index(i+1)} 
                    for i, v in enumerate(string) if 
                    v == 'g'] 
    return all(are_gs_happy)

# We'll say that a "triple" in a string is a char appearing three times in a row. Return the 
# number of triples in the given string. The triples may overlap.
def count_triple(string):
    triples = [i for i, _ in enumerate(string[:-2]) 
               if string[i] == string[i+1] == string[i+2]]
    return len(triples)

# Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other
# characters. Return 0 if there are no digits in the string. (Note: str.isdigit(char) tests 
# if a char is one of the chars '0', '1', .. '9'. int(string) converts a string to an int.)
def sum_digits(string):
    return sum([int(char) for char in string if str.isdigit(char)])

# Given a string, return the longest substring that appears at both the beginning and end of the 
# string without overlapping. For example, sameEnds("abXab") is "ab".
def same_ends(string):
    front_back_substrings = [(string[:i], string[-i:]) 
                             for i, v in enumerate(string[:len(string) // 2 + 1]) 
                             if i != 0]
    equal_substrings = [tup[0]
                        for tup in front_back_substrings 
                        if tup[0] == tup[1]]
    return max(equal_substrings, default='', key=len)

# Given a string, look for a mirror image (backwards) string at both the beginning and end of the 
# given string. In other words, zero or more characters at the very begining of the given string, 
# and at the very end of the string in reverse order (possibly overlapping). For example, the string 
# "abXYZba" has the mirror end "ab".
def mirror_ends(string):
    front_back_substrings = [(string[:i], string[-i:])
                             for i in range(len(string)+1)]
    mirrored_substrings = [tup[0] 
                           for tup in front_back_substrings 
                           if tup[0] == tup[1][::-1]]
    return max(mirrored_substrings, default='', key=len)

# Given a string, return the length of the largest "block" in the string. A block is a run of adjacent 
# chars that are the same.
def max_block(string):
    string_len = len(string)
    all_equal = lambda string: len(set(string)) == 1
    longest_block_at_index = lambda index: max([len(string[index:i])
                                                for i in range(string_len, index, -1)
                                                if all_equal(string[index:i])], default='') 
    blocks = [longest_block_at_index(index) for index, _ in enumerate(string)]
    return max(blocks, default=0)

# Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. 
# A number is a series of 1 or more digit chars in a row. (Note: str.isdecimal(char) tests if a char 
# is one of the chars '0', '1', .. '9'. int(string) converts a string to an int.)
def sum_numbers(string):
    string_with_only_digits = ''.join([char if str.isdigit(char) else ' ' 
                                       for char in string])
    str_numbers = string_with_only_digits.split()
    return sum(int(num) for num in str_numbers)

# Given a string, return a string where every appearance of the lowercase word "is" has been replaced with 
# "is not". The word "is" should not be immediately preceeded or followed by a letter -- so for example the 
# "is" in "this" does not count. (Note: str.isalpha(char) tests if a char is a letter.)
def not_replace(string):
    # If the index of the string is not preceeded or followed by a letter and is not followed
    # by the word 'not', this is the index of an 'is' that needs to be replaced.
    get_char_at_index = lambda index: string[index] if 0 <= index <= len(string) - 1 else ''
    is_invalid = lambda index: all([not str.isalpha(get_char_at_index(index-1)),
                                    not str.isalpha(get_char_at_index(index+2)), 
                                    string[index+3:index+6] != 'not'])
    find_matches = lambda string : [i 
                                    for i, v in enumerate(string) 
                                    if string[i:i+2] == 'is' and is_invalid(i)]
    
    single_replacement = lambda string, index: f'{string[:index]}is not{string[index+2:]}'

    while(find_matches(string)):
        string = single_replacement(string, find_matches(string)[0])

    return string
