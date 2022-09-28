
from collections import Counter

"""
problem: given s1, s2 string check that s2 container permutation of s1.
analyze: 
    permutation is change the order of element in sequence
    permutation have to have the same zine and count of each element have to be equal.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        k = len(s1)
        #loop through s2 to get substring
        for i in range(len(s2)):  # ---- O(n)
            #do not have out of range problem
            sub = s2[i:i+k]  # get sub string
            d2 = Counter(sub) # build counter of sub string
            if d1 == d2: #compare s1 with substring of s2
                return True
        return False



    def checkInclusion_rolling_hass(self, s1: str, s2: str) -> bool:
        #find length of the window
        k = len(s1)
        #counter object
        d1 = Counter(s1)
        
        # initial window
        window = s2[:k]
        d2 = Counter(window)
        
        # check the intial window 
        if d1 == d2:
            return True

        for i in range(len(s2)-k):
        
            # SLIDE THE WINDOW
            # 1 - remove s2[i]
            if d2[s2[i]] == 1:
                del d2[s2[i]]
            elif d2[s2[i]] > 1:
                d2[s2[i]] -= 1
            
            # 2- add s2[i+k]
            if s2[i+k] in d2:
                d2[s2[i+k]] += 1
            else:
                d2[s2[i+k]] = 1
                
            # check after sliding
            if d1 == d2:
                return True
                
        return False
            