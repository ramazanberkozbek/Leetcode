"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
"""

#İlk aklıma gelen çözüm
#def isAnagram(s: str, t: str) -> bool:
#    return sorted(s) == sorted(t)

#2
from collections import defaultdict

def isAnagram(s,t):
    char_count = defaultdict(int)
    
    #for i in range(len(s)):
    for i,j in zip(s,t):
        char_count[ord(i)] += 1
        char_count[ord(j)] -= 1
    if (max(char_count.values()) == 0):
        return True
    return False
        

    
s = "aaac"
t = "aaab"
print(isAnagram(s,t))