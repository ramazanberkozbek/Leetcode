"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.    
"""

from collections import defaultdict

def canConstruct(ransomNote,magazine):
    frequency = defaultdict(int)
    
    for word in ransomNote:
        frequency[word] += 1
    
    for word in magazine:
        frequency[word] -= 1
     
    if max(frequency.values()) > 0:
        return False
    return True

    
print(canConstruct("aba","baba"))