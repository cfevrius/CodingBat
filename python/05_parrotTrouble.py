def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

# Test case
assert  parrot_trouble(True, 6) == True
assert  parrot_trouble(True, 7) == False
assert  parrot_trouble(False, 6) == False
assert  parrot_trouble(True, 21) == True
assert  parrot_trouble(False, 21) == False
assert  parrot_trouble(False, 20) == False
assert  parrot_trouble(True, 23) == True
assert  parrot_trouble(False, 23) == False
assert  parrot_trouble(True, 20) == False
assert  parrot_trouble(False, 12) == False