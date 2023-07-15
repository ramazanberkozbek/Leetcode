"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
"""

def wordPattern(pattern,s):
    patternDict = {}
    sDict = {}
    sList = s.split(" ")
    
    if len(pattern) != len(sList):
        return False
    
    for i,j in zip(pattern,sList):
        if (i in patternDict and patternDict[i] != j) or (j in sDict and sDict[j] != i):
            return False
        patternDict[i] = j
        sDict[j] = i
    return True
    
    
print(wordPattern(pattern = "aaaa", s = "aa aa aa aa"))