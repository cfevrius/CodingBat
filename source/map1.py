def map_bully(mp):
    """Modify and return the given map as follows: if the key 'a' has a value, set the key 'b' 
    to have that value, and set the key 'a' to have the value ''. Basically 'b' is a bully, 
    taking the value and replacing it with the empty string.
    """
    if 'a' in mp:
        mp['a'], mp['b'] = '', mp['a']
    return mp

def map_share(mp):
    """Modify and return the given map as follows: if the key 'a' has a value, set the key 'b' 
    to have that same value. In all cases remove the key 'c', leaving the rest of the map 
    unchanged.
    """
    if 'a' in mp:
        mp['b'] = mp['a']
    if 'c' in mp:
        del mp['c']
    return mp

def map_ab(mp):
    """Modify and return the given map as follows: for this problem the map may or may not contain 
    the 'a' and 'b' keys. If both keys are present, append their 2 string values together and 
    store the result under the key 'ab'.
    """
    if 'a' in mp and 'b' in mp:
        mp['ab'] = mp['a'] + mp['b']
    return mp

def topping1(mp):
    """Given a map of food keys and topping values, modify and return the map as follows: if the 
    key 'ice cream' is present, set its value to 'cherry'. In all cases, set the key 'bread' 
    to have the value 'butter'.
    """
    if 'ice cream' in mp:
        mp['ice cream'] = 'cherry'
    mp['bread'] = 'butter'
    return mp

def topping2(mp):
    """Given a map of food keys and their topping values, modify and return the map as follows: 
    if the key 'ice cream' has a value, set that as the value for the key 'yogurt' also. If 
    the key 'spinach' has a value, change that value to 'nuts'.
    """
    if 'ice cream' in mp:
        mp['yogurt'] = mp['ice cream']
    if 'spinach' in mp:
        mp['spinach'] = 'nuts'
    return mp

def topping3(mp):
    """Given a map of food keys and topping values, modify and return the map as follows: if 
    the key 'potato' has a value, set that as the value for the key 'fries'. If the key 'salad' 
    has a value, set that as the value for the key 'spinach'.
    """
    if 'potato' in mp:
        mp['fries'] = mp['potato']
    if 'salad' in mp:
        mp['spinach'] = mp['salad']
    return mp

def map_ab2(mp):
    """Modify and return the given map as follows: if the keys 'a' and 'b' are both in the map 
    and have equal values, remove them both.
    """
    if 'a' in mp and 'b' in mp and mp['a'] == mp['b']:
        del mp['a']
        del mp['b']
    return mp

def map_ab3(mp):
    """Modify and return the given map as follows: if exactly one of the keys 'a' or 'b' has a 
    value in the map (but not both), set the other to have that same value in the map.
    """
    if 'a' in mp and 'b' not in mp:
        mp['b'] = mp['a']
    elif 'b' in mp and 'a' not in mp:
        mp['a'] = mp['b']
    return mp

def map_ab4(mp):
    """Modify and return the given map as follows: if the keys 'a' and 'b' have values that have 
    different lengths, then set 'c' to have the longer value. If the values exist and have the 
    same length, change them both to the empty string in the map.
    """
    if 'a' in mp and 'b' in mp:
        if len(mp['a']) == len(mp['b']):
            mp['a'], mp['b'] = '', ''
        else:
            mp['c'] = max(mp['a'], mp['b'], key=len)
    return mp
