"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.  
Input: s = "egg", t = "add"
Output: true  
"""


def isIsomorphic(s,t):
    mapS,mapT = {},{}
    
    for c1, c2 in zip(s, t):
        if (c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1):
            return False
        mapS[c1] = c2
        mapT[c2] = c1
    return True
    
print(isIsomorphic("baba","dede"))