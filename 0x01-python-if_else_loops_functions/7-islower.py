#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of the character is within the lowercase range (97-122)
    if 97 <= ord(c) <= 122:
        return True
    return False
