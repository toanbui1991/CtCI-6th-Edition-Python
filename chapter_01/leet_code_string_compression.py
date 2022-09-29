from typing import List
"""
problem: given a list of string, construct compressed string and then compute the len of new list
analyze: 
    
"""
def compress(self, chars: List[str]) -> int:
    walker, runner = 0, 0
    #using runner pointer to loop through chars
    while runner < len(chars):
        #update for construct new chars list
        chars[walker] = chars[runner]
        count = 1
        #update count and runner when prev = current
        while runner + 1 < len(chars) and chars[runner] == chars[runner+1]:
            runner += 1
            count += 1
        
        if count > 1:
            for c in str(count):
                chars[walker+1] = c
                walker += 1
        
        runner += 1
        walker += 1
    
    return walker

def compress_v2(self, chars: List[str]) -> int:
    #the goal is construct a new list of chars 
    #why do we need two loop: inner loop to count number of each chars
    #the outer loop is for loop throug the first element in group
    #the inner loop is to count number of element and del element after we have count
    #and we handle the numerial digit.
    r_index = 0
 
    # outer loop
    while r_index < len(chars):
        
        # count at least 1 for first char we look at
        count = 1
        
        # inner loop - how far can we go
        while r_index + 1 < len(chars) and chars[r_index] == chars[r_index + 1]:
            count += 1
            del chars[r_index + 1] #delete next char because it is the same as curr charr
            
        # now handle if count is numerical digit like 12 a characters,  "a", "1", "2"
        if count > 1:
            for char in str(count):
                chars.insert(r_index + 1, char)
                r_index += 1
        
        r_index += 1
    
    return len(chars)  