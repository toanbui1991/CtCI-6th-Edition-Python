"""
problem: check a string is another rotation of another string.
analyze: 
    #pick a point in string and lift the left to the right side of string. Example: abcde -> bcdea
    #if s2 is rotation from s1, therefore len(s1) == len(s2)
    #if s2 is rotation from s1 if s2 in s1*2
"""
def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False
