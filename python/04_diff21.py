def diff_21(n):
    result = abs(21 - n)
    if n > 21:
        result *= 2
    return result

# Test code
assert diff_21(19) ==  2
assert diff_21(10) == 11
assert diff_21(21) ==  0
assert diff_21(22) ==  2
assert diff_21(25) ==  8
assert diff_21(30) == 18
assert diff_21(0) == 21
assert diff_21(1) == 20
assert diff_21(2) == 19
assert diff_21(-1) == 22
assert diff_21(-2) == 23
assert diff_21(50) == 58