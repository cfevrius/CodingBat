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
    return str[-1] + str + str[-1]

def or_35(n):
    return n % 3 == 0 or n % 5 == 0

def front_22(str):
    front = str[:2] if len(str) > 2 else str
    return front + str + front