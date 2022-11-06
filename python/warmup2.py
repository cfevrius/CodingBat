def string_times(str, n):
    return str * n

def front_times(str, n):
    end_pos = min(len(str), 3)
    front = str[:end_pos]
    return front * n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    lst_of_substrs = [str[:i] for i in range(1, len(str)+1)]
    return ''.join(lst_of_substrs)

def last2(str):
    search_str = str[-2:]
    occurrences = [i for i in range(len(str)) if str.startswith(search_str, i, -1)]
    return len(occurrences)

def array_count9(nums):
    return len([i for i in nums if i == 9])

def array_front9(nums):
    end = min(len(nums), 4)
    front = nums[:end]
    return 9 in front

def array123(nums):
    occurrences = [i for i in range(len(nums) - 2) if nums[i:i+3] == [1, 2, 3]]
    return len(occurrences) > 0

def string_match(a, b):
    lower = min(len(a), len(b))
    occurrences = [i for i in range(lower - 1) if a[i:i+2] == b[i:i+2]]
    return len(occurrences)

def back_around(str):
    back = str[-1]
    return back + str + back

def or_35(n):
    return n % 3 == 0 or n % 5 == 0

def front_22(str):
    front = str if len(str) < 2 else str[:2]
    return front + str + front

def start_hi(str):
    return str.startswith('hi')

def icy_hot(temp1, temp2):
    one_icy_another_hot = lambda x, y : x < 0 and y > 100
    return one_icy_another_hot(temp1, temp2) or one_icy_another_hot(temp2, temp1)

def in_1020(a, b):
    in_range = lambda x : x >= 10 and x <= 20
    return in_range(a) or in_range(b)

def has_teen(a, b, c):
    is_teen = lambda x : x >= 13 and x <= 19
    return is_teen(a) or is_teen(b) or is_teen(c)

def lone_teen(a, b):
    is_teen = lambda x : x >= 13 and x <= 19
    teens = [x for x in [a, b] if is_teen(x)]
    return len(teens) == 1

def del_del(str):
    return str[0] + str[4:] if len(str) >= 4 and str[1:4] == 'del' else str

def mix_start(str):
    return len(str) >= 3 and str[1:3] == 'ix'

def start_oz(str):
    first_char_is_o = len(str) >= 1 and str[0] == 'o'
    second_char_is_z = len(str) >= 2 and str[1] == 'z'
    return ''.join(['o' if first_char_is_o else '', 'z' if second_char_is_z else ''])

def int_max(a, b, c):
    return max(a, b, c)

def close_10(a, b):
    a_dist_10 = abs(10 - a)
    b_dist_10 = abs(10 - b)
    return 0 if a_dist_10 == b_dist_10 else (a if a_dist_10 < b_dist_10 else b)

def in_3040(a, b):
    in_30_40 = lambda x : x >= 30 and x <= 40
    in_40_50 = lambda x : x >= 40 and x <= 50
    return (in_30_40(a) and in_30_40(b)) or (in_40_50(a) and in_40_50(b))

def max_1020(a, b):
    nums_in_range = [x for x in [a, b] if x >= 10 and x <= 20]
    return 0 if len(nums_in_range) == 0 else max(nums_in_range)
