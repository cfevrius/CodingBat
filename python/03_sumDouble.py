def sum_double(a, b):
    result = a + b
    if a == b:
        result *= 2
    return result

# Test code
assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8
assert sum_double(-1, 0) == -1
assert sum_double(3, 3) == 12
assert sum_double(0, 0) == 0
assert sum_double(0, 1) == 1
assert sum_double(3, 4) == 7