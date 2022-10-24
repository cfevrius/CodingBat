def monkey_trouble(aSmile, bSmile):
    return aSmile and bSmile or (not aSmile and not bSmile)

# Test code
assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False
assert monkey_trouble(False, True) == False