def sleep_in(weekday, vacation):
    return not weekday or vacation

# Test code
assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True