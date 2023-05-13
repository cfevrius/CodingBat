def word0(strings):
    """Given an array of strings, return a Map<String, Integer> containing a key for 
    every different string in the array, always with the value 0. For example the 
    string "hello" makes the pair "hello":0. We'll do more complicated counting 
    later, but for this problem the value is simply 0.
    """
    return {string: 0 for string in set(strings)}

def word_len(strings):
    """Given an array of strings, return a Map<String, Integer> containing a key for 
    every different string in the array, and the value is that string's length.
    """
    return {string: len(string) for string in set(strings)}

def pairs(strings):
    """Given an array of non-empty strings, create and return a Map<String, String> as 
    follows: for each string add its first character as a key with its last character 
    as the value.
    """
    return {string[0] : string[-1] for string in strings}

def word_count(strings):
    """The classic word-count algorithm: given an array of strings, return a Map<String, Integer> 
    with a key for each different string, with the value the number of times that string appears 
    in the array.
    """
    return {string: strings.count(string) for string in set(strings)}

def first_char(strings):
    """Given an array of non-empty strings, return a Map<String, String> with a key for every 
    different first character seen, with the value of all the strings starting with that 
    character appended together in the order they appear in the array.
    """
    unique_first_chars = set([string[0] for string in strings])
    def all_strings_with_first_char(char):
        return ''.join([string for string in strings if string.startswith(char)])
    return {char : all_strings_with_first_char(char) for char in unique_first_chars}

def word_appends(strings):
    """Loop over the given array of strings to build a result string like this: when a string 
    appears the 2nd, 4th, 6th, etc. time in the array, append the string to the result. 
    Return the empty string if no string appears a 2nd time.
    """
    word_count = {}
    result = ''
    for string in strings:
        if string not in word_count:
            word_count[string] = 0
        else:
            if word_count[string] % 2 == 0:
                result += string
            word_count[string] += 1 
    return result

def word_multiple(strings):
    """Given an array of strings, return a Map<String, Boolean> where each different string is 
    a key and its value is true if that string appears 2 or more times in the array.
    """
    return {string: strings.count(string) >= 2 for string in set(strings)}

def all_swap(strings):
    """We'll say that 2 strings "match" if they are non-empty and their first chars are the same. 
    Loop over and then return the given array of non-empty strings as follows: if a string matches 
    an earlier string in the array, swap the 2 strings in the array. When a position in the array 
    has been swapped, it no longer matches anything. Using a map, this can be solved making just 
    one pass over the array. More difficult than it looks.
    """
    word_count = {}  # first_char -> (count, first_index)
    for i, string in enumerate(strings):
        first_char = string[0]
        if len(string) > 0 and first_char not in word_count:
            word_count[first_char] = (1, i)
        else:
            # swap
            previous_index = word_count[first_char][1]
            strings[previous_index], strings[i] = strings[i], strings[previous_index]

            del word_count[first_char]
    return strings

def first_swap(strings):
    """We'll say that 2 strings "match" if they are non-empty and their first chars are the same. Loop 
    over and then return the given array of non-empty strings as follows: if a string matches an 
    earlier string in the array, swap the 2 strings in the array. A particular first char can only 
    cause 1 swap, so once a char has caused a swap, its later swaps are disabled. Using a map, this 
    can be solved making just one pass over the array. More difficult than it looks.
    """
    word_count = {}
    for i, string in enumerate(strings):
        first_char = string[0]
        if len(string) > 0 and first_char not in word_count:
            word_count[first_char] = (1, i)
        else:
            if word_count[first_char][0] == 1:
                # swap
                previous_index = word_count[first_char][1]
                strings[previous_index], strings[i] = strings[i], strings[previous_index]

                word_count[first_char] = (word_count[first_char][0] + 1, i)
    return strings
