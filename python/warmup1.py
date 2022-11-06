def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(aSmile, bSmile):
    return aSmile and bSmile or (not aSmile and not bSmile)

def sum_double(a, b):
    result = a + b if a !=b else 2 * (a + b)
    return result

def diff_21(n):
    diff = abs(21 - n)
    result = diff if n <= 21 else 2 * diff
    return result

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes_10(a, b):
    return a == 10 or b == 10 or a + b == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    result = (a < 0 and b < 0) if negative else (a * b) < 0
    return result

def not_string(str):
    result = "not " + str
    if len(str) >= 3 and str[0:3] == "not" :
        result = str
    return result

def missing_char(str, n):
    return str[0:n] + str[n+1:]

def front_back(str):
    result = (str[-1] + str[1:-1] + str[0]) if len(str) > 1 else str
    return result

def front_3(str):
    front = str[0:3] if len(str) >= 3 else str
    return 3 * front

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
